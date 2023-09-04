#Binary Search

list1 = [-4, 2, 5, 9, 10, 11, 50, 53, 69, 77, 89, 91, 93, 99, 102] # must be sorted
def binarysearch(value, start, end): # search for value in l[start:end]
    global list1
    if start < end: # while there is at least one element
        mid = (start + end) // 2
        if list1[mid] == value: # found the element
            return mid
        
        elif list1[mid] < value: # go to the right half
            return binarysearch(value, mid + 1, end)
        else: # go to the left half
            return binarysearch(value, start, mid)
    else: # did not find the key
        return -1

print(binarysearch(10, 0, len(list1))) # 4
# print(binarysearch(-4, 0, len(list1))) # 0
# print(binarysearch(12, 0, len(list1))) # -1
# print(binarysearch(92, 0, len(list1))) # -1
# print(binarysearch(102, 0, len(list1))) # 14
# print(binarysearch(111, 0, len(list1))) # -1