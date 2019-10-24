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

< 宝贝，原来你以为我当时说分开。
= sweetie   you thought that when i said we were splitting up .
> baby   you thought i was separated .
< 斯蒂芬，有，有一件重要的事我必须要告诉你。
= stefan   th   there  s   there  s something important i have to tell you .
> steve   yes   there  s something important i have to tell you .
< 本无烟客房配有两张舒适大床，睡眠空间充足。
= this non smoking room has plenty of sleeping space with two comfortable queen beds .
> this non smoking room comes with two comfortable queen beds .
< 我要告诉他们真相你知道的。
= i  m going to have to tell them you know that .
> i  m going to tell them the truth   you know .
< 不过，我觉得想要唤醒她
= i just think   you know   if you want to wake her up
> but i think i want to wake her up
< 你回到家，不说话独自一人痛苦？
= gets home   does not speak and we will close your troubled world ?
> you come home   you do n t talk about pain ?
< 但是上班时，我带你去见他们
= but on your on   hours i bring you to men
> but at work   i  ll take you to them
< 你记得几年前关于我的投票吗？
= do you remember a few years ago   a vote about me ?
> do you remember a few years ago about my vote ?
< 我对比特币的声明做了语言匹配，猜猜我发现了什么？
= i did a linguistic match on the bitcoin manifesto   and guess what popped up ?
> i made a language of the language for the word   guess what i found ?
< 我也有这种感觉，听你这么说我就放心了。
= for i  m in the humor to  . does me good to hear you .
> i feel that way too   so i  m glad to hear you say that .


</pre>