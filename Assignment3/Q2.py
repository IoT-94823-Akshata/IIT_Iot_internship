A = "AKSHATA"

print(A[1:5]) #1-4
print(A[1:4])
print(A[:3])
print(A[3:])
print(A[::-3])

s = "Akshata" 
for char in s:
    print(char)

r = "KTE"
r = "D"+r[:3]
print(r)

r1 = r.replace("DKTE","Akshata")
print(r1)