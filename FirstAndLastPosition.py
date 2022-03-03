class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def binary_search(arr, l, r, x):
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] < x:
                    l = mid + 1
                elif arr[mid] > x:
                    r = mid - 1
                else:
                    least = binary_search(arr, l, mid - 1, target)
                    most = binary_search(arr, mid + 1, r, target)
                    output = [mid,mid]
                    if least != [-1,-1]:
                        output[0] = least[0]
                    if most != [-1,-1]:
                        output[1] = most[1]
                    return output
            return [-1,-1]
        return binary_search(nums, 0, len(nums) - 1, target)