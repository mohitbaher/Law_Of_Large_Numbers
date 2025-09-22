import random
import matplotlib.pyplot as plt
import numpy as np

print("Let's prove the law of large numbers...")
samp = ['h','t']
outcome = []
xline = []
hgraph = []
tgraph = []
head = 0
tail = 0

largeno = int(input("Enter a large number (More than 1000): "))
for count in range(1,largeno+1):
  toss = random.choice(samp)
  outcome.append(toss)
  if toss == 'h':
    head+=1
  else:
    tail +=1
  #probablitic values
  if count% 100 == 0:
    xline.append(count)
    headprob = (head/count)*100
    tailprob = (tail/count)*100
    hgraph.append(headprob)
    tgraph.append(tailprob)


print(head)
print(tail)
#print(hgraph)
#print(tgraph)
#print(outcome)
plt.plot(xline, hgraph, color='green')
plt.plot(xline, tgraph, color='red')

plt.show()