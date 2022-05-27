n1 = input("Enter first binary number: ")
n2 = input("Enter second binary number: ")

# This part is for prepping the numbers

if "." in n1:
    n1 = [list(n1.split(".")[0]), list(n1.split(".")[1])]
else:
    n1 = [list(n1), ['0']]
if "." in n2:
    n2 = [list(n2.split(".")[0]), list(n2.split(".")[1])]
else:
    n2 = [list(n2), ['0']]

if len(n1[0]) < len(n2[0]):
    for i in range(len(n2[0])-len(n1[0])):
        n1[0].insert(0, '0')
elif len(n2[0]) < len(n1[0]):
    for i in range(len(n1[0])-len(n2[0])):
        n2[0].insert(0, '0')


if len(n1[1]) < len(n2[1]):
    for i in range(len(n2[1])-len(n1[1])):
        n1[1].append('0')
elif len(n2[1]) < len(n1[1]):
    for i in range(len(n1[1])-len(n2[1])):
        n2[1].append('0')

# Actual calculation

print()
ans1 = []
ans2 = []
carry = 0
for i in range(-1, -len(n1[1])-1, -1):
    if carry + int(n1[1][i])+int(n2[1][i]) == 0:
        ans2.insert(0, '0')
        carry = 0
    elif carry + int(n1[1][i])+int(n2[1][i]) == 1:
        ans2.insert(0, '1')
        carry = 0
    elif carry + int(n1[1][i])+int(n2[1][i]) == 2:
        ans2.insert(0, '0')
        carry = 1
    elif carry + int(n1[1][i])+int(n2[1][i]) == 3:
        ans2.insert(0, '1')
        carry = 1
    print(n1[1][i], "+", n2[1][i], "+", carry)
    print(ans2)
print()
for i in range(-1, -len(n1[0])-1, -1):
    if carry + int(n1[0][i])+int(n2[0][i]) == 0:
        ans1.insert(0, '0')
        carry = 0
    elif carry + int(n1[0][i])+int(n2[0][i]) == 1:
        ans1.insert(0, '1')
        carry = 0
    elif carry + int(n1[0][i])+int(n2[0][i]) == 2:
        ans1.insert(0, '0')
        carry = 1
    elif carry + int(n1[0][i])+int(n2[0][i]) == 3:
        ans1.insert(0, '1')
        carry = 1
    print(n1[0][i], "+", n2[0][i], "+", carry)
    print(ans1)

# Cleaning up and making it look presentable

ans1.insert(0, str(carry))
answer = ""
for l in ans1:
    answer += l
answer += "."
for l in ans2:
    answer += l

# Final printing

print()
print(answer.lstrip("0"))
