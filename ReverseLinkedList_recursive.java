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
        
        ListNode p = head.next;
        ListNode q = reverseList(head.next);
        head.next = null;
        p.next = head;
        return q;
    }
}