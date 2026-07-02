# CAR WASH SIMULATOR
import random
print("=====CAR WASH SIMULATOR=====")
print()
# Inputs
def ask_number(question):
    while True:
        try:
            return int(input(question))
        except:
            print("Please type a whole number, like 4")
ArrivalRate = ask_number("How fast do cars arrive? (Every X Minutes) ")
ServiceTime = ask_number("How fast do you wash cars? (In X minutes) ")
Bays = ask_number("How many bays do you want? (X many bays) ")
ShiftTime = ask_number("How long should the simulation last? (For X minutes) ")
Days = ask_number("How many times should the simulation run? (X times) ")
MaxLine = ask_number("What is the longest line before people give up? (X cars) ")


# Main Script
def run_day():
    BayFreeAt = [0] * Bays
    Queue = 0
    CarsWashed = 0
    MaxQueue = 0
    TotalWait = 0
    CarsArrived = 0
    AverageWait = 0
    TurnedAway = 0
    # print("-----SHIFT START-----")
    for Minute in range(ShiftTime):
        # print(Minute)
        for b in range(Bays):
            if Minute == BayFreeAt[b] and Minute > 0: 
                CarsWashed += 1
                # print("A wash finished at minute: " + str(Minute))
        if Queue < MaxLine:
            if random.random() < 1 / ArrivalRate:
                Queue += 1 
                # print("1 car joins the line. Queue: " + str(Queue))
                CarsArrived += 1
                if Queue > MaxQueue:
                    MaxQueue = Queue  
            else:
                TurnedAway += 1 
        for b in range(Bays):  
            if Minute >= BayFreeAt[b] and Queue > 0:
                Queue -= 1
                BayFreeAt[b] = Minute + random.randint(ServiceTime-2, ServiceTime+2)
                # print("A wash has started. Queue: " + str(Queue))
        TotalWait += Queue
    AverageWait = TotalWait/CarsArrived
    return CarsWashed, MaxQueue, AverageWait



# Aftermath
TotalWashed = 0
TotalWait = 0
WorstQueue = 0
for i in range(Days):
      CarsWashed, MaxQueue, AverageWait = run_day()
      TotalWashed += CarsWashed
      TotalWait += AverageWait
      if MaxQueue > WorstQueue:
          WorstQueue = MaxQueue
AvgWashed = TotalWashed / Days
AvgWaitOverall = TotalWait / Days
print("-----SIMULATION RESULTS-----")
print("Cars washed: " + str(round(AvgWashed)) + " cars.")
print("Max length of cars waiting: " + str(WorstQueue) + " cars in line.")
print("The average wait time of cars was: " + str(round(AvgWaitOverall,1)) + " minutes.")