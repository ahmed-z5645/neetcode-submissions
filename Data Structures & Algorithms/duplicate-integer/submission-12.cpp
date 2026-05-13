class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        // go thorugh the elements of the arry
        // and iterate through the rest of the elements
        // return false the element == the searching element 

        // O(n^2) 

        // init a set
        // iterate through the list,
        // check if element is in the the set; if so, return True
        // else add the element to the set
        // O(n)

        // return False

        // TC1: [1, 2, 3, 3]
        // TC2: [1, 2, 3, 4]
        // TC3: []
        // TC4: [1]
        
        int n = nums.size();

        if (n <= 1){
            return false;
        }
        unordered_set<int> numSet;

        for (int i = 0; i < n; i++) {
            if (numSet.count(nums[i]) != 0){
                return true;
            }
            numSet.insert(nums[i]);
        }

        return false;
    }
};
