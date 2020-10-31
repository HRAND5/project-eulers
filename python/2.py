current = 1
last = 1
s = 0
while current < 4000000:
    if current % 2 == 0:
        s += current
    new = current + last 
    last = current 
    current = new

print(s)
