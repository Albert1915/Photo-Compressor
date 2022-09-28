import numpy
import imageio

mtx=numpy.load('compress.npz')
size=mtx['size']
u=mtx['u']
y=mtx['y']
a=int(round(size[0]))
b=int(round(size[1]))
pic=numpy.zeros([a,b,3])

for i in range(0,3):
	aw=u[i].dot(y[i])
	for j in range(0,a):
		for k in range(0,b):
			pic[j,k,i]=round(aw[j,k])
	pic=pic.astype(numpy.uint8)

imageio.imsave('hasil.jpg',pic)
