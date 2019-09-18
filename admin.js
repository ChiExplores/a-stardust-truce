const Node = (val, next) => {
  let node = {}
  node.val = val, node.next = next;
  return node;
}
const single-link-list-stack = _ => {
  let obj = {}
// list-head
  obj.head = null;
// list-push
  obj.push = node => {
    node = Node(node, obj.head);
    obj.head = node;
    if (obj.hasOwnProperty('size')) obj.size++;
  };
  return obj
}