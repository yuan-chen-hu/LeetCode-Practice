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
    ListNode* now;
    ListNode* old;
    ListNode* reverseList(ListNode* head) {

        while(head!=NULL){
            now=head;
            //cout<<"now"<<now->val<<endl;
            head=head->next;
            now->next=old;
            old=now;
            //cout<<"old"<<old->val<<endl;            
        }
        return old;
    }
};