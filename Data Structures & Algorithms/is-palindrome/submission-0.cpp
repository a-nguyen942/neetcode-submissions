class Solution {
public:
    bool isPalindrome(string s) {
        std::string tempS = s;
        tempS.erase(std::remove_if(tempS.begin(), tempS.end(),[](char c) { return !std::isalnum((unsigned char)c); }),
        tempS.end());
        for(int i = 0; i < tempS.size();i++)
        {
            tempS[i] = tolower(tempS[i]);
        }
        int iFront = 0;
        int iBack = tempS.size() - 1;
        while(iFront < iBack)
        {
            if((tempS[iFront] != tempS[iBack]))
            {
                return false;
            }
            iFront++;
            iBack--;
        }
        return true;
    }
};
