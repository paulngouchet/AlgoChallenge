# merge sort

def merge(nums1, nums2):
    result = []
    i, j = 0, 0
    while (i < len(nums1) and j < len(nums2)):
        if nums1[i] <= nums2[j]:
            result.append(nums1[i])
            i += 1
        elif nums2[i] <= nums1[i]:
            result.append(nums2[j])
            j += 1

    if i < len(nums1):
        result += nums1[i:]
    elif j < len(nums2):
        result += nums2[j:]

    return result


def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    floor = len(nums) // 2
    left = merge_sort(nums[:floor])
    right = merge_sort(nums[floor:])
    return merge(left, right)

print(merge_sort([1, 5, 6, 8, 3, 0]))
