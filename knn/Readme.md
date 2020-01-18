一、 算法是什么？
    算法是指解题方案的准确而完整的描述，是一系列解决问题的清晰指令，算法代表着用系统的方法描述解决问题的策略机制。也就是说，能够对一定规范的输入，在有限时间内获得所要求的输出。如果一个算法有缺陷，或不适合于某个问题，执行这个算法将不会解决这个问题。不同的算法可能用不同的时间、空间或效率来完成同样的任务。一个算法的优劣可以用空间复杂度与时间复杂度来衡量。


二、 时间复杂度：
    时间复杂度是用来估计算法运行时间的一个式子（单位）
    一般来说*，时间复杂度高的算法比复杂度低的算法慢   
    常见时间复杂度单位：效率从上到下变低，
        O(1)    简单的一次运算
        O(logn)    循环减半
        O(n)    一次循环
        O(nlogn)    一个循环加一个循环减半
        O(n^2)     两个循环
        O(n^2logn)
        O(n^3)
             
    如何一眼判断时间复杂度？
        循环减半的过程àO(logn)
        几次循环就是n的几次方的复杂度



三、 空间复杂度
    空间复杂度是用来评估算法内存占用大小的单位
    
    空间换时间：如果需要增快算法的速度，需要的空间会更大

 

四、python实现常见的算法

　　1、冒泡（交换）排序

　　　　原理：列表中两个相邻的数，如果前一个数比后一个数大，就做交换。一共需要遍历列表的次数是len(lst)-1
    　　　时间复杂度：O(n^2)


def bubble_sort(lst):
    for i in range(len(lst)-1):     # 这是需要循环遍历多少次
        for j in range(len(lst)-i-1):   # 每次数组中的无序区
            if lst[j] >lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
 
lst = [1, 2, 44, 3, 5]
bubble_sort(lst)
print(lst)
　　

　　　　优化：如果在循环的时候，有一次没有进行交换，就表示数列中的数据已经是有序的
       　　时间复杂度：最好情况是0(n)，只遍历一次，一般情况和最坏情况都是O(n^2)


def bubble_sort(lst):
    for i in range(len(lst)-1):     # 这是需要循环遍历多少次
        change = False      # 做一个标志变量
        for j in range(len(lst)-i-1):   # 每次数组中的无序区
            if lst[j] >lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
                change = True   # 每次遍历，如果进来排序的话，就会改变change的值
        if not change:  # 如果change没有改变，那就表示当前的序列是有序的，直接跳出循环即可
            return
 
 
lst = [1, 2, 44, 3, 5]
bubble_sort(lst)
print(lst)
　　

　　2、选择排序

　　　　原理：每次遍历找到当下数组最小的数，并把它放到第一个位置，下次遍历剩下的无序区


def select_sort(lst):
    for i in range(len(lst) - 1):    # 当前需遍历的次数
        min_loc = i     # 当前最小数的位置
        for j in range(i+1, len(lst)):   # 无序区
            if lst[j] < lst[min_loc]:     # 如果有更小的数
                min_loc = j     # 最小数的位置改变
        if min_loc != i:
            lst[i], lst[min_loc] = lst[min_loc], lst[i]     # 把最小数和无序区第一个数交换交换
 
lst = [1, 2, 44, 3, 5]
select_sort(lst)
print(lst)
　　

　　3、插入排序
        　　原理：列表分为有序区和无序区，有序区是一个相对有序的序列，认为一开始的时候有序区有一值
        　　每次从无序区选择一个值，放到有序区，直到无序区为空


def insert_sort(lst):
    for i in range(1,len(lst)):     # 从1开始遍历表示无序区从1开始，有序区初始有一个值
        tmp = lst[i]    # tmp表示拿到的无序区的第一张牌
        j = i - 1   # j表示有序区的最后一个值
        while j >= 0 and lst[j] > tmp:  # 当有序区有值，并且有序区的值比无序区拿到的值大就一直循环
            lst[j+1] = lst[j]   # 有序区的值往后移
            j -= 1  # 找到上一个有序区的值，然后再循环
        lst[j+1] = tmp  # 跳出循环之后，只有j+1的位置是空的，要把当下无序区的值放到j+1的位置
 
lst = [1, 2, 44, 3, 5]
insert_sort(lst)
print(lst)
　　

二分插入：实际上并没有优化的效果

def insert_sort(lst):
    for i in range(1, len(lst)):
        left = 0
        right = i - 1
        tmp = lst[i]
        while left <= right:
            mid = (left + right) / 2
            if tmp >= lst[mid]:
                left = mid + 1
            if tmp < lst[mid]:
                right = mid - 1
        for j in range(i - 1, left - 1, -1):  # [i-1,left]
            lst[j + 1] = lst[j]
        lst[left] = tmp
 
    return lst
　　

　　4、快速排序

　　　　思路：取第一个元素，让它归位，就是放到一个位置，使它左边的都比它小，右边的都比它大，然后递归
            　　先归位，后递归

　　　　时间复杂度：O(nlog(n))

　　　　最坏情况：

　　　　　　最坏情况下的事件复杂度是O(n2)

　　　　　　标志数的左边或者右边只有一个数
            
              解决方法：不要找第一个元素，随机找一个元素

def parttion(lst, left, right):
    i = left
    j = right
    tmp = lst[i]    # 把此次循环的标志数存起来
    while i < j:
        while i < j and lst[j] > tmp:   # 先从右边开始找比标志数小的，有的话跳出循环
            j -= 1
        lst[i] = lst[j] # 跳出循环之后，把这个比标志数小的值放到标志数的位置
        while i < j and lst[i] < tmp:   # 左边的排序方法和右边一样
            i += 1
        lst[j] = lst[i]
    lst[i] = tmp    # 整个排序结束之后，把一开始的标志数放回空位
    return i
 
 
def quick_sort(lst, left, right):
    if left < right:    # 至少有两个元素
        p = parttion(lst, left, right)
        quick_sort(lst, left, p-1)
        quick_sort(lst, p+1, right)
         
 
lst = [1, 2, 44, 3, 5]
quick_sort(a, 0, 4)
print(lst)
　　

 
