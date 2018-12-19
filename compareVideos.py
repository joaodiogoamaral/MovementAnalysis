

import processOutputs
import ReadOutput
import os,os.path
import sys
import numpy
import matplotlib.pyplot as plt
#from sklearn.metrics.pairwise import cosine_similarity
#from scipy.spatial.distance import cdist
from numpy import dot
from numpy.linalg import norm

#array of directories
def compareVideos(args):

	planes = []
	vidMatrix = []
	for i in args:
		print i
		output=ReadOutput.readOutputs(i)
		vidMatrix.append(output)
		plane=processOutputs.getPlane(output)
		planes.append(plane)


	if(len(set(planes))>1):
		print("Videos not in the same plane, makes no sense to compare them!!!\n")
		sys.exit(1)	
	print(set(planes))
	eqMatrix=[]

	for j in vidMatrix:
	

		if(set(plane)=="right" or set(plane) =="front" or set(plane)=="back"):
			title='rKnee Y position'
			#output of extractEquations is [xCoeffs(time),yCoeffs(time),time]
			[x,y,t]=processOutputs.extractEquationsNorm(j['rKnee'])
			#title='rWrist Y position'
			#[x,y,t]=processOutputs.extractEquationsNorm(j['rWrist'])
		else:
			title='lKnee Y position'
			#output of extractEquations is [xCoeffs(time),yCoeffs(time),time]
			[x,y,t]=processOutputs.extractEquationsNorm(j['lKnee'])
			#title='lWrist Y position'
			#[x,y,t]=processOutputs.extractEquationsNorm(j['lWrist'])

		eqMatrix.append([x,y,t])
	

	print(len(eqMatrix))

	plotEqMatrix(eqMatrix,title)
	getSimilarityMatrix(eqMatrix)


def plotEqMatrix(eqMatrix,title):
	

	plt.figure(1)
	plt.title(title)

	#output of extractEquations is [xCoeffs(time),yCoeffs(time),time]
	for num,eq in enumerate(eqMatrix):
		plt.plot(eq[2],eq[1],label=str(num+1))




	plt.legend()
	plt.show()
	

def getSimilarityMatrix(eqMatrix):

	for i in xrange(len(eqMatrix)):
		if(i<len(eqMatrix)):
			for x in xrange(i+1,len(eqMatrix)):
				print('similarity between videos '+str(i+1)+' and '+str(x+1)+':'+str(getSimilarity(eqMatrix[i][1],eqMatrix[x][1])))



#the input is two numeric vectors to get the similarity
def getSimilarity(a,b):

	#print(len(x1))
	#print(len(x2))
	#if(len(x1) > len (x2)):
	#	a=numpy.pad(x2,(0,len(x1)-len(x2)),'constant') 
	#	b=x1
	#else:
	#	a=x2
	#	b=numpy.pad(x1,(0,len(x2)-len(x1)),'constant') 
	

	cosSim = dot(a, b)/(norm(a)*norm(b)) 

	return cosSim





#inputs are the x or y positions across the video and the name of the keypoint and coordinate (x,y)
def plotMovements(x1,x2,title,vid1,vid2):


	t1 = xrange(len(x1))
	t2 = xrange(len(x2))
	
	

	plt.figure(1)
	plt.plot(t1,x1,'b',label = 'Video 1')
	plt.plot(t2,x2,'g',label = 'Video 2')
	plt.legend()
	plt.show()


#similar to plotMovements but receives a time vector from the caller	
def plotMovementsNorm(x1,x2,t1,t2):
	

	plt.figure(1)
	plt.plot(t1,x1,'b',label = 'Video 1')
	plt.plot(t2,x2,'g',label = 'Video 2')
	plt.legend()
	plt.show()
	


if __name__ == "__main__":
	
	print(sys.argv)
	compareVideos([sys.argv[x] for x,value in enumerate(sys.argv) if x > 0 ])