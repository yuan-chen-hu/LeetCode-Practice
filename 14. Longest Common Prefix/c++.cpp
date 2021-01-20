class Solution {
public
    string longestCommonPrefix(vectorstring& strs) {
        if (strs.size()=0){
            return ;
        }
  
        string first=strs[0];
        string ans=;
        for (int i=0;ifirst.size();i++){
            for (int j=1;jstrs.size();j++){
                coutstrs[j][i]  first[i]endl;
                if (i==strs[j].size()){
                    return ans;
                }
                if (strs[j][i]!=first[i]){
                    return ans;                    
                }
            }
            ans+=first[i];
        }
        return ans;
    }
};