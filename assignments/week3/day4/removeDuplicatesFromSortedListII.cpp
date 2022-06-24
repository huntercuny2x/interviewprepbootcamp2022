class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* dummy = new ListNode(0, head);
        ListNode* prev = dummy;
        
        while(head) {
            //check if we have two consecutive nodes with the same value
            //this is the start of a sublist
            if(head->next && head->val==head->next->val) {
                //find end of the duplicates sublist
                while(head->next && head->val==head->next->val) {
                    head = head->next;
                }
                //point prev to the next non-duplicate value (head->next)
                prev->next = head->next;
            } else {
                //move prev forward
                prev = prev->next;
            }
            //move head forward
            head = head->next;     
        }
        
        return dummy->next;
    }
};
