1、选择排序
选择排序是一种简单直观的排序算法。它的原理是这样：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的后面，以此类推，直到所有元素均排序完毕。算法实现如下：

#找到最小的元素
def FindSmall(list):
    min=list[0]
    for i in range(len(list)):
        if list[i]<min:
            min=list[i]
    return min        

#选择排序
def Select_Sort(list):
    newArr=[]
    for i in range(len(list)):
        minValue=FindSmall(list)
        newArr.append(minValue)
        list.remove(minValue)
    return newArr

testArr=[11,22,33,21,123]
print(Select_Sort(testArr))


2、快速排序
快速排序的运行速度快于选择排序，它的工作原理是这样：设要排序的数组是N，首先任意选取一个数据（通常选用数组的第一个数）作为关键数据，然后将所有比它小的数都放到它前面，所有比它大的数都放到它后面，这个过程称为一趟快速排序。可以使用python用递归式的方法来解决这个问题：

def Quick_Sort(list):
    if len(list)<2:
        return list
    else:
        temp=list[0]
        less=[i for i in list[1:] if i<=temp]
        more=[i for i in list[1:] if i>temp]
        return Quick_Sort(less)+[temp]+Quick_Sort(more)

testArr= [13,44,53,24,876,2]
print(Quick_Sort(testArr))

3、二分查找
二分查找的输入是一个有序的列表，如果要查找的元素包含在一个有序列表中，二分查找可以返回其位置。打个比方来说明二分查找的原理：比如我随便想了个范围在1~100以内的整数，由你来猜，以最少的次数来猜出这个数字，你每次猜完给出个数字，我会回复大了或小了，第一种方法是你从1开始依次往后猜，那如果我想的数字是100，那么你就要猜100次；第二种方法是从50开始，如果我说小了，那你就猜75，就这样依次排除掉一半的剩余数字，这就是二分查找法。可以看出二分查找法更加快速。对于包含n个元素的有序列表，用简单查找最多需要n步，而二分查找法则最多只需lon2 n步。下面用python来实现该算法：

def Item_Search(list,item):
    low=0
    high=len(list)-1
    while low<=high:
        middle=(low+high)//2
        print(list[middle])
        if list[middle]>item:
            high=middle-1
        elif list[middle]<item:
            low=middle+1
        else:
            return middle
    return None        

test_list=[1,3,5,7,9,11,13,15,17,19,21]
Item_Search(test_list,11)

4、广度优先搜索
广度优先搜索是一种图算法，图由节点和边组成，一个节点可能与多个节点连接，这些节点称为邻居。广度优先搜索算法可以解决两类问题：第一类是从节点A出发，有没有前往节点B的路径；第二类问题是从节点A出发，前往B节点的哪条路径最短。使用广度优先搜索算法的前提是图的边没有权值，即该算法只用于非加权图中，如果图的边有权值的话就应使用狄克斯特拉算法来查找最短路径。举个例子，假如你认识alice、bob、claire，bob认识anuj、peggy，alice认识peggy，claire认识tom、jonny，你需要在最短的路径内找到通过认识的人找到tom，那么算法实现如下：

#使用字典构建图
graph={}
graph["you"]=["Alice","Bob","Claire"]
graph["Bob"]=["Anuj","Peggy"]
graph["Alice"]=["Peggy"]
graph["Claire"]=["Tom","Jonny"]
graph["Anuj"]=[]
graph["Peggy"]=[]
graph["Tom"]=[]
graph["Jonny"]=[]

from collections import deque

#简单的判断方法
def person_is_seller(name):
    return name=='Tom'

def Search(name):
    searched=[]   #用于记录检查过的人，防止进入死循环
    search_queue=deque()  #创建队列
    search_queue+=graph[name]
    while search_queue:
        person=search_queue.popleft()
        if not person in searched:    #仅当这个人没检查过时才检查
            if person_is_seller(person):
                print("the seller is {0}".format(person))
                return True
            else:
                search_queue+=graph[person]
                searched.append(person)   #将这个人标记为检查过
    return False

print(Search("you"))

5、贪婪算法
贪婪算法，又名贪心算法，对于没有快速算法的问题（NP完全问题），就只能选择近似算法，贪婪算法寻找局部最优解，并企图以这种方式获得全局最优解，它易于实现、运行速度快，是一种不错的近似算法。假如你是个小偷，商店里有很多箱子，箱子里有各种水果，有些箱子里有3种水果，有些箱子有2种...，你想尝到所有种类的水果，但你一个人力气有限，因此你必须尽量搬走最少的箱子，那么，算法实现如下：

fruits=set(["苹果","香蕉","梨子","西瓜","草莓","橘子","荔枝","榴莲"]) 

#箱子以及包含的水果
box={}
box["b1"]=set(["苹果","香蕉","西瓜"])
box["b2"]=set(["草莓","橘子","榴莲"])
box["b3"]=set(["梨子","荔枝","草莓"])
box["b4"]=set(["香蕉","橘子"])
box["b5"]=set(["梨子","榴莲"])

final_boxs=set() #最终选择的箱子


#直到fruits为空
while fruits:
    best_box=None  #包含了最多的未包含水果的箱子
    fruits_covered=set()  #包含该箱子包含的所有未包含的水果

    #循环迭代每个箱子，并确定它是否为最佳箱子
    for boxItem,fruitItem in box.items():
        covered=fruits & fruitItem  #计算交集
        if len(covered)>len(fruits_covered):  
            best_box=boxItem
            fruits_covered=covered
    fruits-=fruits_covered
    final_boxs.add(best_box)
      
print(final_boxs)