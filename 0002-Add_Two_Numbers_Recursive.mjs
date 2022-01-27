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

  function innerAdd(list1, list2, carry) {
    let tempAdd = 0

    if (list1) {
      tempAdd += list1.val
      list1 = list1.next
    } else {
      list1 = null
    }

    if (list2) {
      tempAdd += list2.val
      list2 = list2.next
    } else {
      list2 = null
    }

    tempAdd += carry
    if (tempAdd > 9) {
      tempAdd -= 10
      carry = 1
    } else {
      carry = 0
    }
    if (head === null) {
      head = { val: tempAdd, next: null }
      newHead = head
    } else {
      newHead.next = { val: tempAdd, next: null }
      newHead = newHead.next
    }
    
    if (list1 || list2) {
      return innerAdd(list1, list2, carry)
    } else {
      if (carry === 1) {
        newHead.next = { val: carry, next: null }
        newHead = newHead.next
      }
      return head
    }
  }
  return innerAdd(l1, l2, 0)
};

parseLinkedList(addTwoNumbers(one, two))

