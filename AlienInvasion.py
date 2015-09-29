import matplotlib.pyplot as plt
import random as rand

class alien:

    state = 0 #Unhatched
    lifetime = 0
    sex = 0

    def __init__(self):
        self.sex= rand.randint(0,1)
        return


days = 30
num_eggs = 3
hatch_time = 5
num_landed = 2

day_ticker = [1]
alien_ticker = [1]

aliens = []

for x in range(num_landed):
    aliens.append(alien())
    aliens[x].state = 1

for x in range(1,days+1):
    a = len(aliens)
    for y in range(a):
        if aliens[y].state == 1 and aliens[y].sex == 0: #For each alien if hatched
            for i in range(num_eggs):
                aliens.append(alien()) #Create new alien
        elif aliens[y].state == 0: #If unhatched
            if aliens[y].lifetime < hatch_time: #if younger than hatch_time
               aliens[y].lifetime = aliens[y].lifetime+1    #increase age
            elif aliens[y].lifetime == hatch_time: #if
                hatch_time
                aliens[y].state = 1        #hatch
    day_ticker.append(x)
    alien_ticker.append(len(aliens))
            

plt.plot(day_ticker,alien_ticker)
print("There are " + str(len(aliens))+ " After "+str(days)+" Days When "+str(num_landed)+" landed on day 1")

plt.ylabel("Aliens")
plt.xlabel("days")
plt.grid()
plt.show()
