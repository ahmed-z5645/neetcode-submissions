class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // create a set
        // loop through the array, and then check if its in the set

        int n = nums.size();

        unordered_set<int> seen;
        for (int i = 0; i < n; i++) {
            if (seen.count(nums[i])) {
                return true;
            } 

            seen.insert(nums[i]);
        }

        return false;
    }
};
