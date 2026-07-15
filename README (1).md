# CIA — Command-line Instant Autocomplete

A terminal-based autocomplete tool built on a trie (prefix tree) data structure, loaded with a real 100,000+ word English dictionary. Type a prefix, get instant matching suggestions — the same core idea behind phone keyboard and search-bar autocomplete.

![demo](demo.gif)

## How it works

The project is built around a **trie**: a tree where each node represents one character, and a path from the root spells out a prefix. Words that share a prefix share the same path, which makes prefix lookups fast without scanning the entire word list.

Each node stores:
- `children` — a hash map of `{character: next node}`
- `endOfWord` — a flag marking whether a complete word ends at this node

**Core operations:**
- `insert(word)` — walks the trie one letter at a time, creating new nodes as needed, and flags the final node as the end of a word
- `search(word)` — walks the same path and checks whether the final node is flagged as a complete word
- `startsWith(prefix)` — checks whether the path exists at all, regardless of whether it's a complete word
- `getWordsWithPrefix(prefix)` — walks to the end of the prefix, then uses depth-first recursion to collect every complete word reachable from that point

## Tech

- Python
- Real word list from `/usr/share/dict/words` (the `wamerican` package on Debian/Ubuntu), ~104,000 words
- Runs as a native Linux executable via a shebang line and `chmod +x`

## Running it

```bash
git clone <this-repo>
cd CIA
sudo apt-get install wamerican   # provides /usr/share/dict/words if not already installed
chmod +x CIA.py
./CIA.py
```

Type a prefix at the `>` prompt. Type `all` or a number when asked how many matches to display. Type `quit` to exit.

## What I learned

- Building a trie from scratch: nodes, hash maps, recursive traversal
- The difference between `search` (exact word) and `startsWith` (valid prefix path)
- Depth-first recursion to collect all words under a node
- Linux fundamentals: file permissions (`chmod`), shebang lines, running scripts as executables, package installation with `apt`
