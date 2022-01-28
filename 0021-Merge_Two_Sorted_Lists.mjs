import { createLinkedList, ListNode } from './createLinkedList.mjs';
import parseLinkedList from './parseLinkedList.mjs';

const linkedList1 = createLinkedList([1, 12, 16, 17]);
const linkedList2 = createLinkedList([1, 13, 14]);

function mergeTwoLists(list1, list2) {
  const head = new ListNode();
  let newHead = head;

  // If both are something
  while (list1 && list2) {
    if (list1.val < list2.val) {
      newHead.next = list1;
      list1 = list1.next;
    } else {
      newHead.next = list2;
      list2 = list2.next;
    }
    newHead = newHead.next;

    // If either are
    if (list1) {
      newHead.next = list1;
    } else if (list2) {
      newHead.next = list2;
    }
  }
  return head.next;
}

parseLinkedList(mergeTwoLists(linkedList1, linkedList2));
