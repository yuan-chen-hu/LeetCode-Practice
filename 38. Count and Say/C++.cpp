class Solution {
public:
    //int first=1;
    string countAndSay(int n) {
        /*if (first==1){
            n=9;
            first=0;
        }*/
        cout<<"n"<<n<<endl;
    if (n==1){
        cout<< "n=1 return"<<endl;
        return "1";    
    }        
    else{
        //cout<<"here"<<endl;
        string temp=countAndSay(n-1);
        //cout<<"here2"<<endl;
        string output="";
        int count=1;
        char now=temp[0];
        //cout<< "now first"<<now<<endl;
        char old=temp[0];
        //cout<<"old first"<<old<<endl;
        //cout<<"len"<<temp.length()<<endl;
        for(int i=1;i<temp.length();i++){
            //cout<<"here3"<<endl;
            now=temp[i];
            //cout<<"count in for loop"<<count<<endl;
            //cout<<"now in for loop"<<now<<endl;
            //cout<<"old in for loop"<<old<<endl;
            if (now==old){
                count+=1;    
            }
            else{

                output=output+to_string(count);
                output=output+old;
                //cout<< "output in else"<<output<<endl;
                count=1;
                old=now;
            }
        }
        //cout<<"count last"<<count<<endl;
        //cout<<"old last "<<old<<endl;
        output=output+to_string(count);   
        output=output+old;
        cout<<output<<endl;

        //cout<<"output========"<<output<<endl;
        return output;
    }  
        
    }
};