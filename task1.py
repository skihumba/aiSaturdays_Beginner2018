import random 

ourList = list()
count = 0 
while (count < 10):
    ourList.append(random.randint(1,10))
    count += 1
    
print(ourList)

#get list of rlrmrnts in ourList that are < 5
b5 = [i for i in ourList if i < 5]

print(b5)