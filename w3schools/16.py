for x in "banana":
  print(x)
#the_break_state
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
#thrid
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

for x in range(6):
  print(x)
print("razdelitel")
for x in range(2, 6):
  print(x)
print("razdelitel")
for x in range(2, 30, 3):
  print(x)
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)