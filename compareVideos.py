

import processOutputs
import ReadOutput
import os,os.path
import sys
import numpy
import matplotlib.pyplot as plt



def compareVideos(vid1,vid2):

	print(vid1,vid2)

	vid1Matrix = ReadOutput.readOutputs(vid1)
	vid2Matrix = ReadOutput.readOutputs(vid2)

	plane1 = processOutputs.getPlane(vid1Matrix)
	plane2 = processOutputs.getPlane(vid2Matrix)

	if( plane1 != plane2 ):
		print("Videos not in the same plane, makes no sense to compare them!!!\n")
		sys.exit(1)


	if( plane1=="right" or plane1 =="front" or "back"):
		[kneeX1,kneeY1] = processOutputs.extractEquations(vid1Matrix['rKnee'])
		[kneeX2,kneeY2] = processOutputs.extractEquations(vid2Matrix['rKnee'])
		plotMovements(kneeY1,kneeY2,'Right Knee Y Position')
	else:
		[kneeX1,kneeY1] = processOutputs.extractEquations(vid1Matrix['lKnee'])
		[kneeX2,kneeY2] = processOutputs.extractEquations(vid2Matrix['lKnee'])
		plotMovements(kneeY1,kneeY2,'Left Knee Y Position')











#inputs are the x or y positions across the video and the name of the keypoint and coordinate (x,y)
def plotMovements(x1,x2,title):


	t1 = xrange(len(x1))
	t2 = xrange(len(x2))
	

	plt.figure(1)
	plt.plot(t1,x1,'x',t2,x2,'+')

	plt.show()



if __name__ == "__main__":
	
	compareVideos(sys.argv[1],sys.argv[2]);