class Solution {
public:
    int reverse(int x) {
        long int ans=0;
        cout<<x<<endl;
        while(x!=0){ 
            ans*=10;  
            ans+=x%10;
            x/=10;                      
            cout<<x<<endl;
            cout<<ans<<endl<<endl;            
        }
        if (ans>2147483647 || ans<-2147483647){
            return 0;
        }
        return ans;        
    }
};