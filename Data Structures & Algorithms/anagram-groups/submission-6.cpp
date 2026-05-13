class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        /* create dict that stores a vector of a vector
         * then iterate through the strings, create a vector of char count
         * append this to some hashmap
         * iterate though hashmap, and append to a result vector
         */

        unordered_map<string, vector<string>> hmap;

        int n = strs.size();
        for (int i = 0; i < n; i++){
            string s = strs[i];
            vector<int> curr(26, 0);

            int m = s.size();
            for (int j = 0; j < m; j++){
                curr[int(s[j]) - int('a')]++;
            }

            string help = to_string(curr[0]);
            for (int k = 1; k < 26; ++k){
                help += ',' + to_string(curr[k]);
            }
            hmap[help].push_back(s);
        }

        vector<vector<string>> res;
        for (pair<string, vector<string>> s : hmap) {
            res.push_back(s.second);
        }

        return res;
    }
};
