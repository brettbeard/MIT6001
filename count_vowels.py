
s = 'azcbobobegghakl'
count = 0
for ch in s:

    if ch in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print('Number of vowels: ' + str(count))