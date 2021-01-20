/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    int getDecimalValue(ListNode* head) {
        int ans=0;
        while(head){
            //cout<<ans<<endl;
            ans*=2;
            ans+=head->val*2;
            head=head->next;            
        }        
        return ans/2;        
    }
};