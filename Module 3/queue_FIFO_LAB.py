# construct FIFO class (first in first out) and error QueueError if get is used on an empty queue

class QueueError(IndexError):  # Choose base class for the new exception.
    def __init__(self):
        pass


class Queue:
    def __init__(self):
        self.queue_list = []


    def put(self, elem):
        self.queue_list.insert(0, elem)

    def get(self):
        try:
            val = self.queue_list[-1]
            del self.queue_list[-1]
            return val
        except:
            raise QueueError

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self): # should return True if the queue is empty
        if len(self.queue_list) == 0:
            return True
        else:
            return False


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")