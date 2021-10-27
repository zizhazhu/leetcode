#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存机制
#

# @lc code=start
class LinkNode:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.val = value
        self.next = next
        self.prev = prev


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, key, value):
        node = LinkNode(key, value)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        return node

    def renew(self, node):
        if node != self.head:
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev
            node.prev.next = node.next
            node.next = self.head
            node.prev = None
            self.head.prev = node
            self.head = node

    def pop(self):
        node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            node.prev.next = None
            self.tail = node.prev
        return node.key
            

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.link = LinkList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self.link.renew(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.link.renew(node)
        else:
            if len(self.map) == self.capacity:
                remove_key = self.link.pop()
                self.map.pop(remove_key)
            node = self.link.push(key, value)
            self.map[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

if __name__ == '__main__':
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    lru.get(1)
    lru.put(3, 3)
    lru.get(2)