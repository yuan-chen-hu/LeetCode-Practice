class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if(strs.size()==0){
            return "";
        }
        sort(begin(strs),end(strs));
        string start=strs[0];
        string end=strs[strs.size()-1];
        string ans; 
        for(int i=0;i<start.size();i++){
            if (i==end.size()){
                return ans;
            }
            if (start[i]==end[i]){
                ans+=start[i];
            }
            else{
                return ans;
            }           
        }
        return ans;        
    }
};