import time
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
start_time = time.time()


lastRound = False
laps = 1*10**4
nums = []
for i in range(2, laps, 2):
    nums.append(i+1)

nCount = 0
testingNum = nums[nCount]
testedIndex = nums[nCount+1]
while testingNum != nums[-1]:
    
    lastRound = False
    if testedIndex == nums[-1]:
        lastRound = True
    
    if testedIndex % testingNum == 0:
        try:
            nums.remove(testedIndex)
        except:
            pass
        
    if lastRound:
        print("lastRound")
        nCount += 1
        testingNum = nums[nCount]
        try:
            testedIndex = nums[nCount+1]
        except:
            print("Done!")
    else:
        testedIndex += 1


with open('VaterPrím.txt','w') as f:
    for num in nums:
        f.write(str(num))
        f.write("\n")

print(nums)
end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)

        

