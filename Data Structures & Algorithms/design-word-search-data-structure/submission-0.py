class WordDictionary:

    def __init__(self):
        self.children = {}
        self.flag = False

    def addWord(self, word: str) -> None:
        next_trie = self
        for ch in word:
            if ch not in next_trie.children:
                next_trie.children[ch] = WordDictionary()
            next_trie = next_trie.children[ch]
                
        next_trie.flag = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            next_trie = root
            for i in range(j, len(word)):
                if word[i] == ".":
                    for ch in next_trie.children:
                        if dfs(i + 1, next_trie.children[ch]):
                            return True

                    return False
                
                else:
                    if word[i] not in next_trie.children:
                        return False
                    next_trie = next_trie.children[word[i]]

            return next_trie.flag

        return dfs(0, self)
