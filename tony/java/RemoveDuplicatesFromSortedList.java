/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode cur = head;
        ListNode pre = cur;
        
        while (cur != null) {
            while (cur.next != null && cur.next.val == pre.val)
                cur = cur.next;
            if (cur.next == null) {
                pre.next = null;
                break;
            } else if (cur.next.val != pre.val) {
                ListNode temp = cur.next;
                cur.next = null;
                pre.next = temp;
                
                cur = temp;
                pre = cur;
            }
        }
        
        return head;
    }
}