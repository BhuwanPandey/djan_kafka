def merge_count_inversion(arr, temp_arr, left, mid, right):
    i = left  # Starting index for left subarray
    m = mid + 1  # Starting index for right subarray
    k = i  # Starting index to be sorted
    inv_count = 0

    while i <= mid and m <= right:
        if arr[i] <= arr[m]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[m]
            inv_count += mid - i + 1
            m += 1
        k += 1

    # Copy the remaining elements of left subarray, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy the remaining elements of right subarray, if any
    while m <= right:
        temp_arr[k] = arr[m]
        m += 1
        k += 1

    # Copy the sorted subarray into the original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    return inv_count


def merge_count_split(arr, temp_arr, left, right):
    if left >= right:
        return 0
    mid = (left + right) // 2
    inv_count = 0
    inv_count += merge_count_split(arr, temp_arr, left, mid)
    inv_count += merge_count_split(arr, temp_arr, mid + 1, right)

    inv_count += merge_count_inversion(arr, temp_arr, left, mid, right)
    return inv_count


def Solution(arr):
    arr_length = len(arr)
    temp_arr = [0] * arr_length
    inversion_count = merge_count_split(arr, temp_arr, 0, arr_length - 1)
    if inversion_count > 1000000000:
        return -1

    return inversion_count


result = Solution([-2, 147, 483, 648, 2, 147, 483, 647])
# print(Solution([-1,6,3,4,7,4]))
print(result)
