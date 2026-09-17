class mystack:
    def __init__(self):
        self.arr=[]

    def push(self,x):
        self.arr.append(x)

    def pop(self):
        if not self.arr:
            print("Stack Underflow")
            return -1
        return self.arr.pop()       

    def peek(self):
        if not self.arr:
            print("Stack is empty")
            return -1
        return self.arr[-1]

    def isEmpty(self):
        return len(self.arr)==0

    def size(self):
        return len(self.arr)


if __name__ == "__main__":
    st = mystack()

    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)

    print("Popped:", st.pop())
    print("Top element:", st.peek())
    print("Is stack empty:", "Yes" if st.isEmpty() else "No")
    print("Current size:", st.size())     