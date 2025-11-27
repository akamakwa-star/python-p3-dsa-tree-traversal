class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    if self.root is None:
      return None

    def dfs(node):
      if node is None:
        return None
      if node.get('id') == id:
        return node
      for child in node.get('children', []):
        found = dfs(child)
        if found is not None:
          return found
      return None

    return dfs(self.root)
