class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::vector<int> v;
        for(int i = 0; i < nums.size(); i++)
        {
            for(int j = 0; j < nums.size();j++)
            {
                if(i != j && nums[i] + nums[j] == target)
                {
                    v.push_back(i);
                    v.push_back(j);
                    std::sort(v.begin(), v.end());
                    return v;
                }
            }
        }
    }
};
