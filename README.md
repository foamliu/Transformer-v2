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

< 去柏林的第一班车明早才出发。你现在想干啥？
= first bus to berlin does n t leave till tomorrow  . what do you wannado ?
> first bus to berlin is not leaving until morning  . what do you want now ?
< 呃，是我们朋友…… 他又带个女人同行吗？
= well   our friend  . . . did he have a woman with him ?
> uh   it  s our friend  . . . is he bringing a woman ?
< 我以我的母亲的名义发誓。
= i swear on the body and soul of my mother .
> i swear on my mother .
< 下了班，就搭免费飞机来。
= get on the plane when you get off work  . you fly for free .
> when you get off work   you get a free plane .
< 如果你读完之后能把那本圣经送回我房间。
= and i  d be grateful if you  d put that bible back in my room .
> if you finish it   you can send that bible back to my room .
< 地球没了大气层，就做不了我们的家
= without its atmosphere   the earth would not be a home to us
> without the atmosphere   we ca n t have our home
< 但其中一人背叛了他们。
= however   one of the seven would betray the other six .
> but one of them betrayed them .
< 不过，我想是因为没人在这做过这件事
= but i guess because no one ever done that before here
> but i think it  s because no one  s done it here
< 把自己的朋友带回家也是罪，吗妈？
= is it a sin to have friends now too mum ?
> it  s a crime to bring your friends home   mom ?
< 我要你知道你在和谁作对。我能看到，为什么要出去？
= to see what you  re up against  . i can see  . why come out ?
> i want you to know who you  re up against  . i can see that  . why go out ?

</pre>