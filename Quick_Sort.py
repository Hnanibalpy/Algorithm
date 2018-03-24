#coding:utf-8

def PARTITION (A, p, r):
    first_num = p-1
    last_num = A[r]
    for i in range(p, r):
        # 以最后一位元素为主元X判定是否进行交换
        if (A[i] <= last_num):
            first_num = first_num + 1
            A[first_num], A[i] = A[i], A[first_num]
    # 将主元X移动到数组中间
    A[first_num+1], A[r] = A[r], A[first_num+1]
    # 返回主元X下标
    return first_num+1

def Quick_Sort (A, p, r):
    # 判定排序条件
    if (p < r):
        q = PARTITION(A, p, r)
        # 返回主元X大小左右两边的乱序数组进行递归
        Quick_Sort(A, p, q-1)
        Quick_Sort(A, q+1, r)

if __name__ == '__main__':
    A_list = [12, 23, 3, 9, 87, 41, 29, 44, 76, 27, 10, 77, 103, 33, 8, 19, 2, 56, 81]
    start = 0
    last = len(A_list)-1  # 数组最后一个元素
    Quick_Sort(A_list, start, last)
    print(A_list)