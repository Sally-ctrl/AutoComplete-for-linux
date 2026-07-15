#!/usr/bin/env python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word):
        cur = self.root

        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.endOfWord

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True

    def getWordsWithPrefix(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return []
            cur = cur.children[c]

        results = []
        self.dfs(cur, prefix, results)
        return results

    def dfs(self, node, current_word, results):
        if node.endOfWord:
            results.append(current_word)

        for letter, child_node in node.children.items():
            self.dfs(child_node, current_word + letter, results)


t = Trie()

with open("/usr/share/dict/words") as f:
    for line in f:
        word = line.strip()
        if word:
            t.insert(word)

print("Dictionary loaded.")
print("Autocomplete demo. Type a prefix (or 'quit' to exit).")
while True:
    user_input = input("> ").strip()
    if user_input.lower() == "quit":
        break
    matches = t.getWordsWithPrefix(user_input)

    if matches:
        print(f"  {len(matches)} matches found.")
        n = input("  How many do you want to see? (or 'all'): ").strip()
        if n.lower() == "all":
            shown = matches
        else:
            shown = matches[:int(n)]
        print("  ", ", ".join(shown))
    else:
        print("  No matches.")