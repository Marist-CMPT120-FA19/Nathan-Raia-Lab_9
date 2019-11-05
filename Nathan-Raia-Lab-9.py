#Nathan Raia
def main():
    maxPrime = eval(input("Enter maximum prime, I'll give you all below that one: "))
    allNums = []
    for i in range(2,maxPrime+1):
        allNums.append(i)
    while len(allNums)>0:
        aPrime = allNums.pop(0) 
        print(aPrime, "is prime!")
        for aNum in allNums:
            if aNum % aPrime == 0: 
                allNums.remove(aNum)

main()