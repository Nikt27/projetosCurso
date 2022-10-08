import math
cat1 = (int(input('Digite o primeiro cateto: ')))
cat2 = (int(input('Digite o segundo cateto: ')))
preHipoten = ((cat1**2)+(cat2**2))
hipoten = (math.sqrt(preHipoten))
print (hipoten)
print (round(hipoten, 2))