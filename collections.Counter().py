# Enter your code here. Read input from STDIN. Print output to STDOUT
total = 0
n = int(input(''))
size = list(map(int, input().split()))
m = int(input(''))
for i in range(m):
    order = list(map(int, input().split()))
    if order[0] in size:
        total = total + order[1]
        size.remove(order[0])
print(total) 
