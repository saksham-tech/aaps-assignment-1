class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA, headB):
    lenA, lenB = 0, 0
    tempA, tempB = headA, headB
    while tempA:
        lenA += 1
        tempA = tempA.next
    while tempB:
        lenB += 1
        tempB = tempB.next
    
    tempA, tempB = headA, headB
    if lenA > lenB:
        for _ in range(lenA - lenB):
            tempA = tempA.next
    elif lenB > lenA:
        for _ in range(lenB - lenA):
            tempB = tempB.next
    
    while tempA and tempB:
        if tempA == tempB:
            return tempA
        tempA = tempA.next
        tempB = tempB.next
    return None
