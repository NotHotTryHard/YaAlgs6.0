from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.head = None
        
    def addValue(self, val):
        if self.head == None: # случай пустого дерева
            self.head = TreeNode(val)
            print('DONE')
            return 
        
        currNode = self.head
        
        while currNode and currNode.val != val:
            if currNode.val < val:
                prevNode = currNode
                currNode = currNode.right
            else:
                prevNode = currNode
                currNode = currNode.left
                
        if currNode: # значение уже присутствует в дереве
            print('ALREADY')
            return 
        else:
            if prevNode.val < val:
                prevNode.right = TreeNode(val) # суём вправо
            else:
                prevNode.left = TreeNode(val) # суём влево
            print('DONE')
            return 


    def findValue(self, target):
        def recSearch(node, target):
            if not node:
                return False, []
            
            if node.val < target:
                res, path = recSearch(node.right, target)
                path.append(1)
                return res, path
            elif node.val > target:
                res, path = recSearch(node.left, target)
                path.append(-1)
                return res, path
            else:
                return True, [0]
        
        res, path = recSearch(self.head, target)
        path.reverse()
        if res:
            print('YES')
        else:
            print('NO')
        return res, path
    
    def printTree(self):
        def rec(node, depth):
            if not node:
                return
            rec(node.left, depth + 1)
            print('.' * depth + str(node.val))
            rec(node.right, depth + 1)
            return 
        rec(self.head, 0)
        return
            
with open("input.txt", "r") as file:
    queries = [list(line.split()) for line in file]

a = BinaryTree()
for com in queries:
    if com[0] == 'ADD':
        a.addValue(int(com[1]))
    elif com[0] == 'SEARCH':
        a.findValue(int(com[1]))
    elif com[0] == 'PRINTTREE':
        a.printTree()