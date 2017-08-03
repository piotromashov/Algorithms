#https://www.hackerrank.com/challenges/ctci-contacts

class Trie:
    def __init__(self):
        self.root = Node('')
        
    def add(self, word):
        self.root.add(word)
        
    def find(self, word):
        return self.root.find(word)

class Node:
    def __init__(self, char):
        self.data = char
        self.childrens = {}
        self.amount = 0
            
    def add(self, word):
        self.amount += 1
        if len(word) == 0:
            return
        char = word[0]
        if char not in self.childrens:
            self.childrens[char] = Node(char)
        self.childrens[char].add(word[1:])            
            
    def find(self, word):
        if not len(word):
            return self.amount
        elif word[0] not in self.childrens:
            return 0
        else:
            return self.childrens[word[0]].find(word[1:])  
        
n = int(input().strip())
trie = Trie()
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == "add":
        trie.add(contact)
    if op == "find":
        print(trie.find(contact))


# class Contacts(object):
    
#     def __init__(self):
#         self._prefixes = {}

#     def add(self, name):            
#         for l in range(1, len(name)+1):
#             try:
#                 self._prefixes[name[:l]] += 1
#             except KeyError:
#                 self._prefixes[name[:l]] = 1
            
    
#     def find(self, partial):
#         try:
#             print(self._prefixes[partial])
#         except KeyError:
#             print(0)
                

# ct = Contacts()
        
# n = int(input().strip())
# for a0 in range(n):
#     op, contact = input().strip().split(' ')

#     getattr(ct, op)(contact)
