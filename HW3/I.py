def func(n, a, b):
    main_road, side_road = [], []
    priority_dict = {1: 4, 4: 3, 3: 2, 2: 1}
    sim_dict = {1: 3, 2: 4, 3: 1, 4: 2}
    
    main_priority_list = [a, b]
    main_priority_list.sort()
    if main_priority_list == [1, 4]:
        main_priority_list = [4, 1]
    
    side_priority_list = []
    for d in range(1, 5):
        if d not in main_priority_list:
            side_priority_list.append(d)
    side_priority_list.sort()
    if side_priority_list == [1, 4]:
        side_priority_list = [4, 1]
        
    priority_list = main_priority_list + side_priority_list
    #print(priority_list)
    
    stack1, stack2, stack3, stack4 = [], [], [], []
    for i in range(n):
        d, t = map(int, input().split())
        if d == priority_list[0]:
            stack1.append([t, d, i])
        if d == priority_list[1]:
            stack2.append([t, d, i])
        if d == priority_list[2]:
            stack3.append([t, d, i])
        if d == priority_list[3]:
            stack4.append([t, d, i])

    stack1.sort()
    stack2.sort()
    stack3.sort()
    stack4.sort()
    
    '''print(stack1)
    print(stack2)
    print(stack3)
    print(stack4)'''
        
    time_map = [None] * n
    time_set = set()
        
    if sim_dict[a] == b:
        #print('case lines')
        #case lines

        # приоритет 1, главная дорога
        time = 1
        for rover in stack1:
            arrival_time, d, idx = rover
            time = max(time, arrival_time)
            time_map[idx] = time
            time_set.add(time)
            time += 1
            
        # приоритет 2, главная дорога (т.к. lines -- можно не пропускать, а ехать сразу)
        time = 1
        for rover in stack2:
            arrival_time, d, idx = rover
            time = max(time, arrival_time)
            time_map[idx] = time
            time_set.add(time)
            time += 1
        
        # приоритет 3, побочная дорога (надо уступать уже проехавшим)
        time = 1
        for rover in stack3:
            arrival_time, d, idx = rover
            time = max(time, arrival_time)
            while time in time_set:
                time += 1
            time_map[idx] = time
            #time_set.add(time) остались только 4 приоритет, а они могут ехать одновременно
            time += 1
        
        # приоритет 4, побочная дорога (уступаем только 1 и 2 приоритетам, с 3 едем одновременно)
        time = 1
        for rover in stack4:
            arrival_time, d, idx = rover
            time = max(time, arrival_time)
            while time in time_set:
                time += 1
            time_map[idx] = time
            #time_set.add(time)
            time += 1

        for t in time_map:
            print(t)
    else:
        #print('case crosses')
        #case crosses
        
        # приоритет 1, главная дорога
        time = 1
        for rover in stack1:
            arrival_time, d, idx = rover
            time = max(time, arrival_time)
            time_map[idx] = time
            time_set.add(time)
            time += 1
            
        # приоритет 2, главная дорога (т.к. crosses -- уступаем 1)
        time = 1
        for rover in stack2:
            arrival_time, d, idx = rover
            time = max(time, arrival_time)
            while time in time_set:
                time += 1
            time_map[idx] = time
            time_set.add(time) # 3е должны уступать нам
            time += 1
        
        # приоритет 3, побочная дорога (уступаем 1 и 2)
        time = 1
        for rover in stack3:
            arrival_time, d, idx = rover
            time = max(time, arrival_time)
            while time in time_set:
                time += 1
            time_map[idx] = time
            time_set.add(time) # 4е должны уступать нам
            time += 1
        
        # приоритет 4, побочная дорога (уступаем 1, 2 и 3 приоритетам)
        time = 1
        for rover in stack4:
            arrival_time, d, idx = rover
            time = max(time, arrival_time)
            while time in time_set:
                time += 1
            time_map[idx] = time
            #time_set.add(time)
            time += 1

        for t in time_map:
            print(t)
    
    
if __name__ == '__main__':
    n = int(input())
    a, b = map(int, input().split())
    func(n, a, b)
    

