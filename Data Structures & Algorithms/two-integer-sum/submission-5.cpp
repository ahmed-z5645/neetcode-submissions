class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hmap;

        int n = nums.size();

        for(int i = 0; i < n; i++){
            if (hmap.count(nums[i])) {
                vector<int> ans;
                ans.push_back(hmap[nums[i]]);
                ans.push_back(i);
                return ans;
            }

            hmap[target - nums[i]] = i;
        }
    }
};
