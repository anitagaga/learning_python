cities = ["Delhi","Mumbai","Melborne","Sydney","Kolkata"]

#list.append()
print(cities)
cities.append("Lucknow")
print(cities)

#list.insert()
cities.insert(1,"Lucknow")
print(cities)

#list.remove
cities.remove("Mumbai")
print(cities)

#list.pop
cities.pop(3)
print(cities)

#list.index
print(cities.index("Kolkata"))

#list.count
print(cities.count("Kolkata"))

#list.sort ; list.reverse
print(cities)
cities.sort()
print(cities)
cities.reverse()
print(cities)

#list.copy
new_cities = cities.copy()
print(new_cities)

#clear
new_cities.clear()
print(new_cities)