class Node:
    def __init__(self,data=None):
        self.data=data
        self.link=None

class Linkedlist:
    def __init__(self):
        self.head=Node()


    def append(self,data):
        new_node=Node(data)
        cur=self.head
        while cur.link !=None:
            cur=cur.link
        cur.link=new_node


    def length(self):
        cur=self.head
        total=0
        while cur.link !=None:
            total +=1
            cur=cur.link
        print(total)


    def display(self):
        elem=[]
        cur=self.head
        while cur.link !=None:
            cur=cur.link
            elem.append(cur.data)
        print(elem)

new=Linkedlist()
new.append(22)
new.append(35)

new.display()
new.length()