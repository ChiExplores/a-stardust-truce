const Node = (val, next) => {
  let node = {}
  node.val = val, node.next = next;
  return node;
}
const Testing Structure 2 _ => {
  let obj = {}
// list-size
  obj.size = 0;
// list-pop
  obj.pop = _ => {
    let pop = obj.head || null;
    obj.head = pop ? pop.next : null;
    if (obj.hasOwnProperty('size')) obj.size--;
    return pop ? pop.val : undefined;
  }
// list-peek
  obj.peek = _ => obj.head ? obj.head.val : undefined;
  return obj
}