from math import sqrt                  # 
import matplotlib.pyplot as plt        # Import
import time                            #




def time_convert(sec):  # Creating a function that makes run time more readable                                                   
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
  
start_time = time.time() # Start timer



def prime(tNum, prímek = []) -> bool: # Creating a functioin to find out if nummber is prime or not
    if prímek:                        # If the list of primes aren't empty
        if tNum in prímek:
            return(True)              # If the tested nummber is in the list of primes than it is a prime
        for prím in prímek:           
            if tNum % prím == 0:      
                return(False)
    if tNum == 1:                     # Adding red flags
        return(False)
    elif tNum == 2 or 3:
        return(True)
    
    for i in range(3, int(sqrt(tNum))+1, 2):     # Running W.C.S. (Worst Case Scenario) tests
        if i in prímek:
            continue
        if tNum % i == 0:
            return(False)
    



res = 100                         # Setting resolution 
x_cords = []                          
y_cords = []
loops = 1*10**6
prímek = []
primes = 0

for i in range(3, loops, 2):
    if prime(i, prímek) == True:
        prímek.append(i)
        primes += 1
    


end_time = time.time()                  # Stop timer
time_lapsed = end_time - start_time     # Calculate the runtime
time_convert(time_lapsed)               # Convert   
plt.show()                              # Show the plot

