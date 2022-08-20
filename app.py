#########################################################################################################################################
## Description: So we are given two linked lists and we have to calculate the sum of those two linked lists
## Input: l1 = [2,4,3], l2 = [5,6,4]
## Output: [7,0,8]
## Explanation: 342 + 465 = 807.
## Strategy: The strategy i had adopted is that we are converting the linked list to simple list and then that list is inverted and then 
             that list is converted into string which is then converted into integer and then those are summed.
             Again we convert those integers to string then those strings are used to create ListNodes
#########################################################################################################################################



# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_ll = []
        second_ll = []
        # COnverting linked list to list
        while l1!=None:
            first_ll.append(l1.val)
            l1 = l1.next
        while l2!=None:
            second_ll.append(l2.val)
            l2 = l2.next
        #Reversing the list
        first_ll = first_ll[::-1]
        second_ll = second_ll[::-1]
        
        #Converting list to string
        first_ll = [str(ll_val) for ll_val in first_ll]
        second_ll = [str(ll_val) for ll_val in second_ll]
        str_first_ll = "".join(first_ll)
        str_second_ll = "".join(second_ll)
        
        #Converting string to integer
        int_first_ll = int(str_first_ll)
        int_second_ll = int(str_second_ll)
        
        int_sum = int_first_ll + int_second_ll
        
        #Converting integer back to string
        str_sum = str(int_sum)
        
        int_sum_list = [int(element) for element in str_sum]
        int_sum_list = int_sum_list[::-1]
        
        #Making listnodes. Note we are making listnodes and then making their .next listnode. We are not making linked list here. Instead making listnodes individually.
        i = 0
        int_sum_ll = ListNode(int_sum_list[i])
        cur = int_sum_ll
        j=1
        while j<len(int_sum_list):
            cur.next = ListNode(int_sum_list[j])
            cur = cur.next
            j+=1
        
        
        return int_sum_ll
    
