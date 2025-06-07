import numpy as np
#Array Creation Methods
array=np.array([[1,10,3],
                [4,5,6],
                [7,8,9]])
print(np.linspace(array,10,5,axis=0,endpoint=False,retstep=True))
print((np.sort(array,axis=None)).reshape(array.shape).size)
boolean=array>4
print(array[boolean].reshape((2,3)))
print(array[[0,2,1],[0,2,2]])
print(np.multiply(array,np.arange(9).reshape((3,3))))
np.random.seed(42)
print(np.random.randint(1,10,(5,6)))
print(array.flatten())
print(np.random.choice(array.flatten(),size=3,replace=False))
print(np.concatenate((array,np.arange(6).reshape((2,3))),axis=0))
print(np.vsplit(array,3))
print(np.zeros((2,3)))





