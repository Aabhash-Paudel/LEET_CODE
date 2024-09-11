class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_loc={}
        for i in range(len(nums)):
            compl=target-nums[i]
            if compl in hash_loc:
                return [i,hash_loc[compl]]
            hash_loc[nums[i]]=i

        return []
