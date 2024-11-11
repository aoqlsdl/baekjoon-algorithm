import sys

word = sys.stdin.readline().strip()
elem = sys.stdin.readline().strip()

i = 0
cnt = 0

while i < len(word):
    if word[i:i+len(elem)] == elem:
        i += len(elem)
        cnt += 1
    else :
        i += 1

print(cnt)