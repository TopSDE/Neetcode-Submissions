class PrefixTree:

    def __init__(self):
        self.children = {}
        self.flag = False

    def insert(self, word: str) -> None:
        next_trie = self
        for ch in word:
            if next_trie.children.get(ch, 0) == 0:
                next_trie.children[ch] = PrefixTree()
            next_trie = next_trie.children[ch]
                
        next_trie.flag = True

    def search(self, word: str) -> bool:
        next_trie = self
        for ch in word:
            if next_trie.children.get(ch, 0) != 0:
                next_trie = next_trie.children[ch]
            else:
                return False
        
        if next_trie.flag:
            return True

        return False

    def startsWith(self, prefix: str) -> bool:
        next_trie = self
        for ch in prefix:
            if next_trie.children.get(ch, 0) != 0:
                next_trie = next_trie.children[ch]
            else:
                return False
        
        return True


        
        