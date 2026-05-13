class Solution {
public:
    bool isValid(string s) {
        vector<char> st;
        map<char, char> key;
        key['}'] = '{';
        key[')'] = '(';
        key[']'] = '[';

        int n = s.size();
        if (n % 2 == 1){
            return false;
        }

        for (char c: s){
            if (c == '(' || c == '{' || c == '[') {
                st.push_back(c);
            } else {
                if ( (!st.empty()) && st[(st.size() - 1)] == (key[c]) ) {
                    st.pop_back();
                } else {
                    return false;
                }
            }
        }

        if (st.size() == 0) {
            return true;
        }
        return false;
    }
};
