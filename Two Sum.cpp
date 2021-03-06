/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
*/

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> r;
        unordered_map<int, int> h;
        for(size_t i=0;i<nums.size();i++)
        {
            int n = target-nums[i];
            if(h.find(n) != h.end())
            {
                r.push_back(h[n]);
                r.push_back(i);
                return r;
            }
            h[nums[i]] = i;
        }
        return r;
    }
};

/*
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target-num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]
*/