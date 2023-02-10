N = int(input())
car_list = [int(input()) for i in range(N)]
count = 0
exit_car_number = 1

while exit_car_number < N:
    print(car_list)
    current_car = car_list.pop(0)
    
    if current_car != exit_car_number:
        car_list.append(current_car)
        
        if current_car == N:
            count +=1
    
    else:        
        exit_car_number +=1

print(count)