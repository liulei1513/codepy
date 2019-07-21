import time
start_time = time.perf_counter()

list_ = [9, 2, 7, 4, 5, 6, 3, 8, 1]



# 堆排序(通过不断的构造最大堆来选出序列的最大值放到末尾)
# 最大堆调整：将堆的末端子节点调整，使得子节点永远小于父节点。
# 建立最大堆：将堆所有数据重新排序。
# 堆排序：移除位在第一个数据的根节点，并做最大堆调整的递归运算。
import random


def max_heapify(heap, heapsize, root):
    # 最大堆调整
    left = 2 * root + 1
    right = left + 1
    larger = root
    if left < heapsize and heap[larger] < heap[left]:
        larger = left
    if right < heapsize and heap[larger] < heap[right]:
        larger = right
    if larger != root:
        heap[larger], heap[root] = heap[root], heap[larger]
        max_heapify(heap, heapsize, larger)


def build_max_heap(heap):
    # 构造一个堆，将堆中所有数据重新排序
    heapsize = len(heap)
    for i in range((heapsize - 2) // 2, -1, -1):
        max_heapify(heap, heapsize, i)


def heapsort(heap):
    # 将根节点去除与最后一位做对调，对前面len-1个节点继续进行对调整过程。
    build_max_heap(heap)
    for i in range(len(heap) - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        max_heapify(heap, i, 0)
    return heap


if __name__ == '__main__':
    a = [30, 50, 57, 77, 62, 78, 94, 80, 84]
    print(a)
    heapsort(a)
    print(a)
    # b = [random.randint(1, 1000) for i in range(1000)]
    # print(b)
    # heapsort(b)
    # print(b)
# --------------------------------------------------------------

# 归并排序
# 首先用分割的方法将这个序列分割成一个个已经排好序的子序列，然后
# 再利用归并的方法将一个个的子序列合并成排序号的序列
def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0)) if left[0] < right[0] else result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


def mergesort(l):
    if len(l) < 2:
        return l
    mid_index = len(l) // 2
    left = mergesort(l[:mid_index])
    right = mergesort(l[mid_index:])
    return merge(left, right)


print(mergesort(list_))
# --------------------------------------------------------------

# 希尔排序 将序列分割成若干子序列（由相隔某个增量的元素组成的）分别进行直接插入排序接着依次缩小增量继续进行排序，待整个序列基本有序时，再对全体元素进行插入排序。
def shell_sort(l):
    n = len(l)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = l[i]  # 每个步长进行插入排序
            j = i
            # 插入排序
            while j >= gap and l[j - gap] > temp:
                l[j] = l[j - gap]
                j -= gap
            l[j] = temp
        gap = gap // 2
    return l


print(shell_sort(list_))
# --------------------------------------------------------------

# 插入排序 
# 从索引1开始，一次与其左边的数相比较，若比自己大则插入并删除自己。
def insertsort(l):
    len_ = len(l)
    for i in range(1, len_):
        for j in range(i):
            if l[j] > l[i]:
                l.insert(j, l[i])
                l.pop(i+1)
                break
    return l


print(insertsort(list_))
# --------------------------------------------------------------

# 快速排序
# 选定一个基数如第一个元素
# 将比基数小的和比基数大的元素分别放在新列表里并按顺序排列相加
# 递归直到新列表元素只有一个
def quicksort(l):
    len_ = len(l)
    if len_ < 2:
        return l
    else:
        pivot = l[0]
        less = [i for i in l[1:] if i <= pivot]
        greater = [j for j in l[1:] if j > pivot]
        print(less, greater)
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort(list_))
# --------------------------------------------------------------

# 选择排序
# 上述选择排序代码存在问题，这次复习自己重写时发现对重复数字处理不对，同时循环也有问题。以下是更改后代码：
def selectsort(l):
    length = len(l)
    for i in range(length-1):
        m = min(l[i+1:])  # 当前数字右边的数字列表中的最小数
        j = l[i+1:].index(m) + i + 1  # m的索引，防止重复数字的干扰 
        if l[i] > m:
            l[i], l[j] = l[j], l[i]
    return l

print(selectsort(list_)) 
# --------------------------------------------------------------

# 冒泡排序
# 从索引0开始依次本身和右边的元素，若右边小则调换位置，来取得最大值
# 然后依次循环把较大的轮换到右边
def bubblesort(l):
    len_ = len(l)
    for i in range(len_ - 1):
        for j in range(len_ - i - 1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l


print(bubblesort(list_))


end_time = time.process_time()
print(end_time - start_time)