
# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler = None):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode(handler)

    def insert(self, path_lst, handler = None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        curr = self.root
        for p in path_lst:
            curr.insert(p)
            curr = curr.children[p]
        curr.handler = handler

    def find(self, path_lst):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        curr = self.root
        for p in path_lst:
            if p not in curr.children.keys():
                return None
            curr = curr.children[p]
        return curr.handler


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, handler = None):
        # Initialize the node with children as before, plus a handler
        self.children = {}
        self.handler = handler

    def insert(self, path):
        # Insert the node as before
        if path not in self.children:
            self.children[path] = RouteTrieNode()