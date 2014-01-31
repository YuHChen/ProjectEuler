<<<<<<< HEAD
threes = [] #multiples of three
fives = [] #multiples of five

#find the multiples of three and five within the given range
for i in range (1,1000):
    if (i%3) == 0 :
        threes.append(i)
    if (i%5) == 0 :
        fives.append(i)

#debug : print the lists of multiples
print("threes")
print(threes)
print("fives")
print(fives)

commonMultiples = [] #list of common multiples, no repeats

# transfers elements from threes and fives over to common multiples list while removing repeats
while ((len(threes) > 0) and (len(fives) > 0)):
    if(threes[0] < fives[0]):
        commonMultiples.append(threes[0])
        threes = threes[1:]
    elif(threes[0] == fives[0]):
        commonMultiples.append(threes[0])
        threes = threes[1:]
        fives = fives[1:]
    else:
        commonMultiples.append(fives[0])
        fives = fives[1:]

#add anything else remaining
for i in threes:
    commonMultiples.append(i)

#debug : print common multiples
print("common multiples")
print(commonMultiples)
  
total = 0  
#summing
for i in commonMultiples:
    total += i

print("sum")
print(total)
=======
for i in range (1,10):
    
>>>>>>> fa13f4d2a03d1d8dfed22c8d4284f67d135148d3
