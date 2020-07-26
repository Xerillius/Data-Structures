class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.length = 0

  def add_to_head(self, value):
    new_node = Node(self, self.head)
    self.head = new_node
    if self.length == 0:
      self.tail = new_node
    self.length += 1
    
  def add_to_tail(self, value):
    new_node = Node(value)
    if self.length == 0:
      self.head = new_node
    else:
      self.tail.set_next(new_node)
    self.tail = new_node
    self.length += 1

  def remove_head(self):
    if self.head is None:
      return None
    elif self.head == self.tail:
      value = self.head.get_value()
      self.head = None
      self.tail = None
      self.length -= 1
      return value
    else:
      value = self.head.get_value()
      self.head = self.head.get_next()
      self.length -= 1
      return value

  def remove_tail(self):
    pass

  def contains(self, value):
    cur_node = self.head
    while cur_node is not None:
      if cur_node.get_value() == value:
        return True
      cur_node = cur_node.get_next()
    return False

  def get_max(self):
    if self.head is not None:
      cur_node = self.head
      cur_max = self.head.get_value()
      while cur_node is not None:
        if cur_node.get_value() > cur_max:
          cur_max = cur_node.get_value()
        cur_node = cur_node.get_next()
      return cur_max
    else:
      return None

  def find_middle(self):
    # Doing this in 1 pass, without using `length` attribute
    mid_point = self.head
    end_point = self.head
    index = 0
    while end_point is not None or end_point.get_next() is not None:
      index += 1
      mid_point = mid_point.get_next()
      end_point = end_point.get_next().get_next()
    return index

sll = LinkedList()
sll.add_to_tail(1)
sll.add_to_tail(1)
sll.add_to_tail(1)
sll.add_to_tail(1)
sll.add_to_tail(1)
sll.add_to_tail(1)
sll.add_to_tail(1)
sll.add_to_tail(1)
sll.add_to_tail(1)
sll.add_to_tail(1)
sll.add_to_tail(1)
print(sll.find_middle(), sll.length)