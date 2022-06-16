demo_set1 = {"Delhi", "Mumbai", "Melborne", "Sydney", "Kolkata"}

# add(elem)
print(demo_set1)
demo_set1.add("London")
print(demo_set1)

# remove(elem), .discard, .pop
demo_set1.remove("Delhi")
print(demo_set1)
demo_set1.discard("London")
print(demo_set1)
demo_set1.pop()
print(demo_set1)

# clear
demo_set1.clear()
print(demo_set1)

# union
demo_set1 = {"Delhi", "Mumbai", "Melborne", "Sydney", "Kolkata"}
demo_set2 = {"Delhi", "Mumbai", "Melborne", "Sydney", "Kolkata", "New Yourk"}
print(demo_set1)
demo_set3 = demo_set1.union(demo_set2)
print(demo_set3)

# update
print(demo_set1)
print(demo_set2)
demo_set1.update(demo_set2)
print(demo_set1)

# intersection, intersection_update
demo_set1 = {"Delhi", "Mumbai", "Melborne", "Sydney", "Kolkata"}
demo_set2 = {"Delhi", "Mumbai", "Melborne", "Sydney", "Kolkata", "New Yourk"}
demo_set3 = demo_set1.intersection(demo_set2)
print(demo_set3)

demo_set1 = {"Delhi", "Mumbai", "Melborne", "Sydney", "Kolkata"}
demo_set2 = {"Delhi", "Mumbai", "Melborne", "Sydney", "Kolkata", "New Yourk"}
print(demo_set1)
demo_set1.intersection_update(demo_set2)
print(demo_set1)


demo_set1 = {"Delhi", "Mumbai", "Melborne", "Sydney", "Kolkata"}
demo_set2 = {"Delhi", "Mumbai", "Melborne", "Sydney", "Kolkata", "New Yourk"}
print(demo_set1)
demo_set3 = demo_set1.difference(demo_set2)
print(demo_set3)
demo_set3 = demo_set2.difference(demo_set1)
print(demo_set3)

#issubset, issuperset
demo_set1 = {"Delhi", "Mumbai", "Melborne", "Sydney", "Kolkata"}
demo_set2 = {"Delhi", "Mumbai", "Melborne", "Sydney", "Kolkata", "New Yourk"}
demo_set3 = demo_set1.issubset(demo_set2)
print(demo_set3)
demo_set3 = demo_set1.issuperset(demo_set2)
print(demo_set3)