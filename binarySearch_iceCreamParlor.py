#https://www.hackerrank.com/challenges/ctci-ice-cream-parlor

def binarySearch(a, element):
	start = 0
	end = len(a)-1
	while start <= end:
		mid = start + (end-start)//2
		if element == a[mid]:
			return True
		elif element > a[mid]:
			start = mid+1
		else:
			end = mid-1
	return False

def find(a, element):
	a.sort()
	return binarySearch(a, element)

t = int(input().strip())
for a0 in range(t):
	m = int(input().strip())
	n = int(input().strip())
	a = list(map(int, input().strip().split(' ')))

	for element in a:
		b = a.copy()
		b.remove(element)
		if find(b, m-element):
			firstIndex = a.index(element)+1
			a.remove(element)
			secondIndex = a.index(m-element)+2
			if firstIndex < secondIndex:
				print("{} {}".format(firstIndex, secondIndex))
			else:
				print("{} {}".format(secondIndex, firstIndex))
			break
		
