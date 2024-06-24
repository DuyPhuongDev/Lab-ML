import numpy as np
scores = []
while 1:
    if(len(scores) == 10): break
    #x = round(np.random.uniform(0,110),2)
    x = input("enter score: ")
    if(float(x)>100):
        print("Scores greater than 100!")
        print("please enter scores again!")
    else:
        scores.append(float(x))
    
scores.sort()
print(scores)

# a.
print("Lowest score is: ", scores[0])
print("Highest score is: ", scores[9])

#b
def avgScore(scores):
    sum = 0
    for x in scores:
        sum += x
    avg = round(sum/len(scores),2)
    print("Avg of scores:", avg)

# call functrion avg
avgScore(scores)
scores.reverse()

for i in range(len(scores)-1):
    if(scores[i+1] != scores[i]):
        print("Second largest score: ", scores[i+1])
        break
    else:
        print("Not have second largest score!")


scores.reverse()
scores.pop(0)
scores.pop(0)

avgScore(scores)