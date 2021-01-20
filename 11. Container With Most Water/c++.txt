class Solution {
public:
    int maxArea(vector<int>& height) {
        cout<<height.size()<<endl;
        int ans=0;
        int left_flag;
        int right_flag;
        int left_height=0;
        int right_height=0;
        for(int i=0;i<height.size();i++){
            if (height[i]<left_height){
                continue;
            }            
            for (int j=height.size()-1;j>i;j--){
                if (height[j]<right_height){
                continue;
                }
                if ((j-i)*height[i]<ans){
                    break;
                }
                int temp=(j-i)*min(height[i],height[j]);
                if (temp>ans){
                    ans=temp;
                    left_height=height[i];
                    right_height=height[j];
                }                
            }
        }   
        return ans;    
        
    }
};