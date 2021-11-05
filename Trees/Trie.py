from array import array
from StackLinkedList import Stack

class TrieNode:
    def __init__(self, array_map = False, alphabet_size = 26):
        self.array_map = array_map
        self.alphabet_size = alphabet_size
        self.word_end = False
        self.map = [None] * alphabet_size if array_map else {}
        self.size = 0

    def __len__(self):
        return self.size + self.word_end

    def __get_node(self, char):
        if self.array_map:
            index = ord(char) - ord('a')
            return self.map[index]
        else:
            if not char in self.map:
                return None
            return self.map[char]

    def __add_node(self, char):
        node = TrieNode(self.array_map, self.alphabet_size)
        if self.array_map:
            index = ord(char) - ord('a')
            if self.map[index]:
                return
            self.size += 1
            self.map[index] = node
        else:
            if char in self.map:
                return
            self.size += 1
            self.map[char] = node
        return node

    def __remove_node(self, char):
        if self.array_map:
            index = ord(char) - ord('a')
            if self.map[index]:
                self.size -= 1
            self.map[index] = None
        else:
            if char in self.map:
                self.size -= 1
            del self.map[char]
            
    def __set_word_end(self, value = True):
        self.word_end = value

    def insert(self, text):
        text = text.lower()
        node = self
        for c in text:
            next_node = node.__get_node(c)
            if next_node is None:
                next_node = node.__add_node(c)
            node = next_node
        node.__set_word_end()

    def search(self, text):
        text = text.lower()
        node = self
        for c in text:
            next_node = node.__get_node(c)
            if next_node is None:
                return False
            node = next_node
        return node.word_end

    def delete(self, text):
        word_nodes = Stack()
        node = self
        for c in text:
            next_node = node.__get_node(c)
            if next_node is None:
                return
            word_nodes.push(node)
            node = next_node
        
        if not node.word_end:
            return

        node.__set_word_end(False)
        end_node_len = len(node)
        if end_node_len > 0:
            return
        
        node = word_nodes.pop()
        for i in range(len(text)):
            c = text[-i-1]
            node.__remove_node(c)
            node_len = len(node)
            if node_len > 0:
                break
            node = word_nodes.pop()

if __name__ == '__main__':
    trie = TrieNode()
    trie.insert("api")
    trie.insert("apple")
    print("All True: ")
    print(trie.search("api"))
    print(trie.search("apple"))
    trie.delete("api")
    print("Only first one False: ")
    print(trie.search("api"))
    print(trie.search("apple"))
    trie.insert("api")
    trie.insert("apis")
    print("All True: ")
    print(trie.search("api"))
    print(trie.search("apis"))
    print(trie.search("apple"))
    trie.delete("api")
    print("Only first one False: ")
    print(trie.search("api"))
    print(trie.search("apis"))
    print(trie.search("apple"))
    trie.insert("ap")
    print("All True: ")
    print(trie.search("ap"))
    print(trie.search("apis"))
    print(trie.search("apple"))
    trie.delete("apis")
    print("Only first one False: ")
    print(trie.search("apis"))
    print(trie.search("ap"))
    print(trie.search("apple"))

