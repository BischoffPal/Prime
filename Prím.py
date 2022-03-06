from alive_progress import alive_bar   #                  
import xlsxwriter                      # Import
import matplotlib.pyplot as plt        # 
import time                            #


def time_convert(sec):  # Creating a function that makes run time more readable                                                   
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
  
start_time = time.time() # Start timer



def prime(tNum, prímek = []) -> bool: # Creating a functioin to find out if nummber is prime or not
    isPrime = True
    if prímek:                        # If the list of primes aren't empty
        if tNum in prímek:
            return(True)              # If the tested nummber is in the list of primes than it is a prime
        for prím in prímek:           
            if tNum % prím == 0:      
                isPrime = False
                return(False)
    if tNum == 1:                     # Adding red flags
        isPrime = False
        return(False)
    elif tNum == 2 or 3:
        return(True)
    
    for i in range(3, tNum/2, 2):     # Running W.C.S. (Worst Case Scenario) tests
        if i in prímek:
            continue
        if tNum % i == 0:
            return(False)
    if isPrime:                       # Returning the data
        return(True)
    elif isPrime == False:
        return(False)



res = 10000                           # Setting resolution 
x_cords = []                          
y_cords = []
loops = 1*10**5
prímek = []
primes = 0
with alive_bar(loops) as bar:
    for i in range(loops):
        if prime(i+1, prímek) == True:
            prímek.append(i+1)
            primes += 1
        if (i+1) % res == 0:
            y_cords.append(i+1)
            x_cords.append(primes)
            primes = 0 
        bar()

workbook = xlsxwriter.Workbook(r"prímek.xlsx")
worksheet = workbook.add_worksheet("Prímek")
worksheet.write(0, 0, "Numbers")
worksheet.write(0, 1, "Primes")
worksheet.write(loops+1, 0, "All:")
worksheet.write(loops+1, 1, len(prímek))

with alive_bar(len(prímek)) as bar2:
    for prím in prímek:
        worksheet.write(prím+1, 1, prím)
        bar2()

with alive_bar(loops) as bar3:
    for n in range(loops):
        worksheet.write(n+1,0, n)
        bar3()

workbook.close()
    


plt.plot(y_cords, x_cords)              # Setting the plot 
plt.ylabel("Primes")            
plt.xlabel("Nums")


end_time = time.time()                  # Stop timer
time_lapsed = end_time - start_time     # Calculate the runtime
time_convert(time_lapsed)               # Convert   
plt.show()                              # Show the plot