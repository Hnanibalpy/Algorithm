#coding:utf-8

def closs_mid (list_a, low, mid, high):
    global max_right
    global max_left
    # 求得跨越中点的最大子数组
    left_num = -99999999
    num = 0
    left_list = []
    for n in range(low, mid):
        left_list.append(n)
    left_list.reverse()
    # 构建左边mid downto low的数组以方便迭代
    for i in left_list:
        num = num + list_a[i]
        if (num > left_num):
            left_num = num
            max_left = i
    right_num = -99999999
    num = 0
    for i in range(mid, high):
        num = num + list_a[i]
        if (num > right_num):
            right_num = num
            max_right = i
    return (max_left, max_right, left_num + right_num)

def maximum (list_b, low, high):
    global max_left
    global max_right
    max_right = 0
    max_left = 0
    if (high == low):
        return (low, high, list_b[0])
    else:
        mid = int((low + high)/2)
        (left_low, left_high, left_num) = maximum(list_b, low, mid)
        (right_low, right_high, right_num) = maximum(list_b, mid+1, high)
        (cross_low, cross_high, cross_num) = closs_mid(list_b, low, mid, high)
        if ((left_num >= right_num) and (left_num >= cross_num)):
            return (left_low, left_high, left_num)
        if ((right_num >= left_num) and (right_num >= cross_num)):
            return (right_low, right_high, right_num)
        else:
            return (cross_low, cross_high, cross_num)

if __name__ == '__main__':
    a = [34, 67, -23, -59, 14, -9, -76, 27, -3, 96, -88, 7]
    a_low = 0
    a_high = len(a)
    print(maximum(a, a_low, a_high))