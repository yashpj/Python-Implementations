def shuffle_playlist(playlist):
    # Handle empty list or single node
    if not playlist or not playlist.next:
        return playlist
    
    slow = playlist
    fast = playlist
    prev = None
    
    # Step 1: Split the list in half
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    
    # Disconnect the two halves
    if prev:
        prev.next = None
    
    # Step 2: Reverse the second half (slow)
    p2 = slow
    prev_rev = None
    curr = p2
    while curr:
        temp = curr.next
        curr.next = prev_rev
        prev_rev = curr
        curr = temp
    
    # Step 3: Merge the two halves
    p1 = playlist
    p2 = prev_rev
    head = p1 # Store the head to return it later
    
    while p1:
        temp1 = p1.next
        temp2 = p2.next
        
        p1.next = p2
        if temp1: # Only point p2 back to p1's next if it exists
            p2.next = temp1
            
        p1 = temp1
        p2 = temp2
        
    return head