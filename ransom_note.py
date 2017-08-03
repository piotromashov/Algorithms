# Sample input
# 6 4
# give me one grand today night
# give one grand today

# Sample output
# Yes

# Sample input
# 6 5
# two times three is not four
# two times two is four

# Sample Output 1
# No


def ransom_note(magazine, ransom):
    
    words = {}
    
    for word in magazine:
        if not word in words:
            words[word] = 1
        else:
            words[word] += 1

    print(words)
            
    for word in ransom:
        if word in words and words[word] > 0:
            words[word] -= 1
        else:
            return False
        
    return True

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    