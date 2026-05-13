class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> numSet;
        int n = nums.size();
        for (int i = 0; i < n; i++){
            if (numSet.count(nums[i]) == 0){
                numSet.insert(nums[i]);
            } else {
                return true;
            }
        }

        return false;
    }
};
