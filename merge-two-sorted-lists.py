class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        
        l1_next = l1.next
        for v1 in l1:
            l1_list.append(v1.x)

        l2_list = []
        for v2 in l2:
            l2_list.append(v2.x)

        new_list = l1_list+l2_list
        new_list.sort()
        new_link_list = []
        for i in range(len(new_list)):
            tmp_node = ListNode(new_list[i])
            tmp_node.val = new_list[i]
            if(i < len(new_list)-1):
                tmp_node.next = new_list[i+1]
            else:
                tmp_node.next = None
            new_link_list.append(tmp_node)
        return new_link_list


solution = Solution()
result = solution.mergeTwoLists([1,2,4], [1,3,4])
print(result)