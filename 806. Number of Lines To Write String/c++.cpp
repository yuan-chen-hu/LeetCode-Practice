class Solution {
public:
    vector<int> numberOfLines(vector<int>& widths, string s) {
        int i=0;
        int total=0;
        int count=1;
        while(i<size(s)){
            //cout<<"i"<<i<<endl;
            //cout<<widths[int(s[i])-97]<<endl;
            if (total+widths[int(s[i])-97]>100){
                total=0;
                count++;
            }
            total+=widths[int(s[i])-97];
            i++;
            
        }
        
        return {count,total};
        
    }
};