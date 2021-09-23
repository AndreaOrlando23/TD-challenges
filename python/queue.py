
class Queue:

    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        else:
            self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]

    def isEmpty(self):
        return bool(len(self.queue) == 0)
    
    def size(self):
        return len(self.queue)



# Queue test
input_queue = Queue()

# The player wants to get the upper hand so pressing the right combination of buttons quickly
input_queue.enqueue('DOWN')
input_queue.enqueue('RIGHT')
input_queue.enqueue('B')

print(input_queue.peek())
print(input_queue.size())
print(input_queue.isEmpty())
