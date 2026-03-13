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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *currentptr = new ListNode();
        ListNode *currentptrHead = currentptr;

        int overflow = 0;

        while(l1 != nullptr || l2 != nullptr){
            if(l1 != nullptr){
                currentptr->val += l1->val;
                l1 = l1->next;
            }

            if(l2 != nullptr){
                currentptr->val += l2->val;
                l2 = l2->next;
            }

            overflow = currentptr->val / 10;
            currentptr->val %= 10;

            if(l1 != nullptr || l2 != nullptr || overflow != 0){
                currentptr->next = new ListNode(overflow);
                currentptr = currentptr->next;
            }
        }

        return currentptrHead;
    }
};