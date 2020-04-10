n = int(input().strip())
s = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])
count=0
for i in range((n-m)+1):
    c=0
    for j in range(i,(i+m)):
        c+=s[j]
    if(c==d):
        count+=1
print(count)
