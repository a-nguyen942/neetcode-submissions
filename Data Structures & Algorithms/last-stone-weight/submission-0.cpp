
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        std::vector<int> v = stones;
        std::make_heap(v.begin(), v.end());
        while(v.size() > 1)
        {
            std::pop_heap(v.begin(), v.end());
            int fL = v.back();
            v.pop_back();
            
            std::pop_heap(v.begin(), v.end());
            int sL = v.back();
            v.pop_back();
            
            int result = fL - sL;
            if(result > 0)
            {
                v.push_back(result);
                std::push_heap(v.begin(), v.end());
            }
        }

         if(v.empty())
        {
            return 0;
        }
        else
        {
            return v[0];
        }
    }
    
   
};
