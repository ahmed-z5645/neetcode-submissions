class Solution {
public:
    bool isAnagram(string s, string t) {
        int sSize = s.size();
        int tSize = t.size();

        if (sSize != tSize){
            return false;
        }

        unordered_map<char, int> sCount;
        unordered_map<char, int> tCount;
        for (int i = 0; i < sSize; i++){
            sCount[s[i]] += 1;
            tCount[t[i]] += 1;
        }

        return sCount == tCount;
    }
};
