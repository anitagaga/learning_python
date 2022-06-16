# len(s)
# str()
# upper()
# count(sub[, start[, end]])
# isupper()
# islower()
# split(sep=None, maxsplit=-1)
# rsplit
# strip()
# lstrip([chars])
# rstrip([chars])
# replace(ald, new[, count])
# find(sub[, start[, end]])
# index(sub[, start[, end]])

# len(s)
x = "anita"
print(len(x))

# str() converts value into a String
y = 533453
print(str(y))
z = str(y)
print(z.find("53"))

# upper()
print(x.upper())

# count(sub[, start[, end]])
x = "anita academy academy anita is my favorite place to be anita"
print(x.count("anita"))
print(x.count("anita",0,10))

# isupper()
# islower()
x = "anita"
y = "ANITA"
print(x.isupper())
print(x.islower())

print(y.isupper())
print(y.islower())

# split(sep=None, maxsplit=-1)
# rsplit
x = "anita academy academy anita is my favorite place to be anita"
print(x.split())

# strip()
# lstrip([chars]) - removes from the left
# rstrip([chars]) - removes from the right
x = "   $%^&anita academy academy anita is my favorite place to be anita"
print(x.strip())
print(x.strip('$% ^&'))

# replace(ald, new[, count])
x = "anita anita anita beautiful"
print(x.replace("anita", "gaga", 2))

# find(sub[, start[, end]])
# index(sub[, start[, end]])
x = "123anita anita anita beautiful"
print(x.find("anita"))
print(x.index("anita"))

