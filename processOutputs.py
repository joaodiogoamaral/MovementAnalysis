
#includes

from scipy.interpolate import interpolate
import matplotlib.pyplot as plt
import numpy as np

CONFIDENCE_THRESHOLD = 0.3




#input is a dictionary where each entry is a list of tupples with the size of nFrames
def processOutputs(keypointMatrix):

	for i in keypointMatrix.keys():
		keypointMatrix[i] = [x for x in keypointMatrix[i] if checkFrameConfidenceOk(x)]

	getPlane(keypointMatrix)	
		#for frame in i:
			#if not all(frame):
				#print(frame)
				#del frame
				#note: should i eliminate all the entries regarding that frame? ?? 







# this functions extracts items (tuples) from the dictionary entries when the respective confidence is below a treshold.
# Besides, if a certain tupple contains an empty value, delete it too
def checkFrameConfidenceOk(keypoinFrame):
	
	if(keypoinFrame[2]<CONFIDENCE_THRESHOLD):
		return False
	return True




#function that extracts the plane from which the video was filmed
#returns a string: "front", "lSide", "rSide", "error" , the last one for cases where the  
def getPlane(keypointMatrix):
	
	

	if( len(keypointMatrix['lEar']) > 0 and len(keypointMatrix['rEar']) > 0):
		print("\nFront plane\n")
	elif  len(keypointMatrix['lEar']) > 0:
		print("\nLeft plane\n")
	elif len(keypointMatrix['rEar']) > 0:
		print("\nRight plane\n")
	else:
		print("Other Plane")





	return False;







# jointPositions is a list of tuples and the key name!

def computeMovement(jointPositions,jointName):
	
	frames = xrange(len(jointPositions))
	x = []
	y = []

	for i in jointPositions:
		if(i[2]<CONFIDENCE_THRESHOLD):
			del(i)
			continue

		x.append(i[0])
		y.append(i[1])


	#plot results
	plt.figure()
	plt.plot(frames,x,'b',frames,y,'r')
	#plt.axis([-0.05, 6.33, -1.05, 1.05])
	plt.title(jointName)
	plt.show()
	














