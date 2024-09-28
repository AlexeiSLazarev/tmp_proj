class BoundedStack:
    DEFAULT_MAX_SIZE = 32
    POP_NIL = 0
    POP_OK = 1
    POP_ERR = 2
    PEEK_NIL = 0
    PEEK_OK = 1
    PEEK_ERR = 2
    PUSH_OK = 1
    PUSH_ERR = 2

    def __init__(self, max_size=None):
        self.max_size = max_size if max_size is not None else BoundedStack.DEFAULT_MAX_SIZE
        self.stack = []
        self.peek_status = BoundedStack.PEEK_NIL
        self.pop_status = BoundedStack.POP_NIL
        self.push_status = BoundedStack.PUSH_OK

    def push(self, value):
        self.push_status = BoundedStack.PUSH_OK if self.size() < self.max_size else BoundedStack.PUSH_ERR
        if self.push_status == BoundedStack.PUSH_OK:
            self.stack.append(value)

    def pop(self):
        self.pop_status = BoundedStack.POP_OK if self.size() > 0 else BoundedStack.POP_ERR
        if self.pop_status == BoundedStack.POP_OK:
            self.stack.pop()

    def clear(self):
        self.stack = []
        self.peek_status = BoundedStack.PEEK_NIL
        self.pop_status = BoundedStack.POP_NIL
        self.push_status = BoundedStack.PUSH_OK

    def peek(self):
        self.peek_status = BoundedStack.PEEK_OK if self.size() > 0 else BoundedStack.PEEK_ERR
        return self.stack[-1] if self.size() > 0 else None

    def size(self):
        return len(self.stack)

    def get_pop_status(self):
        return self.pop_status

    def get_peek_status(self):
        return self.peek_status

    def get_push_status(self):
        return self.push_status



