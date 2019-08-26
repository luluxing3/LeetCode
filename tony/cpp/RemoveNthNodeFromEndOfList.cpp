/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *p1 = head, *p2 = head, *p3 = NULL;
        while (p1 != NULL) {
            p1 = p1->next;
            if (--n < 0) {
                p3 = p2;
                p2 = p2->next;
            }
        }
        if (p3 != NULL) {
            ListNode *tmp = p3->next;
            p3->next = p2->next;
            delete tmp;
        } else { 
            ListNode *tmp = head;
            head = p2->next;
            delete tmp;
        }
        
        return head;
    }
};