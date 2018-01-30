import numpy as np
a = np.random.random_integers(0,100 ,15)
print(a)
mx = max(a)
print('maximum value : ',mx)
for i in range(len(a)):
    if a[i] == mx :
        a[i] = 100
        print('max value position is : ',i+1)
print(a)

