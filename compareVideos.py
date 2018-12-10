

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


def compareVideos(vid1,vid2):

	

	vid1Matrix = ReadOutput.readOutputs(vid1)
	vid2Matrix = ReadOutput.readOutputs(vid2)

	plane1 = processOutputs.getPlane(vid1Matrix)
	plane2 = processOutputs.getPlane(vid2Matrix)

	if( plane1 != plane2 ):
		print("Videos not in the same plane, makes no sense to compare them!!!\n")
		sys.exit(1)

	else:
		print(plane1)




	if( plane1=="right" or plane1 =="front" or "back"):
		
		[kneeX1,kneeY1,t1] = processOutputs.extractEquationsNorm(vid1Matrix['rKnee'])
		
		[kneeX2,kneeY2,t2] = processOutputs.extractEquationsNorm(vid2Matrix['rKnee'])
		
		plotMovementsNorm(kneeY1,kneeY2,t1,t2)




	else:

		[kneeX1,kneeY1,t1] = processOutputs.extractEquationsNorm(vid1Matrix['lKnee'])

		[kneeX2,kneeY2,t2] = processOutputs.extractEquationsNorm(vid2Matrix['lKnee'])

		plotMovementsNorm(kneeY1,kneeY2,t1,t2)



	sim = getSimilarity(kneeY1,kneeY2)

	print(sim)



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
	
	compareVideos(sys.argv[1],sys.argv[2]);