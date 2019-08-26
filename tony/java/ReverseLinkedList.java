/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null || head.next == null)
            return head;
        
        ListNode pre = head, p = head.next, tmp;
        pre.next = null;
        while (p != null) {
            tmp = p.next;
            p.next = pre;
            pre = p;
            p = tmp;
        }
        return pre;
    }
}