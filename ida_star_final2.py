import numpy as np 
city = [] # name of city 
city_dict = {} # name be ezai yek index rahnama
numberofcity = int(input("number of city:")) 
a = np.zeros((numberofcity, numberofcity)) 
x_range = range(0, numberofcity)
for i in x_range:
    nameofcity = str(input("name of city: "))
    city.append(nameofcity)  
    x_counter = i 
    city_dict[nameofcity] = x_counter
    if i == 0:
        start_index = x_counter
        start_name = nameofcity
visit_cost=[]
print(city_dict) #rahnama to terminal baraye kam shodan khata
print("9999 is a unrout key")#9999 is a largest num and its mean is not route betwean i ,j
for i_i in range(0, numberofcity):
    for j_j in range(0, numberofcity):
        visitedd = False
        for pathh in visit_cost: 
            if city[i_i] in pathh and city[j_j] in pathh : 
                visitedd = True
                a[i_i][j_j] = pathh[2] 
        if i_i == j_j:
            a[i_i][j_j] = 9999  
        elif not visitedd :
            route = int(input("enter cost of {} , {}: ".format(city[i_i], city[j_j])))
            a[i_i][j_j] = route 
            visit_cost.append([city[i_i] , city[j_j] , route])
best_path = []
best_matrix = float('inf')
met = set([start_index])
def iterativ_deepening_star(current_state, path, cost, depth): 
    global best_path, best_matrix 
    if depth == numberofcity: #place of start a work of cuttoff and f(n)
        cost+= a[current_state][start_index]
        if cost < best_matrix:
            best_matrix = cost
            best_path = path[:] 
    for i in range(numberofcity): 
        if i not in met :
            met.add(i) 
            path.append(city[i]) 
            iterativ_deepening_star(i, path, cost + a[current_state][i], depth+1)
            met.remove(i) 
            path.pop()
iterativ_deepening_star(start_index, [start_name], 0, 1)
print("path:", ' --- '.join(best_path))
print("sum of cost :", best_matrix)
