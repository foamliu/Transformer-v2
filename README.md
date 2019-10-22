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

下面第一行是英文例句（数据集），第二行是人翻中文例句（数据集），之后五行是机翻（本模型）中文句子（实时生成）。

<pre>

< 我没有注意到我的妻子是否在床上。
=  i did not notice if my wife was in bed  .
>   i did n t notice if my wife was in bed  .
< 我知道你们都需要我，但我需要你们时我会打电话。
=  and i know you all need me   but i  ll call you if i need any of you  .
>   i know you all need me   but i  ll call you when i need you  .
< 在距离南美海岸700英里的地方
=  lying over   miles off the coast of south america
>     miles from south america coast
< 必须找到他记得让他给我回电话。
=  you do that and you tell him to call me  .
>   we have to find him   remember him to call me back  .
< 所以我没兴趣听什么演员来演讲。
=  so i  m not really interested in having some actor lecture me  .
>   so i  m not interested in hearing a speech  .
< 今晚你可以把电脑拿到厨房来用
=  you can use the computer right here in the kitchen tonight
>   you can take your computer to the kitchen tonight
< 我以前从没穿过这件西装所以没发现过。
=  i never found it  cause i have n t worn this suit before  .
>   i  ve never been through this suit before  .
< 我们做了什么？他做了什么？他都跟你说了什么？
=  what did we do  ? what did he do  ? what  d he tell you  ?
>   what did we do  ? what did he do  ? what did he tell you  ?
< 像你这样的人是如何有了这么大的一家公司的呢？
=  how exactly did a guy like you get to own a major corporation  ?
>   how does a guy like you have such a company  ?
< 我们只要知道它在那儿。我们只要知道它很安全。
=  we need to know it  s there  . we need to know it  s safe  .
>   we just need to know it  s there  . we just need to know it  s safe  .

</pre>