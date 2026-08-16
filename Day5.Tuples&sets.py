#create a tuple
nums = ("1", "4", "2", "3", "4", "5", "4")
print(nums)

#acess tuple elements
print(nums[0:6])

#find tuple length
print(len(nums))

#count a tuple length
print(nums.count("4"))

#find index of a tuple element
print(nums[0:4])
print(nums[::-1])
print(nums[::])

#create set
s1 = {10, 20, 30, 40, 80}
s2 = {40, 50, 60, 70}
print(type(s1))
print(s1)
print(type(s2))
print(s2)

#add an element to a set
s1.add(90)
print(s1)

#remove element from set
s2.remove(70)
print(s2)

#find union
print(s1|s2)

#find intersection
print(s1&s2)