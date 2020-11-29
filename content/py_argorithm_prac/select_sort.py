'''
Date: 2020-11-29 21:42:42
LastEditTime: 2020-11-29 23:10:53
'''

def select_sort(arr):
    len_arr = len(arr)
    for i in range(len_arr):
        min_index = i
        for j in range(i+1, len_arr):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

if __name__ == "__main__":
    a = [1, 2, -30, 399, 46, -3454, -40, 200]
    s_a = select_sort(a)
    print(s_a)
    pass
