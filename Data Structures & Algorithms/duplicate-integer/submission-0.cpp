class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::vector<int> noDup;
        for(int i = 0; i < nums.size(); i++)
        {   
            for(int j = 0; j < noDup.size(); j++)
            {
                if(noDup[j] == nums[i])
                {
                    return true;
                }
            }
            noDup.push_back(nums[i]);
        }

        return false;
    }
};