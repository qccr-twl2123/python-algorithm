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

