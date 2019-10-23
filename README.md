# 中英机器文本翻译

评测中英文本机器翻译的能力。机器翻译语言方向为中文到英文。


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

下面第一行是中文例句（数据集），第二行是人翻英文例句（数据集），之后一行是机翻（本模型）英文句子（实时生成）。

<pre>

< 是多次击打头部…… 是谁干的。
=  repeated banging to the head  . . .  . as to who did it  .
>   it  s a couple of times shooting  . . . who did  .
< 我自己都不想去描述。不怎么好看。
=  i do n t wan na think about what that looks like  . it  s not pretty  .
>   i do n t even want to describe myself  . it  s not so good  .
< 不过坏消息是你不够钱雇我了。
=  the bad news is that you ca n t afford me anymore  .
>   but the bad news is you  re not enough to hire me  .
< 他不接电话。我有点担心。
=  he  s not answering his cell  . i  m kind of freaking out  .
>   he  s not answering the phone  . i  m worried  .
< 什么女人啊，就是她跟着我们。
=  what a major bitch  . she  s the one who followed us  .
>   what woman   she  s following us  .
< 回到那里让我意识到这里才是我想呆的地方。
=  being back there made me realize this is where want to be  .
>   back there and make me realize where i want to stay  .
< 他怎么用" 试验中收集的其他数据" 做到的。
=  along with the rest of the data collected during the experiment  .
>   how did he collect other data of data in the experiment  .
< 我们得确保在这手术没做之前
=  we need to make sure this whole thing does n t fall apart
>   we need to make sure that we do n t have anything
< 是的。但是不要告诉别人是我告诉你的。噢，我不会。
=  yes  . but do n t tell anyone i told you  . oh   i wo n t  .
>   yeah  . but do n t tell anyone i told you  . oh   i wo n t  .
< 抱歉，只是个恶梦。几点了？
=  sorry  . it was just a bad dream  . what time is it  ?
>   sorry  . it  s just a nightmare  . what time is it  ?


</pre>