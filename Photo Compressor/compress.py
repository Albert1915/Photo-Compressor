import numpy
import imageio
final=[]

nama=input('Masukkan nama file : ')
im=imageio.imread('{}.jpg'.format(nama))

b=min(im.shape[0],im.shape[1])
z=int(input('Masukkan nilai antara 1 sampai {} : '.format(b)))
u=numpy.zeros([3,im.shape[0],z])
y=numpy.zeros([3,z,im.shape[1]])

for n in range(0,3):
	a=im[:,:,n]

	uhm,s,v=numpy.linalg.svd(a)

	u[n,:,:]=uhm[:,:z]
	ut=u[n].transpose()
	y[n,:,:]=ut.dot(a)

numpy.savez('compress.npz',size=numpy.array(im.shape),u=u,y=y)
