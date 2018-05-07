print ('\t\t.............FIRST COME FIRST SERVE SCEDHULING..................')
fcfsque= []
total_wtime = 0
finishtime=0
totalturnaround=0

n = int(input('Enter the total no of processes: '))
for i in range(n):
    fcfsque.append([])#adding a list object to the list
    fcfsque[i].append(input('Enter process  name: '))
    print(fcfsque[i][0], end='')
    fcfsque[i].append(int(input(' arrival time: ')))
    print(fcfsque[i][0], end='')
    fcfsque[i].append(int(input(' burst time: ')))
    print ('')
    fcfsque.sort(key = lambda sjfque:sjfque[1])
  
print ('ProcessName\tArrivalTime\tBurstTime\tWaitingTime\tTurnAroundTime')
for i in range(n):
    
    finishtime+=fcfsque[i][2]
    total_wtime+=finishtime-fcfsque[i][1]-fcfsque[i][2]
    totalturnaround+=finishtime-fcfsque[i][1]
    print (fcfsque[i][0],'\t\t',fcfsque[i][1],'\t\t',fcfsque[i][2],'\t\t',finishtime-fcfsque[i][1]-fcfsque[i][2],'\t\t',finishtime-fcfsque[i][1])

print ('Total waiting time: ',total_wtime)
print ('Average waiting time: ',(total_wtime/n))
print ('Total turnaround time: ',totalturnaround)
print ('Average turnaround time: ',(totalturnaround/n))

