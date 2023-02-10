N = int(input())
car_list = [int(input()) for i in range(N)]
count = 0


for current_num in range(1, N+1):
    
    if len(car_list) == 0:
        break
    offset = 0
    print('now=', current_num)
    print(car_list)
    try:
        pos = car_list.index(current_num)
    except:
        continue
    
    
    if pos != 0:    
        for j in car_list[:pos]:
            car_list.append(j)
    
    if N in car_list[:pos]:
        count +=1
        
    print(car_list)
    
    for j in range(1, len(car_list) - pos):
        if car_list[pos+j] == current_num+j:
            print("offset updated")
            offset +=1

    
    print('pos:', pos)
    print(car_list)
    car_list = car_list[pos+offset:]
    print(car_list, '\n')
            
print(count)
