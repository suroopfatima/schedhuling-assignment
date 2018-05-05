print ('\t\t.............SHORTEST JOB FIRST SCEDHULING..................')
sjfque= []
total_wtime = 0
finishtime=0
totalturnaround=0
btime=0
k=0
tempat=tempbt=0
temppname=''
k=1
n = int(input('Enter the total no of processes: '))
for i in range(n):
    sjfque.append([])#adding a list object to the list
    sjfque[i].append(input('Enter process  name: '))
    print(sjfque[i][0], end='')
    sjfque[i].append(int(input(' arrival time: ')))
    print(sjfque[i][0], end='')
    sjfque[i].append(int(input(' burst time: ')))
    print ('')
    sjfque.sort(key = lambda sjfque:sjfque[1])
for j in range(n):
    btime+=sjfque[j][2]
    int( minn=sjfque[k][2])
    for i in range (k,n):
      if btime>=sjfque[i][1] and sjfque[i][2]<minn:
          temppname=sjfque[k][0]
          sjfque[k][0]=sjfque[i][0]
          sjfque[i][0]=temppname
          tempat=sjfque[k][1]
          sjfque[k][1]=sjfque[i][1]
          sjfque[i][1]=tempat
          tempbt=sjfque[k][2]
          sjfque[k][2]=sjfque[i][2]
          sjfque[i][2]=tempbt
    
    k+=1          
print ('ProcessName\tArrivalTime\tBurstTime\tWaitingTime\tTurnAroundTime')
for i in range(n):
    
    finishtime+=sjfque[i][2]
    total_wtime+=finishtime-sjfque[i][1]-sjfque[i][2]
    totalturnaround+=finishtime-sjfque[i][1]
    print (sjfque[i][0],'\t\t',sjfque[i][1],'\t\t',sjfque[i][2],'\t\t',finishtime-sjfque[i][1]-sjfque[i][2],'\t\t',finishtime-sjfque[i][1])

print ('Total waiting time: ',total_wtime)
print ('Average waiting time: ',(total_wtime/n))
print ('Total turnaround time: ',totalturnaround)
print ('Average turnaround time: ',(totalturnaround/n))

