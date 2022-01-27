/*
 * You are given two non-empty linked lists representing two non-negative integers.
 * The digits are stored in reverse order, and each of their nodes contains a single digit.
 * Add the two numbers and return the sum as a linked list.
 * 
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 */

import parseLinkedList from "./parseLinkedList.mjs"
import { createLinkedList, ListNode } from "./createLinkedList.mjs";

const one = createLinkedList([2, 4, 3])
const two = createLinkedList([5, 6, 4])

/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
function addTwoNumbers(l1, l2) {
  let head = null;
  let newHead;
  let carry = 0;

  while (l1 || l2) {

    let tempAdd = 0

    if (l1) {
      tempAdd += l1.val
      l1 = l1.next
    }

    if (l2) {
      tempAdd += l2.val
      l2 = l2.next
    }

    tempAdd += carry
    if (tempAdd > 9) {
      tempAdd = tempAdd - 10
      carry = 1
    } else {
      carry = 0
    }
    if (head === null) {
      head = new ListNode(tempAdd)
      newHead = head
    } else {
      newHead.next = new ListNode(tempAdd)
      newHead = newHead.next
    }
  }
  if (carry !== 0) {
    newHead.next = new ListNode(carry)
  }
  return head
};

parseLinkedList(addTwoNumbers(one, two))

