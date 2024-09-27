import heapq


def Asearch(start,goal,gridded_map):
    open_list=[]
    close_list={}
    number_of_states=0
    goal_x=goal.get_x()
    goal_y=goal.get_y()

    
    heapq.heappush(open_list,start)  # push to both open and close list

    close_list[start.state_hash()]=start

    while open_list!=[]:
        current_state=heapq.heappop(open_list)  # get current state
        number_of_states+=1
        if current_state==goal:###
            return current_state.get_g(),number_of_states  # check for goal
        
        children=gridded_map.successors(current_state)
        for child in children:  # go through children
            
            hash_value=child.state_hash()
            x=child.get_x()
            y=child.get_y()

            delta_x=abs(x-goal_x)
            delta_y=abs(y-goal_y)
            h=1.5*min(delta_y,delta_x)+abs(delta_x-delta_y)

            child.set_cost(h+child.get_g())
    
            if hash_value not in close_list:  # add new child in both lists
                heapq.heappush(open_list,child)
                close_list[hash_value]=child

            else:
                
                if (child.get_cost())< close_list[hash_value].get_cost() or (child.get_g())< close_list[hash_value].get_g():  # new cheaper path
                    heapq.heappush(open_list,child)
                    close_list[hash_value]=child
                    # close_list[hash_value].set_cost(child.get_cost())  # update new cost
                    # close_list[hash_value].set_g(child.get_g()) 


                
    return -1,-1  # no solution

            