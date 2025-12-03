#list
a= 'ali'
b=[1,2,3,4,5]

print("length: ",len(a))

print("max value: ",max([1,4,6,3,7,2]))

print("min value: ",min([1,4,6,3,7,2]))

print("sum value: ",sum([1,4,6,3,7,2]))

b.append(6)
print("append value: ",b)

b.insert(1,6)
print(f"insert value at {1}: ",b)

b.extend([1,6])
print(f"extend value: ",b)

b.remove(2)
print(f"remove value: ",b)

b.pop()
print(f"pop value: ",b)

b.clear()
print(f"clear value: ",b)

print(f"index value: ",b.index(3))

print(f"count value: ",b.count(3))

b.sort()
print(f"sort value: ",b)

b.reverse()
print(f"reverse value: ",b)


