class Solution {
public:
    bool isAnagram(string s, string t){

        int sS = s.size();
        int tS = t.size();
        
        if (sS != tS){
            return false;
        }

        map<char, int> word1;
        map<char, int> word2;

        for (int i = 0; i < sS; i++){
            if(word1.count(s[i])){
                word1[s[i]]++;
            } else {
                word1[s[i]] = 1;
            }

            if(word2.count(t[i])){
                word2[t[i]]++;
            } else {
                word2[t[i]] = 1;
            }
        }

        return (word1 == word2);
    };
};
