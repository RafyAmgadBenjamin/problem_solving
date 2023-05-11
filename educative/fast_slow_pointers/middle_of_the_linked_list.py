def get_middle_node(head):
    # Write your code here
    tmp1 = head 
    tmp2 = head 
    while tmp2 and tmp2.next:
        tmp1 = tmp1.next 
        tmp2 = tmp2.next.next
        
        
    # your code will replace this placeholder return statement
    return tmp1