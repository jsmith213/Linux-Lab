import sys

shift = int(sys.argv[1])
result = []

for line in sys.stdin:
    for ch in line:
        if ch.isalpha():
            c = ord(ch.upper()) - ord('A')
            c = (c + shift) % 26
            result.append(chr(c + ord('A')))

# Print in blocks of 5, 10 blocks per line
blocks = [''.join(result[i:i+5]) for i in range(0, len(result), 5)]
for i in range(0, len(blocks), 10):
    print(' '.join(blocks[i:i+10]))