"""
B-Tree is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. 
The B-tree is a generalization of a binary search tree in that a node can have more than two children. 
Unlike self-balancing binary search trees, the B-tree is optimized for systems that read and write large blocks of data. 
It is commonly used in databases and file systems.
"""

#2차 B-Tree를 구현합니다.

#2차 트리는 해당 노드에 최대 2개의 데이터를 지닐수 있습니다.


class Node:
    def __init__(self, data=None):
        self.data = data  # 노드의 데이터 (값)
        self.front = None  # 이전 노드를 가리키는 포인터 (기본값: None)
        self.back = None  # 다음 노드를 가리키는 포인터 (기본값: None)
        self.index = 1 #중복값 관리를 위한 print 문

class LinkedList:
    def __init__(self,M=1):
        self.head = None
        self.M = M

    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return

        last = self.head
        while last.front==None and last.back==None:
            if last.data>data:
                last = last.front
            elif last.data<data:
                last = last.back
            else:
                last.index += 1
                return
        
        if last.data>data:
            last.front = new_node
        elif last.data<data:
            last.back = new_node
        else:
            last.index += 1
