class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, new_item):     # "en"queue means "insert"
        self.queue.append(new_item) 

    def dequeue(self):                # "de"queue means "delete"
        self.queue.pop(0)

    def peak(self):
        return self.queue[0]

q1 = Queue()
q1.enqueue(6) 
q1.enqueue(50)
q1.enqueue(24)
q1.enqueue(65)
print(q1.peak())
q1.dequeue()
q1.dequeue()
print(q1.peak())