'''
8
1 3
1 1
2 1
3 1
4 1
1 2
2 2
3 2
4 2

4
2 3
3 1
2 1
2 2
2 3

#4
#1
#2
#3

4
1 4
1 1
4 1
4 2
1 2

#3
#1 
#2
#4















def func(n, a, b):
    main_road, side_road = [], []
    priority_dict = {1: 4, 4: 3, 3: 2, 2: 1}
    sim_dict = {1: 3, 2: 4, 3: 1, 4: 2}
    
    for i in range(n):
        d, t = map(int, input().split())
        if d in [a, b]:
            main_road.append([t, d, i])
        else:
            side_road.append([t, d, i])

    main_road.sort()
    side_road.sort()
    
    for rover in range(len(main_road) - 1):
        rov1 = main_road[rover]
        rov2 = main_road[rover + 1]
        if rov1[0] == rov2[0] and priority_dict[rov1[1]] == rov2[1]:
            rov1, rov2 = rov2, rov1
            main_road[rover] = rov1
            rov2[0] += 1
            main_road[rover + 1] = rov2
        elif rov1[0] == rov2[0] and priority_dict[rov2[1]] == rov1[1]:
            rov2[0] += 1
            main_road[rover + 1] = rov2
        
            
    for rover in range(len(side_road) - 1):
        rov1 = side_road[rover]
        rov2 = side_road[rover + 1]
        if rov1[0] == rov2[0] and priority_dict[rov1[1]] == rov2[1]:
            rov1, rov2 = rov2, rov1
            side_road[rover] = rov1
            rov2[0] += 1
            side_road[rover + 1] = rov2
        elif rov1[0] == rov2[0] and priority_dict[rov2[1]] == rov1[1]:
            rov2[0] += 1
            side_road[rover + 1] = rov2
    
    i = 0
    main_road_sim = []
    while i <= len(main_road) - 1:
        if i == len(main_road) - 1:
            rov1 = main_road[i]
            main_road_sim.append((rov1[0], [rov1[1]], [rov1[2]]))
            break
        
        rov1 = main_road[i]
        rov2 = main_road[i + 1]
        
        if rov1[0] == rov2[0] and sim_dict[rov1[1]] == rov2[1]:
            main_road_sim.append((rov1[0], [rov1[1], rov2[1]], [rov1[2], rov2[2]]))
            i += 2
        else:
            main_road_sim.append((rov1[0], [rov1[1]], [rov1[2]]))
            i += 1
            
    i = 0
    side_road_sim = []
    while i <= len(side_road) - 1:
        if i == len(side_road) - 1:
            rov1 = side_road[i]
            side_road_sim.append((rov1[0], [rov1[1]], [rov1[2]]))
            break
        
        rov1 = side_road[i]
        rov2 = side_road[i + 1]
        
        if rov1[0] == rov2[0] and sim_dict[rov1[1]] == rov2[1]:
            side_road_sim.append((rov1[0], [rov1[1], rov2[1]], [rov1[2], rov2[2]]))
            i += 2
        else:
            side_road_sim.append((rov1[0], [rov1[1]], [rov1[2]]))
            i += 1
        
        
    #print(main_road)
    #print(side_road)    
    #print(main_road_sim)
    #print(side_road_sim)

    time_map = [None] * n
    time_set = set()

    # Проезжают роверы с главной дороги
    time = 1
    for rover_pile in main_road_sim:
        arrival_time, d_pile, idx_pile = rover_pile
        time = max(time, arrival_time)
        for idx in idx_pile:
            time_map[idx] = time
        time_set.add(time)
        time += 1
        
    
    time = 1
    for rover_pile in side_road_sim:
        arrival_time, d_pile, idx_pile = rover_pile
        time = max(time, arrival_time)
        while time in time_set:
            time += 1
        for idx in idx_pile:
            time_map[idx] = time
        time_set.add(time)
        time += 1

    for t in time_map:
        print(t)
        
        
        
        
def func(n, a, b):
    main_road, side_road = [], []
    priority_dict = {1: 4, 4: 3, 3: 2, 2: 1}
    sim_dict = {1: 3, 2: 4, 3: 1, 4: 2}
    
    for i in range(n):
        d, t = map(int, input().split())
        if d in [a, b]:
            main_road.append([t, d, i])
        else:
            side_road.append([t, d, i])

    main_road.sort()
    side_road.sort()
    
    if sim_dict[a] == b:
        #case lines
    
        i = 0
        main_road_sim = []
        while i <= len(main_road) - 1:
            if i == len(main_road) - 1:
                rov1 = main_road[i]
                main_road_sim.append((rov1[0], [rov1[1]], [rov1[2]]))
                break
            
            rov1 = main_road[i]
            rov2 = main_road[i + 1]
            
            if rov1[0] == rov2[0] and sim_dict[rov1[1]] == rov2[1]:
                main_road_sim.append((rov1[0], [rov1[1], rov2[1]], [rov1[2], rov2[2]]))
                i += 2
            else:
                main_road_sim.append((rov1[0], [rov1[1]], [rov1[2]]))
                i += 1
                
        i = 0
        side_road_sim = []
        while i <= len(side_road) - 1:
            if i == len(side_road) - 1:
                rov1 = side_road[i]
                side_road_sim.append((rov1[0], [rov1[1]], [rov1[2]]))
                break
            
            rov1 = side_road[i]
            rov2 = side_road[i + 1]
            
            if rov1[0] == rov2[0] and sim_dict[rov1[1]] == rov2[1]:
                side_road_sim.append((rov1[0], [rov1[1], rov2[1]], [rov1[2], rov2[2]]))
                i += 2
            else:
                side_road_sim.append((rov1[0], [rov1[1]], [rov1[2]]))
                i += 1
            
            
        #print(main_road)
        #print(side_road)    
        #print(main_road_sim)
        #print(side_road_sim)

        time_map = [None] * n
        time_set = set()

        # Проезжают роверы с главной дороги
        time = 1
        for rover_pile in main_road_sim:
            arrival_time, d_pile, idx_pile = rover_pile
            time = max(time, arrival_time)
            for idx in idx_pile:
                time_map[idx] = time
            time_set.add(time)
            time += 1
            
        
        time = 1
        for rover_pile in side_road_sim:
            arrival_time, d_pile, idx_pile = rover_pile
            time = max(time, arrival_time)
            while time in time_set:
                time += 1
            for idx in idx_pile:
                time_map[idx] = time
            #time_set.add(time)
            time += 1

        for t in time_map:
            print(t)
    else:
        pass
    
'''