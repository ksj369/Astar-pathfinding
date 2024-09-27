import heapq

def MMs(start,goal,gridded_map):
    openf=[]
    openb=[]
    closef={}
    closeb={}
    number_of_states=0
    goal_x=goal.get_x()
    goal_y=goal.get_y()

    


    start_x=start.get_x()
    start_y=start.get_y()


    delta_x=abs(start_x-goal_x)
    delta_y=abs(start_y-goal_y)
    h=1.5*min(delta_y,delta_x)+abs(delta_x-delta_y)
    p=max(h+start.get_g(),2*start.get_x())

    start.set_cost(p)

    p=max(h+goal.get_g(),2*goal.get_x())
    goal.set_cost(p)
    

    heapq.heappush(openf,start)  #push in both open list and close
    heapq.heappush(openb,goal)

    closef[start.state_hash()]=start
    closeb[goal.state_hash()]=goal

    u=float("inf")

    while openb!=[] and openf!=[]:
        if  u<=min(openf[0].get_cost() , openb[0].get_cost()):   # chekc for optimal solution
            return u,number_of_states

        if openf[0].get_cost()<openb[0].get_cost():
            current=heapq.heappop(openf)
            number_of_states+=1

            children=gridded_map.successors(current)  # get surrounding state

            for child in children:
                x=child.get_x()
                y=child.get_y()
                #child.set_g(child.get_g())#
                delta_x=abs(x-goal_x)
                delta_y=abs(y-goal_y)
                h=1.5*min(delta_y,delta_x)+abs(delta_x-delta_y)
                p=max(h+child.get_g(),2*child.get_x())
                child.set_cost(p)

                if child.state_hash() in closeb:
                    #####
                    u=min(u,child.get_g()+closeb[child.state_hash()].get_g())  # calculateminimum value

                if child.state_hash() not in closef:  # add new element ot lists
                   
                    
                    heapq.heappush(openf,child)
                    closef[child.state_hash()]=child

                if child.state_hash() in closef and (child.get_cost()<closef[child.state_hash()].get_cost() or child.get_g()<closef[child.state_hash()].get_g() ):  # new cheaper cost


                    closef[child.state_hash()]=child
                   # closef[child.state_hash()].set_cost(child.get_cost())  # update cost and reheapify
                    for st in openf:
                        if st==child:
                            st.set_cost(child.get_cost())
                            st.set_g(child.get_g())
                    heapq.heapify(openf)
        else:


            current=heapq.heappop(openb)  #back ward search
            number_of_states+=1

            children=gridded_map.successors(current)

            for child in children:
                x=child.get_x()
                y=child.get_y()
                #child.set_g(child.get_g())#
                delta_x=abs(x-start_x)
                delta_y=abs(y-start_y)
                h=1.5*min(delta_y,delta_x)+abs(delta_x-delta_y)

                p=max(h+child.get_g(),2*child.get_x())
                child.set_cost(p)


                if child.state_hash() in closef:
                    #
                    u=min(u,child.get_g()+closef[child.state_hash()].get_g())

                if child.state_hash() not in closeb:
                   
                    heapq.heappush(openb,child)
                    closeb[child.state_hash()]=child

                if child.state_hash() in closeb and (child.get_cost()<closeb[child.state_hash()].get_cost() or child.get_g()<closeb[child.state_hash()].get_g()):


                    closeb[child.state_hash()]=child
                    #closeb[child.state_hash()].set_cost(child.get_cost())
                    for st in openb:
                        if st==child:
                            st.set_cost(child.get_cost())
                            st.set_g(child.get_g())
                    heapq.heapify(openb)

    return -1,-1  # no solution

                    

