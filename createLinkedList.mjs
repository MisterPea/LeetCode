export function ListNode(val, next) {
  this.val = (val === undefined ? 0 : val)
  this.next = (next === undefined ? null : next)
}

export function createLinkedList(linkedArray) {
  let head = null;
  let newHead = null;

  for(let link of linkedArray) {
    if(head === null) {
      head = new ListNode(link)
      newHead = head
    } else {
      newHead.next = new ListNode(link)
      newHead = newHead.next
    }
  }
  return head
}