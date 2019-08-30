import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return 
        if not nums1:
            return nums2[len(nums2)//2]
        if not nums2:
            return nums1[len(nums1)//2]

        if (len(nums1) + len(nums2)) % 2 == 0:
            k = (len(nums1) + len(nums2)) // 2
        else:
            k = (len(nums1) + len(nums2) + 1) // 2

        i = 0
        j = 0
        count = 0
        print('k: %s' %k)
        while count != k - 1:
            if i == len(nums1) - 1:
                j += 1
            if j == len(nums2) - 1:
                i += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
            count += 1
            print('i=%s\tj=%s\tcount=%s' %(i, j, count))
        if nums1[i] < nums2[j]:
            return nums1[i]
        else:
            return nums2[j]

    def findMedianSortedArraysV0(self, nums1, nums2):
        tmp = []
        if (len(nums1) + len(nums2)) % 2 == 0:
            k = (len(nums1) + len(nums2)) / 2
            count = 2
        else:
            k = (len(nums1) + len(nums2) - 1) / 2
            count = 1
        #print('k=%s' %k)
        i = 0
        j = 0
        while len(tmp) != k and i <= len(nums1) - 1 and j <= len(nums2) -1:
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1
            #print('---i=%s\tj=%s' %(i, j))
        #print('i=%s\tj=%s' %(i, j))
        #print('tmp: %s' %tmp)
        if len(tmp) != k:
            if i > len(nums1) - 1:
                while len(tmp) < k:
                    j += 1
            else:
                while len(tmp) < k:
                    i += 1

        if count == 1:
            return tmp[-1]
        else:
            return (tmp[-2] + tmp[-1]) / 2


    def findMedianSortedArraysV0(self, nums1, nums2):
        if (len(nums1) + len(nums2)) % 2 != 0:
            #one median
            k = (len(nums1) + len(nums2)) / 2
            medianIsTwo = False
        else:
            k = (len(nums1) + len(nums2)) / 2 - 1
            medianIsTwo = True

        count = 0
        i = 0
        j = 0
        while count <= k and i <= len(nums1) - 1 and j <= len(nums2) - 1:
            if nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
            count += 1

        while count != k and i <= len(nums1) - 1:
            i += 1
            count += 1
        while count != k and j <= len(nums2) - 1:
            j += 1
            count += 1

        if not medianIsTwo: 
            if i <= len(nums1) -1 and j <= len(nums2) -1:
                if nums1[i] < nums2[j]:
                    return nums1[i]
                else:
                    return nums2[j]
            elif i <= len(nums1) - 1:
                    return nums1[i]
            else:
                return nums2[j]
        else:
            median = 0
            if i <= len(nums1) =1 and j <= len(nums2) - 1:
                if nums1[i] < nums2[j]:
                    median += nums1[i]
                    i += 1
                else:
                    median += nums2[j]
                    j += 1
            elif i <= len(nums1)





    def findMedianSortedArraysV1(self, nums1, nums2):
        tmp = []
        i = 0
        j = 0
        while i <= len(nums1) - 1 and j <= len(nums2) - 1:
            if nums1[i] < nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1

        while i <= len(nums1) - 1:
            tmp.append(nums1[i])
            i += 1

        while j <= len(nums2) - 1:
            tmp.append(nums2[j])
            j += 1

        print(nums1)
        print(nums2)
        print(tmp)

        if (len(tmp) - 1) % 2 == 0:
            return tmp[(len(tmp) - 1) / 2]
        else:
            return (tmp[len(tmp)/2]*1.0 + tmp[len(tmp)/2-1])/2
       
 

if __name__ == '__main__':
    mySolution = Solution()
    print(mySolution.findMedianSortedArraysV1([1, 3], [2]))
    print("="*10)
    print(mySolution.findMedianSortedArraysV1([3], [-2, -1]))
    print("="*10)
    print(mySolution.findMedianSortedArraysV1([1, 2], [3, 4]))
