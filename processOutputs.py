
#includes

from scipy.interpolate import interpolate,interp1d,splev,splrep
import matplotlib.pyplot as plt
import numpy as np
import peakutils as pk 

CONFIDENCE_THRESHOLD = 0.5
INTERPOLATION_ORDER = 10#10
SQUAT_THRESHOLD = 0.2
N_PTS = 100 #Number of points for time vectors


#input is a dictionary where each entry is a list of tupples with the size of nFrames
def processOutputs(keypointMatrix):


	#this loop discards frames where the keypoint could not be identified with a certain confidence
	for i in keypointMatrix.keys():
		keypointMatrix[i] = [x for x in keypointMatrix[i] if checkFrameConfidenceOk(x)]
		



	plane = getPlane(keypointMatrix) #according to the plane, search for references in a certain folder 

	if(plane == "error"):
		print("The point of view could not be identified!\n")
		exit(1)
	elif(plane == "front"):
		print("Front plane!\n")
		#search in frontplane models
	elif(plane == "left"):
		print("Left plane")    
		#search in leftplane models
	elif(plane == "right"):
		print("Right plane")




	#analyze movement for the knees
	if( plane=="right" or plane =="front" or "back"):
		#[kneeX,kneeY] = extractEquations(keypointMatrix['rKnee'])
		[kneeX,kneeY,time] = extractEquationsNorm(keypointMatrix['rKnee'])
	else:
		#[kneeX,kneeY] = extractEquations(keypointMatrix['lKnee'])
		[kneeX,kneeY,time] = extractEquationsNorm(keypointMatrix['lKnee'])

	squats=checkSquats(kneeY)

	
	print("You performed %d squats!\n" % (squats))
	

	print(autocorr(kneeY))









	
	


#this function identifies the movement according to the plane from which the video was recorded
def checkSquats(kneeY):
	
	kneeY = [ -x for x in kneeY]
	squatCount = 0

	indexes = pk.peak.indexes(kneeY,thres=SQUAT_THRESHOLD)
	#debug
	print(indexes)
	for i in indexes:
		if( kneeY[i] > 0.1):
			squatCount+=1
	#plot data
	
	return squatCount


def autocorr(x):
    result = np.correlate(x, x, mode='full')
    return result[result.size/2:]



# this functions extracts items (tuples) from the dictionary entries when the respective confidence is below a treshold.
# Besides, if a certain tupple contains an empty value, delete it too

def getCoherentMatrix(keypointMatrix):
		#this loop discards frames where the keypoint could not be identified with a certain confidence
	for i in keypointMatrix.keys():
		keypointMatrix[i] = [x for x in keypointMatrix[i] if checkFrameConfidenceOk(x)]


	return keypointMatrix

def checkFrameConfidenceOk(keypointFrame):
	
	if(keypointFrame[2]<CONFIDENCE_THRESHOLD):
		return False
	return True




#function that extracts the plane from which the video was filmed
#returns a string: "front", "lSide", "rSide", "error" , the last one for cases where the  
def getPlane(keypointMatrix):
	
	

	if( len(keypointMatrix['lEar']) > 0 and len(keypointMatrix['rEar']) > 0):
		if(len(keypointMatrix['nose'])!=0):
			return "front"
		else:
			return "back"

	elif  len(keypointMatrix['lEar']) > 0:
		return "left"
	elif len(keypointMatrix['rEar']) > 0:
		return "right"
	else:
		return "error"





	return False;

#input to this function is a list of tupples for a certain keypoint
def extractEquations(keypointPositions):
	time = xrange(len(keypointPositions))

	y = []
	x = []
	for i in keypointPositions:
		
		y.append(i[1])
		x.append(i[0])






	print('\n\n\n')	

	yCoeffs = np.poly1d(np.polyfit(time,y,INTERPOLATION_ORDER))
	xCoeffs = np.poly1d(np.polyfit(time,x,INTERPOLATION_ORDER))	
	#tck = splrep(time, y, s=0)
	#yCubic = interp1d(time, y, kind='cubic')
	#ySpline = splev(time, tck, der=0)




	#plt.figure(1)
	#plt.plot(time,y,'x',time,yCoeffs(time),'r',time,yCubic(time),'--',time,ySpline)
	#plt.plot(time,-yCoeffs(time),'--')

	#plt.show()

	return [xCoeffs(time),yCoeffs(time)]



#input to this function is a list of tupples for a certain keypoint
def extractEquationsNorm(keypointPositions):
	

	time = np.linspace(0,len(keypointPositions),N_PTS)
	tInt = xrange(len(keypointPositions)) #time vector for interpolation

	y = []
	x = []
	for i in keypointPositions:
		
		y.append(i[1])
		x.append(i[0])

	print('\n\n\n')	

	yCoeffs = np.poly1d(np.polyfit(tInt,y,INTERPOLATION_ORDER))
	xCoeffs = np.poly1d(np.polyfit(tInt,x,INTERPOLATION_ORDER))	
	



	return [xCoeffs(time),yCoeffs(time),time]

# jointPositions is a list of tuples and the key name!

#def computeMovement(jointPositions,jointName):
	
#	frames = xrange(len(jointPositions))
#	x = []
#	y = []

#	for i in jointPositions:
#		x.append(i[0])
#		y.append(i[1])


	#plot results
#	plt.figure(1)
#	plt.plot(frames,x,'b')
	#plt.axis([-0.05, 6.33, -1.05, 1.05])
#	plt.title(jointName+'x')
#	plt.show()

#	plt.figure(2)
#	plt.plot(frames,y,'r')
#	plt.title(jointName+'y')
#	plt.show()
	














