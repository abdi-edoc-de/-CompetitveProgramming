prefix='+4*312'
revers=prefix[::-1]
print(revers)
stack = []
operater = "-+*/"
for i in revers:
    if i not in operater:
        stack.append(i)
    if i in operater:
        temp = f"({stack.pop()} {i} {stack.pop()})"
        stack.append(temp)
print((stack.pop()))

        
      