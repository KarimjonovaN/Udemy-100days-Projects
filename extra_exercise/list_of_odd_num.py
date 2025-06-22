list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

even = []
odd = []
for n in list1:
  if (n % 2) != 0:
      odd.append(n)

for i in list2:
    if i % 2 ==0:
        even.append(i)

final_list = odd + even

print(f"Result list: {final_list}")
