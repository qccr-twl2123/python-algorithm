# 贝叶斯算法入门


## 前言
贝叶斯推断（Bayesian inference）是一种统计学方法，用来估计统计量的某种性质。
公式为
```
   P(A|B) = P(A)(P(B|A)/P(B)) 
   后验概率 = 先验概率 X 调整因子 
```
## 公式推导过程
要理解贝叶斯推断，必须先理解贝叶斯定理。后者实际上就是计算"条件概率"的公式。
所谓"条件概率"（Conditional probability），就是指在事件B发生的情况下，事件A发生的概率，用P(A|B)来表示。

![输入图片说明](https://github.com/qccr-twl2123/python-algorithm/blob/master/resources/bg2011082502.jpg "在这里输入图片标题")

根据文氏图，可以很清楚地看到在事件B发生的情况下，事件A发生的概率就是P(A∩B)除以P(B)。

![输入图片说明](https://github.com/qccr-twl2123/python-algorithm/blob/master/resources/chart.png "在这里输入图片标题")

因此，

![输入图片说明](https://github.com/qccr-twl2123/python-algorithm/blob/master/resources/chart1.png "在这里输入图片标题")

同理

![输入图片说明](https://github.com/qccr-twl2123/python-algorithm/blob/master/resources/chart2.png "在这里输入图片标题")

所以

![输入图片说明](https://github.com/qccr-twl2123/python-algorithm/blob/master/resources/chart3.png "在这里输入图片标题")

即

![输入图片说明](https://github.com/qccr-twl2123/python-algorithm/blob/master/resources/chart5.png "在这里输入图片标题")

这就是条件概率的计算公式

### 全概率公式推导
除了条件概率以外，这里还要推导全概率公式。
假定样本空间S，是两个事件A与A'的和。

![输入图片说明](https://github.com/qccr-twl2123/python-algorithm/blob/master/resources/bg2011082503.jpg "在这里输入图片标题")

上图中，红色部分是事件A，绿色部分是事件A'，它们共同构成了样本空间S。
在这种情况下，事件B可以划分成两个部分。

![输入图片说明](https://github.com/qccr-twl2123/python-algorithm/blob/master/resources/bg2011082504.jpg "在这里输入图片标题")

即

![输入图片说明](https://github.com/qccr-twl2123/python-algorithm/blob/master/resources/chart6.png "在这里输入图片标题")

在上一节的推导当中，我们已知

![输入图片说明](https://github.com/qccr-twl2123/python-algorithm/blob/master/resources/chart7.png "在这里输入图片标题")

所以

![输入图片说明](https://github.com/qccr-twl2123/python-algorithm/blob/master/resources/chart8.png "在这里输入图片标题")

这就是全概率公式。它的含义是，如果A和A'构成样本空间的一个划分，
那么事件B的概率，就等于A和A'的概率分别乘以B对这两个事件的条件概率之和。

将这个公式代入上一节的条件概率公式，就得到了条件概率的另一种写法：

![输入图片说明](https://github.com/qccr-twl2123/python-algorithm/blob/master/resources/chart9.png "在这里输入图片标题")
