from data_structures.stack import Stack

def test_stack():
    stack = Stack()

    stack.push(10)
    stack.push(20)

    assert stack.top() == 20
    assert stack.pop() == 20
    assert stack.top() == 10
    assert stack.is_empty() == False