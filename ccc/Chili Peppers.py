n = eval(input())
pepper = []
for i in range(n):
    a = input()
    pepper.append(a)
heat = {"Poblano" : 1500, "Mirasol" : 6000, "Serrano" : 15500, "Cayenne" : 40000, "Thai" : 75000, "Habanero" : 125000}
t = 0
for i in pepper:
    t += heat[i]
print(t)