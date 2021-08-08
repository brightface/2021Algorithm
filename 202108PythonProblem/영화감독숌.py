n = int(input())
name = "665"
cnt = 0

while True:
    name = int(name) +1
    if "666" in str(name):
        cnt += 1
        if n == cnt:
            break
print(name)
