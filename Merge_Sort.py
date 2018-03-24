#coding:utf-8

def Merge_Sort (A_list, lo, mid, hi):
    i = lo
    j = mid + 1

    for k in range(lo, hi+1):
        aux[k] = A_list[k]

    for k in range(lo, hi+1):
        if (i > mid):
            A_list[k] = aux[j]
            j = j + 1
        elif (j > hi):
            A_list[k] = aux[i]
            i = i + 1
        elif (aux[j] < aux[i]):
            A_list[k] = aux[j]
            j = j + 1
        else:
            A_list[k] = aux[i]
            i = i + 1

def M_sort (A_list, lo, hi):
    if (hi <= lo):
        return

    mid = lo + int((hi - lo)/2)
    M_sort(A_list, lo, mid)
    M_sort(A_list, mid + 1, hi)
    Merge_Sort(A_list, lo, mid, hi)


if __name__ == '__main__':
    list = [3,8,97,5,64,0,33,51,87,87,45,29,10,44,37,28,75,58,31,93,109,75,24,96,36]
    aux = [0] * len(list)
    M_sort(list, 0, len(list)-1)
    print(list)