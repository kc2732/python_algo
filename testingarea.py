dic = {}
s = "chenkun"
t = "chenkun1"
tmp = 0
for char in s+t:
    tmp ^= ord(char)
print chr(tmp)