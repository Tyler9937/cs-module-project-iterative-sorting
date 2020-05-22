def selection_sort(arr):
    for i in range(len(arr)):
        sml_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[sml_idx]:
                sml_idx = j
        arr[i], arr[sml_idx] = arr[sml_idx], arr[i]
    return arr


def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    

# STRETCH: implement the Count Sort function below
def count_sort(arr):
    index = [0] * 200
    for i in arr:
        if i < 0:
            return "Error, negative numbers not allowed in Count Sort"
        index[i] += 1
    for i in range(1, len(index)):
        index[i] += index[i-1]
    for i in range(len(index)-1, 0, -1):
        index[i] = index[i-1]
    index[0] = 0
    ans = [0] * len(arr)
    for x in arr:
        i = index[x]
        ans[i] = x
        index[x] += 1
    return ans