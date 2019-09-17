const Node = (val, next) => {
  let node = {}
  node.val = val, node.next = next;
  return node;
}
const single-link-list-stack _ => {
  let obj = {}
// list-head
  obj.head = null;
// list-size
  obj.size = 0;
// list-push
  obj.push = node => {
    node = Node(node, obj.head);
    obj.head = node;
    if (obj.hasOwnProperty('size')) obj.size++;
  };
// list-pop
  obj.pop = _ => {
    let pop = obj.head || null;
    obj.head = pop ? pop.next : null;
    if (obj.hasOwnProperty('size')) obj.size--;
    return pop ? pop.val : undefined;
  }
// list-peek
  obj.peek = _ => obj.head ? obj.head.val : undefined;
// list-isEmpty
  obj.isEmpty = _ => !obj.head
  return obj
}