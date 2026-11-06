from bisect import bisect_left
class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        ans=0

        for el in arr1:
            index=bisect_left(arr2,el-d)
            # low=0
            # high=len(arr2)

            # while low<high:
            #     mid=(low+high)//2
            #     if arr2[mid]<el-d:
            #         low=mid+1
            #     else:
            #         high=mid
            if index==len(arr2) or arr2[index]>el+d:
                ans+=1
        return ans