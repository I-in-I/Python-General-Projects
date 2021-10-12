class QueueError(IndexError):
    pass


class Queue():
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.insert(0, elem)

    def get(self):
        if len(self.__queue) > 0:
            elem = self.__queue[-1]
            del self.__queue[-1]
            return elem
        else:
            raise QueueError

    def get_queue_length(self):
        return len(self.__queue)


class SuperQueue(Queue):

    def isempty(self):
        if self.get_queue_length() == 0:
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
