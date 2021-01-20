class Solution {
public:
    int maxArea(vector<int>& height) {
        int right=height.size()-1;
        int left=0;
        int area=0;
        int ans=0;
        while(left!=right){
            if (height[left]>height[right]){
                //cout<<"right"<<right<<endl ;
                area=height[right]*(right-left);
                right--;
            }
            else{
                //cout<<"left"<<left<<endl ;
                area=height[left]*(right-left);
                left++;
            }
            ans=max(ans,area);
        }
        return ans;   
    }
};