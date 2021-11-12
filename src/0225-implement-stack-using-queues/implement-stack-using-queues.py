# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).
#
# Implement the MyStack class:
#
#
# 	void push(int x) Pushes element x to the top of the stack.
# 	int pop() Removes the element on the top of the stack and returns it.
# 	int top() Returns the element on the top of the stack.
# 	boolean empty() Returns true if the stack is empty, false otherwise.
#
#
# Notes:
#
#
# 	You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# 	Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
#
#
#  
# Example 1:
#
#
# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]
#
# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False
#
#
#  
# Constraints:
#
#
# 	1 <= x <= 9
# 	At most 100 calls will be made to push, pop, top, and empty.
# 	All the calls to pop and top are valid.
#
#
#  
# Follow-up: Can you implement the stack using only one queue?
#


from queue import Queue


class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
        self.t = None

    def push(self, x: int) -> None:
        self.q1.put(x)
        self.t = x

    def pop(self) -> int:
        self.t = None

        while self.q1.qsize() > 1:
            x = self.q1.get()
            self.q2.put(x)
            self.t = x
        
        res = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1
        return res

    def top(self) -> int:
        return self.t

    def empty(self) -> bool:
        return True if self.q1.empty() else False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

