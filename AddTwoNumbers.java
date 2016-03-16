/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    	ListNode head = new ListNode(0);
    	ListNode cur = head, p1 = l1, p2 = l2;
    	int carry = 0;

    	while (p1 != null || p2 != null || carry != 0) {
    		int sum = (p1 != null ? p1.val : 0) + (p2 != null ? p2.val : 0) + carry;
    		carry = sum / 10;
    		ListNode newNode = new ListNode(sum % 10);
    		head.next = newNode;
    		head = head.next;
    		p1 = (p1 != null ? p1.next : null);
    		p2 = (p2 != null ? p2.next : null);
    	}

    	return head.next;
    }
}