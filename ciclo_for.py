range(5) # [0,1,2,3,4]
range(5, 40, 3)
for i in range(5, 0, -1): #vamos desde 5 hasta 1 bajando
    print("Solo i: ",  i)

for i in range(30):
  if i % 3 != 0:
    continue
  else:
    print(i**2)