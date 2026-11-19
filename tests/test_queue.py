from data_structures.queue import Queue

def test_queue():
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)

    assert queue.get_front() == 10
    assert queue.dequeue() == 10
    assert queue.get_front() == 20
    assert queue.dequeue() == 20