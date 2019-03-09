class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # get a reference to right and left nodes
    left = self.left
    right = self.right
    #return cb with a value
    cb(self.value) 

    # if left exists, recur until we hit the bottom
    if left is not None:
      left.depth_first_for_each(cb)
    # if right exists, recur until we hit the bottom
    if right is not None:
      right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb):
    # get reference to left and right
    left = self.left
    right = self.right
    # return cb with a value
    cb(self.value)

    if left is not None:
      cb(left.value)

    if right is not None:
      cb(right.value)

    if left and left.left is not None:
      left.left.breadth_first_for_each(cb)
    if left and left.right is not None:
      left.right.breadth_first_for_each(cb)
    if right and right.left is not None:
      right.left.breadth_first_for_each(cb)
    if right and right.right is not None:
      right.right.breadth_first_for_each(cb)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if target < self.value:
      if not self.left:
        return False
      else:
        return self.left.contains(target)
    else:
      if not self.right:
        return False
      else:
        return self.right.contains(target)

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
