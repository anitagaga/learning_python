# s[i:j] - slice of s from i to j
# s[i:j:k] - slice of s from i to j with step k
# s[startindex:endingidex:step]

s = "welcome to software testing class"
s2 = 'welcome to software testing class'

print(s)
print(s[0])
print(s[-1])
print(s[0:8])
print(s[4:8])
print(s[4:8:1])
print(s[4:8:2])
print(s[0:])
print(s[0:-1])
print(s[:])

print(s[-5:-1])
print(s[20:])

print(s[::-1])

comma = "one, two, three, four"

print(comma.index(","))
print(comma[0:comma.index(",")])
