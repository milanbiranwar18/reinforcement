# calculate duplicate value
import time
s = time.time()
n = [1, 5, 6, 6, 4, 50]
duplicate = None
for i in range(len(n)):
    for j in range(i+1, len(n)):
        if n[i] == n[j]:
            duplicate = n[i]
e = time.time()
print(e-s)
print(duplicate)



