/**
 * Method to output the entirety of a linked list
 * @param {function} head The head of the linked list
 * @output The output is a console.log of the linked list with elements separated by an arrow.
 */
export default function parseLinkedList(head) {
  const linkedListArray = []
  while (head) {
    if (head.next) {
      linkedListArray.push(`${head.val} ➔ `)
    } else {
      linkedListArray.push(head.val)
    }
    head = head.next
  }
  console.log(linkedListArray.join(''))
}