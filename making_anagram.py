def number_needed(a, b):
    a = sorted(a)
    b = sorted(b)
    i = 0
    while i < len(a):
        if a[i] in b:
            b.remove(a[i])
            a.remove(a[i])
        else:
            i += 1

    return len(a) + len(b)


def number_needed(a, b):
    a = sorted(a)
    b = sorted(b)
    deletions = 0
    index_a = 0
    index_b = 0
    
    while(index_a < len(a) and index_b < len(b)):
        if(a[index_a] == b[index_b]):
            index_a += 1
            index_b += 1
        elif(a[index_a] < b[index_b]):
            deletions += 1
            index_a += 1
        else:
            deletions += 1
            index_b += 1
            
    if(index_a == len(a) and index_b < len(b)):
        deletions += len(b)-index_b
    if(index_b == len(b) and index_a < len(a)):
        deletions += len(a)-index_a
    
    return deletions

a = input().strip()
b = input().strip()

print(number_needed(a, b))
