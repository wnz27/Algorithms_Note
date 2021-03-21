<!--
* @UpdateTime : 2021/3/20 5:58 下午
* @description: type some description
* @Author: a27
-->
# 目标

数据如何在计算机中进行组织和存储，使我们可以高效的获取数据或者修改数据

# 动态数组
## resize 的复杂度分析
最坏的复杂度是O(n)
但问题是根本不可能每次都是需要扩容的
> 分析：
>先从一般分析：假如目标到k扩容，之前的操作数是k，k+1时 扩容k，所以整个k+1次add实际使用时间是2k + 1，
>那么平均是2k+1/k 约等于 2 得出O(1)的复杂度

>再到特殊分析：扩容契机是k + 1， 2k + 1， 4k + 1，8k + 1，。。。。。2nk + 1 = k + ... + 2nk + n

>总的操作数是 k + 1 + 2k+1 + 4k+1 +.......2nk+1 , 式一 k 加到 2nk + n

>实际操作了k + k + 1 + 2k + 2k + 1 + 4k + 4k + 1 + ....... + 2nk + 2nk + 1  式二 k加到 2nk乘以2再加n

> (k +....+2nk) * 2 + n / k + ....2nk + n 

>所以复杂度是 式二除以式一，得出O(1)复杂度,也是常数阶

这就是均摊复杂度  amortized time complexity

## 复杂度震荡
该扩容的时候addLast
之后立即removeLast
然后addLast
然后removeLast
这种情况
这几个操作都是O(n)
> 原因: removeLast时resize过于着急

> 解决办法: Lazy
 
> 删除操作时先不缩容，等实际元素到容量的四分之一再缩容 size = capacity / 4




