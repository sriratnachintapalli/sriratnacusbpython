multiply = 1
values = [8,16,22,12,41]
n = len(values)

for i in values:
    multiply = (multiply)*(i)

geometric_mean = (multiply)**(1/n)
print ('The Geometric Mean is: ' + str(geometric_mean)) 
