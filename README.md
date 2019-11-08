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

< 你帮我们看一下这里少了些什么东西？
= just take a look around and you notice anything missing or out of place ?
> can you take a look at what  s missing here ?
< 如果告诉了，你我就有大麻烦。
= if i tell you   i am in deep trouble .
> if i tell you   i  m in big trouble .
< 因为你们俩隐瞒了关于昨晚和儿子所谓的争吵之事。
= with held information from me about the so   called family argument last night .
> because the two of you were hiding what you said about last night and your son .
< 他现在的唯一要求就是我们能到选举结束之后再宣布这件事。
= all he  s asking is that we hold off on the announcement until after the election .
> his only request now is that we can make the announcement after the election .
< 但明天还有很长的路要走。我要睡觉。
= but i got a long road tomorrow  . i need to sleep .
> but there  s a long way to go tomorrow  . i need to sleep .
< 我要她知道我跟你一样支持她。
= and i wanted her to know that you and i were the same in our feelings .
> i want her to know that i support her just as much as you do .
< 您会受到家人一般的待遇，在宽敞的客房中感到彻底的放松。
= rest assured you  ll be treated like family and feel completely relaxed in our spacious rooms .
> you will feel completely relaxed in a spacious room with family treatment .
< 好好体会付出感情的滋味吧，或者这是你的第一次呢。
= and focus more on what it feels like to give love   maybe for the first time in your life .
> feel what it  s like to give love   or this is your first time .
< 希望你不要介意。我按过门铃但没人回应。
= i hope you do n t mind  . i tried to ring the bell   but nobody answered .
> i hope you do n t mind  . i ring the bell   but no one answered .
< 所以你为什么不告诉我这到底是怎么回事。
= so why do n t you just tell me what the hell this is all about .
> so why do n t you tell me what  s going on .

</pre>