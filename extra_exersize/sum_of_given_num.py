# # 1st way

# n =int(input('Enter number:'))
# sum = (n + 1) * n /2
# print(type(sum))
# print(f"Sum is: {round(sum)}")



#2nd way

n = int(input("Enter number:"))

total = 0
for scores in range(n):
  total = (scores+1)* scores / 2 

print(total)