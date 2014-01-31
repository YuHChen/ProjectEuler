sum = 0 #the new term to be added
fibs = [1,2] #initial fib sequence 

#generate fibs within a value range
while (sum < 4000000):
    sum = 0
    sum = fibs[-1] + fibs[len(fibs)-2]
    fibs.append(sum)

#adjust list to get fib numbers only within the range
fibs = fibs[ : len(fibs)-1]

#debug : print list of fib numbers
print(fibs)

#limiting the list to even terms
evens = []
for i in fibs:
    if i % 2 == 0:
        evens.append(i)
        
#debug: print list of even fibs
print(evens)

sum = 0
#finding the sum
for i in evens:
    sum += i

print sum
    
