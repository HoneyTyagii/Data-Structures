# 432. All O`one Data Structure

# Hard

# Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

# Implement the AllOne class:

# AllOne() Initializes the object of the data structure.
# inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
# dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
# getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
# getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
# Note that each function must run in O(1) average time complexity. 

# Example 1:

# Input
# ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
# [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
# Output
# [null, null, null, "hello", "hello", null, "hello", "leet"]

# Explanation
# AllOne allOne = new AllOne();
# allOne.inc("hello");
# allOne.inc("hello");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "hello"
# allOne.inc("leet");
# allOne.getMaxKey(); // return "hello"
# allOne.getMinKey(); // return "leet"

# Constraints:

# 1 <= key.length <= 10
# key consists of lowercase English letters.
# It is guaranteed that for each call to dec, key is existing in the data structure.
# At most 5 * 104 calls will be made to inc, dec, getMaxKey, and getMinKey.

class ListNode:
    def __init__(self, count: int = -1):
        self.prev = None
        self.next = None
        self.words = set()
        self.count = count

class DoubleLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_word(self, node: ListNode, word: str) -> None:
        node.words.remove(word)

        if not node.words:
            self.remove_node(node)

    def remove_node(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add_right_node(self, current_node: ListNode, new_node: ListNode) -> None:
        new_node.next = current_node.next
        current_node.next.prev = new_node
        new_node.prev = current_node
        current_node.next = new_node

class AllOne:
    def __init__(self):
        self.word_to_node = {}
        self.double_linked_list = DoubleLinkedList()

    def inc(self, key: str) -> None:
        if key in self.word_to_node:
            current_node = self.word_to_node[key]
            next_node = current_node.next
            count = current_node.count + 1

            if next_node.count != count:
                next_node = ListNode(count)
                self.double_linked_list.add_right_node(current_node, next_node)

            next_node.words.add(key)
            self.word_to_node[key] = next_node
            self.double_linked_list.remove_word(current_node, key)
        else:
            head = self.double_linked_list.head
            next_node = head.next

            if next_node.count != 1:
                next_node = ListNode(1)
                self.double_linked_list.add_right_node(head, next_node)
 
            next_node.words.add(key)
            self.word_to_node[key] = next_node          

    def dec(self, key: str) -> None:
        current_node = self.word_to_node[key]
        count = current_node.count - 1

        if count == 0:
            del self.word_to_node[key]
        else:
            prev_node = current_node.prev
            next_node = prev_node

            if prev_node.count != count:
                next_node = ListNode(count)
                self.double_linked_list.add_right_node(prev_node, next_node)

            next_node.words.add(key)
            self.word_to_node[key] = next_node

        self.double_linked_list.remove_word(current_node, key)

    def getMaxKey(self) -> str:
        words = self.double_linked_list.tail.prev.words

        if words:
            word = words.pop()
            words.add(word)
            return word
            
        return ""

    def getMinKey(self) -> str:
        words = self.double_linked_list.head.next.words

        if words:
            word = words.pop()
            words.add(word)
            return word

        return ""