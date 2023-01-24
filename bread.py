numbers = '1234123987897942343000000000000000000000042212324'

#가장 좋아하는 숫자는?

nums = list(numbers)

d = dict()
for n in numbers:
    d[n] = d.get(n,0) + 1

max = 0
key = ""
for n, c in d.items():
    if max < c:
        max = c
        key = n

print(f"key: {max}, count: {key}")        





