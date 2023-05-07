def detect_cycle(head):
   tmp1 = head
   tmp2 = head 

   while tmp2.next != None:
      tmp1 = tmp1.next
      tmp2 = tmp2.next.next
      if tmp1 == tmp2: 
         return True

   return False