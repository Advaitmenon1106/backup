import random as rand
results = {1: 0, 0: 0} #results of the simulation, 1 = switched, 0 = did not switch
counter = 0
while counter!=1000000:

    price_winner_index = rand.randint(0, 2) #the actual door containing the car: only host knows what door this is
    participant_choice_ind = rand.randint(0, 2) #All 3 doors are closed, participant chooses a door

    i = 0
    #Host's move (opens a door that isnt the participant's choice and also NOT the one that has the car)
    while True: #Eventually only one number is chosen here
        i = rand.randint(0, 2)
        if i != price_winner_index and i != participant_choice_ind:
            break 
        else:
            continue

    host_choice_index = i

    while True:
        switched = rand.randint(0, 2)
        if switched!=participant_choice_ind and switched!=host_choice_index:
            break
        else:
            continue

    if switched == price_winner_index:
        results[1] +=1
    else:
        results[0]+=1
    counter+=1

print(results)
print(results[1]/(results[0]+results[1])) 
#This is the final probability that if the participants switches the doors, s/he gets the car at a probability of approx 0.666..