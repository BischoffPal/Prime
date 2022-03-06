import time
import pyautogui
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
start_time = time.time()

loops = 1*10**5
nums = []
for n in range(2, loops+1):
    nums.append(n)
badNums = []
testingNum = 2
for num in nums:
    if num in badNums:
        continue
    if testingNum not in badNums:
        for i in range(nums.index(testingNum*2), len(nums)+1, testingNum):
            try:   
                if nums[i] not in badNums:
                    badNums.append(nums[i])
            except:
                print(i)
    testingNum += 1


for badNum in badNums:
    nums.remove(badNum)

print(nums)

with open('VaterPrím_v2.0.txt','w') as f:
    for num in nums:
        f.write(str(num))
        f.write("\n")


end_time = time.time()
time_lapsed = end_time - start_time
time_convert(time_lapsed)
