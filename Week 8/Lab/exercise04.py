def enqueue(queue, customer):
    queue.append(customer)

def dequeue(queue):
    if is_empty(queue):
        raise IndexError("can't dequeue from an empty queue")
    return queue.pop(0)

def peek(queue):
    if is_empty(queue):
        raise IndexError("can't peek at an empty queue")
    return queue[0]

def is_empty(queue):
    return len(queue) == 0

def size(queue):
    return len(queue)


# create an empty checkout queue
checkout_queue = []

# add customers in order
for customer in ["Alice", "Bob", "Charlie", "Diana"]:
    enqueue(checkout_queue, customer)

print("Next customer:", peek(checkout_queue))

# serve customers one at a time
while not is_empty(checkout_queue): # repeat this until the queue is empty
    customer = dequeue(checkout_queue)
    print("Serving:", customer)

print("The queue is empty.") # only runs once the queue is empty/customer_queue is not empty
