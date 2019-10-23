# import the necessary packages
import pickle
import random
import time

import numpy as np
import torch
from nltk.tokenize.treebank import TreebankWordDetokenizer

from config import device, logger, data_file, vocab_file, sos_id, eos_id
from transformer.transformer import Transformer

if __name__ == '__main__':
    filename = 'transformer-v2.pt'
    print('loading {}...'.format(filename))
    start = time.time()
    model = Transformer()
    model.load_state_dict(torch.load(filename))
    print('elapsed {} sec'.format(time.time() - start))
    model = model.to(device)
    model.eval()

    logger.info('loading samples...')
    start = time.time()
    with open(data_file, 'rb') as file:
        data = pickle.load(file)
        samples = data['valid']
    elapsed = time.time() - start
    logger.info('elapsed: {:.4f} seconds'.format(elapsed))

    logger.info('loading vocab...')
    start = time.time()
    with open(vocab_file, 'rb') as file:
        data = pickle.load(file)
        src_idx2char = data['dict']['src_idx2char']
        tgt_idx2char = data['dict']['tgt_idx2char']
    elapsed = time.time() - start
    logger.info('elapsed: {:.4f} seconds'.format(elapsed))

    samples = random.sample(samples, 10)
    detokenizer = TreebankWordDetokenizer()

    for sample in samples:
        sentence_in = sample['in']
        sentence_out = sample['out']

        input = torch.from_numpy(np.array(sentence_in, dtype=np.long)).to(device)
        input_length = torch.LongTensor([len(sentence_in)]).to(device)

        sentence_in = ''.join([src_idx2char[idx] for idx in sentence_in])
        sentence_out = ' '.join([tgt_idx2char[idx] for idx in sentence_out if idx not in [sos_id, eos_id]])
        sentence_out = detokenizer.detokenize(sentence_out)
        print('< ' + sentence_in)
        print('= ' + sentence_out)

        with torch.no_grad():
            nbest_hyps = model.recognize(input=input, input_length=input_length, char_list=tgt_idx2char)
            # print(nbest_hyps)

        for hyp in nbest_hyps:
            out = hyp['yseq']
            out = [tgt_idx2char[idx] for idx in out if idx not in [sos_id, eos_id]]
            out = detokenizer.detokenize(out)

            print('> {}'.format(out))
