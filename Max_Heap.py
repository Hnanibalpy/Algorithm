#coding:utf-8

def Max_Heapify (A, i):
    # 求得左右子节点
    L_i = 2*i+1
    R_i = 2*i+2
    A_len = len(A)
    # 分别对左右子节点进行比较，如果子节点大于父节点就进行交换
    if ((L_i < A_len)and(A[L_i]>A[i])):
        largest = L_i
    else:
        largest = i
    if ((R_i < A_len)and(A[R_i]>A[largest])):
        largest = R_i
    else:
        largest = largest
    if (largest != i):
        # 对进行交换过的节点再次比较
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A, largest)

def Build_Max_Heap (A):
    A_len = len(A)
    # 从最后一个节点的父节点开始
    A_start = int((A_len-1)/2)
    for i in range(A_start, -1, -1):
        Max_Heapify(A, i)
B_Heap = []
def Heap_Sort (A):
    Build_Max_Heap(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        B_Heap.append(A.pop())
        Max_Heapify(A, 0)

if __name__ == "__main__":
    Heap_list = [40, 99, 87, 3, 45, 9, 13, 69, 54, 27, 61, 102, 98, 35, 88, 203]
    Build_Max_Heap(Heap_list)
    print(Heap_list)
    Heap_Sort(Heap_list)
    print(Heap_list)
    print(B_Heap)