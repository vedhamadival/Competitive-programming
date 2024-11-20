class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def addLists(first,second):
    dummy = Node(-1)
    carry = 0
    tail = dummy
    
    while first or second or carry:
        f = first.data if first else 0
        s = second.data if second else 0
        
        total = f + s + carry
        carry = total // 10
        new_digit = total % 10
        
        tail.next = Node(new_digit)
        tail = tail.next
        
        if first:
            first = first.next
        if second:
            second = second.next
    
    return dummy.next

if __name__ == "__main__":
    N = int(input())
    arr1 = list(map(int,input().split()))[:N]
    LL1 = Node(arr1[0])
    for i in range(1,N):
        new_node = Node(arr1[i])
        new_node.next = LL1
        LL1 = new_node
    
    M = int(input())
    arr2 = list(map(int,input().split()))[:M]
    LL2 = Node(arr2[0])
    for i in range(1,M):
        new_node = Node(arr2[i])
        new_node.next = LL2
        LL2 = new_node
    
    res = addLists(LL1 , LL2)
    
    output = []
    while res:
        output.append(str(res.data))
        res = res.next
    output.reverse()
    print(" ".join(output))
        