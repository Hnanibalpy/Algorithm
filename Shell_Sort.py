#coding:utf-8

def Shell_Sort (A):
    A_length = len(A)
    head = 1
    while (head < A_length/3):
        head = 3*head + 1

    while (head >= 1):
        for i in range(head, A_length):
            j = i
            #print(j)

            while ((j >= head)&(A[j] < A[j - head])):
                A[j], A[j - head] = A[j - head], A[j]
                j = j - head
                #print(A)
        head = int(head/3)


if __name__ == '__main__':
    List = [4, 0, 8, 1, 88, 37, 2, 91, 66, 5, 23, 4, 4, 87, 102, 907, 823, 63, 81]
    Shell_Sort(List)
    print(List)