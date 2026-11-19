from data_structures.linked_list import LinkedList

def test_append():
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)

    assert linked_list.head.data == 10
    assert linked_list.head.next.data == 20
    assert linked_list.head.next.next.data == 30