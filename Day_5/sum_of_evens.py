#Write your code below this row 👇
sum_even = 0

for i in range(2,101,2):
    sum_even += i

print(sum_even)


## 2nd way
total = 0
for i in range(1,101):
    if i%2 == 0:
        total += i

print(total)
