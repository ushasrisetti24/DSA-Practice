class Node:
    def __init__(self,x):
        self.data= x
        self.next=None

class mystack:
    def __init__(self):
        self.top=None
        self.count=0

    def push(self,x):
        temp=Node(x)
        temp.next= self.top
        self.top= temp
        self.count+=1

    def pop(self):
        if self.pop is None:
            print("stack underflow")
            return -1

        temp=self.top
        self.top=self.top.next
        val=temp.data
        self.count-=1    
        return val

    def peek(self):
        if self.top is None:
            print("Stack is Empty")
            return -1
        return self.top.data

    def isEmpty(self):
        return self.top is None

    def size(self):
        return self.count


if __name__ == "__main__":
    st = mystack()

    # pushing elements
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)

    print("Popped:", st.pop())

    print("Top element:", st.peek())
    print("Is stack empty:", "Yes" if st.isEmpty() else "No")
    print("Current size:", st.size())