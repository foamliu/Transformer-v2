# 英中机器文本翻译

评测英中文本机器翻译的能力。机器翻译语言方向为英文到中文。


## 依赖

- Python 3.6.8
- PyTorch 1.3.0

## 数据集

我们使用AI Challenger 2017中的英中机器文本翻译数据集，超过1000万的英中对照的句子对作为数据集合。其中，训练集合占据绝大部分，为12904955对，验证集合8000对，测试集A 8000条，测试集B 8000条。

可以从这里下载：[英中翻译数据集](https://challenger.ai/datasets/translation)

![image](https://github.com/foamliu/Transformer/raw/master/images/dataset.png)

## 用法

### 数据预处理
提取训练和验证样本：
```bash
$ python extract.py
$ python pre_process.py
```

### 训练
```bash
$ python train.py
```

要想可视化训练过程，在终端中运行：
```bash
$ tensorboard --logdir path_to_current_dir/logs
```

### Demo
下载 [预训练模型](https://github.com/foamliu/Scene-Classification/releases/download/v1.0/model.85-0.7657.hdf5) 然后执行:

```bash
$ python demo.py
```

下面第一行是中文例句（数据集），第二行是人翻英文例句（数据集），之后一行是机翻（本模型）的英文句子（实时生成）。

<pre>

< 我是说，我觉得你俩能说到一起。
= i mean   i saw the connection between the two of you .
> i mean   i think you two can talk together .
< 酒店提供免费无线网络，商务中心和升级豪华套房住宿，让您更加愉快地入住。
= complimentary wi fi   business center and our upgraded deluxe suite accommodations will make your stay even more enjoyable .
> the hotel offers free wireless internet   business center and a deluxe suite to make you feel better .
< 我没有这样想。- 不，你不是荡妇。
= i do n t think so  .   no   you  re not a slut .
> i do n t think so  .   no   you  re not a slut .
< 他将对光芒的恐惧，作为借口困你们于此，
= he  s trapped you here with fear   fear of the light
> the fear of the light   as an excuse you here
< 我们的枪。该死的，少校！拒绝这样的机会！
= our guns  . damn it   major ! to pass up such a chance !
> our guns  . damn it   major ! refuse !
< 他才负责我们婚礼16个小时，
= he  s been in charge of our wedding for exactly   hours
> he  s in charge of our wedding for   hours
< 对你也不想拿着那些玩意到处走。
= right    cause you do n t wannawalk around with that kind of cabbage .
> yeah   and you do n t want to walk around with that stuff .
< 恐怖分子拥有军用级神经毒气。
= these terrorists have possession of a military   grade nerve agent .
> the terrorists have military nerve gas .
< 我要迟到了得走了，
= i  . . . i  m going to be late   so i better get going
> i  m late  . i gotta go
< 呃，我的老板最近也不太好相处。
= yeah   my boss has n t exactly been a joy to be around lately   either .
> well   my boss has n t been very good lately .

</pre>