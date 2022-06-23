def ll_iterator(node):
        while node != None:
            yield node
            node = l1[node]

def addTwoNumbers(l1,l2):
    res = []
    str_l1 = map(str,l1)
    str_l2 = map(str,l2)
    num1 = ''.join(str_l1)[::-1]
    num2 = ''.join(str_l2)[::-1]
    sum = str(int(num1) + int(num2))
    reverse_sum = sum[::-1]
    for i in range(len(reverse_sum)):
        res.append(reverse_sum[i])
    res = list(map(int,res))
    return res 


def addTwoNumbers(l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next
# l1 = [2,4,3]
# l2 = [5,6,4]
# l1 =[0]
# l2=[0]
l1 =[9,9,9,9,9,9,9]
l2 = [9,9,9,9]
print(addTwoNumbers(l1,l2))