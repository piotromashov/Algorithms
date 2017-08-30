#!/bin/python3
#https://www.hackerrank.com/challenges/ctci-find-the-running-median
import sys

def lt(x,y):
	return x<y
def gt(x,y):
	return x>y

class Heap:
	def __init__(self, heapType):
		self.storage = []
		self.comparer = lt
		if heapType == "max":
			self.comparer = gt

	def add(self, element):
		self.storage.append(element)
		self.heapUp()

	def heapUp(self):
		index = len(self.storage)-1
		while self.hasSwappableParent(index):
			index = self.swapParent(index)

	def hasSwappableParent(self, index):
		parentIndex = (index-1)//2
		return parentIndex >= 0 and self.comparer(self.storage[index], self.storage[parentIndex])
	
	def swapParent(self, index):
		parentIndex = (index-1)//2
		self.swap(index, parentIndex)
		return parentIndex

	def swap(self, index1, index2):
		self.storage[index1], self.storage[index2] = self.storage[index2], self.storage[index1]

	def size(self):
		return len(self.storage)

	def top(self):
		return self.storage[0]

	def pop(self):
		aux = self.storage[0]
		self.storage[0] = self.storage.pop()
		self.heapDown()
		return aux

	def heapDown(self):
		index = 0
		while self.hasSwappableChildren(index):
			index = self.swapChildren(index)

	def swapChildren(self, index):
		childrenIndex = index*2+1
		if childrenIndex+1 < len(self.storage) and self.comparer(self.storage[childrenIndex+1], self.storage[childrenIndex]):
			childrenIndex += 1
		self.swap(index, childrenIndex)
		return childrenIndex

	def hasSwappableChildren(self, index):
		childrenIndex = index*2+1
		return childrenIndex < len(self.storage) and self.comparer(self.storage[childrenIndex], self.storage[index])

class Median:
	def __init__(self):
		self.min_heap = Heap("min")
		self.max_heap = Heap("max")

	def add(self, element):
		if self.min_heap.size() == 0 or element > self.min_heap.top():
			self.min_heap.add(element)
		else:
			self.max_heap.add(element)
		self.rebalance()

	def rebalance(self):
		while self.min_heap.size() - self.max_heap.size() > 1:
			self.max_heap.add(self.min_heap.pop())
		while self.max_heap.size() - self.min_heap.size() > 1:
			self.min_heap.add(self.max_heap.pop())

	def median(self):
		if self.min_heap.size() == self.max_heap.size():
			return (self.min_heap.top()+self.max_heap.top())/2
		elif self.min_heap.size() > self.max_heap.size():
			return self.min_heap.top()*1.0
		else:
			return self.max_heap.top()*1.0

n = int(input().strip())
mh = Median()
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   mh.add(a_t)
   print(mh.median())