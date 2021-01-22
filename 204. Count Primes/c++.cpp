class Solution:
    def countPrimes(self, n: int) -> int:
        prime_list=[]            
        for i in range(2,n):
            #print("i=",i)
            #print(prime_list)
            if prime_list==[]:
                prime_list.append(i)
                continue
            else:    
                for j in prime_list:                                
                    if i%j==0:
                        break
                    if j>i**0.5:
                        prime_list.append(i)
                        break

        #print(prime_list)
        return len(prime_list)