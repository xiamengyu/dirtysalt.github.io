package remove_nth

type ListNode struct {
	Val int
	Next* ListNode
}
 
func removeNthFromEnd(head *ListNode, n int) *ListNode {
	var pp *ListNode = head
	var p *ListNode = head
	for i:=0;i<n && p != nil;i++ {
		p = p.Next
        
	}
    if p == nil {
        return pp.Next
    }
    
	for ;p.Next != nil; {
		pp = pp.Next
		p = p.Next
	}
	pp.Next = pp.Next.Next
	return head
}