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
    bool isPalindrome(ListNode* head) {
        vector<int> listValues;

        while(head != nullptr){
            listValues.push_back(head->val);
            if(head->next == nullptr){
                break;
            }

            head = head->next;
        }

        for(int i = 0, j = (listValues.size() - 1); i < listValues.size()/2; i++, j--){
            if(listValues[i] == listValues[j]){
                continue;
            }else{
                return false;
            }
        }

        return true;
  