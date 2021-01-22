# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head==None:
            return True
        if head.next==None:
            return True
        store=[]
        while (head!=None):
            store.append(head.val)
            head=head.next
        flag=False
        print(store)
        for i in range(len(store)):
            print(i)
            if store[i]==store[len(store)-1-i]:
                print("first if")
                flag=True
            else:
                print("else")
                flag=False    
                break
            if i>len(store)/2:
                print("second if")
                break

        return flag 
                
                
    """
    def isPalindrome(self, head: ListNode) -> bool:
        print(head)
        if head==None:
            return True
        if head.next==None:
            return True
        previous=None
        count=0
        while(head!=None):
            count+=1
            print(count)
            first_half=head        
            print(first_half)
            second_half=head.next
            print(second_half)
            first_half.next=previous
            print(first_half)
            previous=first_half
            print(previous)
            test1=previous
            test2=second_half
            flag=False
            first_in_while=True

            while(test2!=None):
                
                print("in while")
                print(test1.val)
                print(test2.val)
                if test1.val==test2.val:
                    print("in while if")
                    test1=test1.next
                    test2=test2.next
                    flag=True  
                elif first_in_while:
                    print("in while elif")
                    first_in_while=False
                    test2=test2.next
                else:
                    print("in while else")
                    flag=False
                    break
            if flag==True:
                return flag

            print(head)
            head=head.next

        return False
    """        

        
        