#Day 6 Universal Orbit Map

data = open('inputdata.txt', 'r').read().split('\n')
links = []

for i in data:
   links.append(i.split(')')) 

counter = 0
youpath = []
sanpath = []

for i in range(len(links)-1):
    current_orbit = links[i]
    if(current_orbit[1] == 'YOU'): 
        j = 0
        youpath.append(current_orbit)
        while(True):
            orbit_judged = links[j]

            if current_orbit[0] == 'COM':
                counter += 1
                print("COM found")
                youpath.append(current_orbit)
                break

            if current_orbit[0] == orbit_judged[1]:
                counter += 1
                current_orbit = orbit_judged
                youpath.append(current_orbit)

            if j == (len(links) -2):
                j = 0
            else:
                j += 1

    if (current_orbit[1] == 'SAN'):
        j = 0
        sanpath.append(current_orbit)
        while(True):
            orbit_judged = links[j]
                                            
            if current_orbit[0] == 'COM':
                counter += 1
                print("COM found")
                sanpath.append(current_orbit)
                break
                                            
            if current_orbit[0] == orbit_judged[1]:
                counter += 1
                current_orbit = orbit_judged
                sanpath.append(current_orbit)
            if j == (len(links)-2):
                j = 0
            else:
                j += 1

samepath = [] 
for i in range(len(sanpath)):
    for j in range(len(youpath)):
        if (sanpath[i] == youpath[j]):
            samepath.append(sanpath[i])

for i in samepath:
    for j in sanpath:
        if (i == j):
            sanpath.pop(sanpath.index(j))

    for k in youpath:
        if(i == k):
            youpath.pop(youpath.index(k))



print(samepath)
print(youpath)
print(sanpath)
print(f'The length of samepath is {len(samepath)}')
print(f'The length of youpath is {len(youpath)}')
print(f'The length of sanpath is {len(sanpath)}')


print(len(youpath) + len(sanpath) - 2)
