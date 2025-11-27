class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        def _get_element_by_id(node, id):
            if node is None:
                return None

            # dict-based node access
            if node.get("id") == id:
                return node

            for child in node.get("children", []):
                result = _get_element_by_id(child, id)
                if result is not None:
                    return result

            return None

        return _get_element_by_id(self.root, id)
