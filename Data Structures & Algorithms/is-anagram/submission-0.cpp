class Solution {
public:
    bool isAnagram(string s, string t) {
        std::string tempS = s;
        std::sort(tempS.begin(), tempS.end());
        std::string tempT = t; 
        std::sort(tempT.begin(), tempT.end());
        if(tempS == tempT)
        {
            return true;
        }
        return false;
    }
};
