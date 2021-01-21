class Solution:
    def climbStairs(self, n: int) -> int:        
        final_ans=0
        total=int(n/2)
        #print(total)
        thetwo=total
        if int(n/2)*2<n:
            total+=1
        for count in range(thetwo+1): 
            #print("count",count)
            sum_one=1
            sum_two=1
            sum_three=1
            for i in range(1,total+count+1):
                sum_one*=i
                #print("sum_one",sum_one)
            for i in range(1,thetwo-count+1):
                sum_two*=i
                #print("sum_two",sum_two)
            for i in range(1,total+count*2-thetwo+1):
                sum_three*=i  
                #print("sum_three",sum_three)
            #ans=sum_one/(sum_two*sum_three) 
            #print("ans",ans)
            final_ans+=sum_one/(sum_two*sum_three) 
        return int(final_ans)   