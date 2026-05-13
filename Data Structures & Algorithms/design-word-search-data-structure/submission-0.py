class Node:
    def __init__(self, val):
        self.val = val
        self.connected = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.head = Node(None)

    def addWord(self, word: str) -> None:
        curr = self.head
        for i in word:
            if i in curr.connected:
                curr = curr.connected[i]
            else:
                curr.connected[i] = Node(i)
                curr = curr.connected[i]
        curr.is_word = True

    def search(self, word: str) -> bool:
        
        def dfs (index, node):
            for i in range(index, len(word)):
                c = word[i]
                if c == ".":
                    for child in node.connected.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    if c not in node.connected:
                        return False
                    node = node.connected[c]
            return node.is_word

        return dfs(0, self.head)
        

        
        