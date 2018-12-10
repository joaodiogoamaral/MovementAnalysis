


import json
import os
import sys
import numpy
import processOutputs 


n2DKeypoints = 25
CONFIDENCE_THRESHOLD = 0.3





#outputDir = sys.argv[1]




#xCords = []
#yCords = []
#conf = []
#for loop to iterate through each json file in the directory
#input is the name of the folder from which the results should be read from
def readOutputs(outputDir):



	#pose keypoints2D are in format (x,y,c) with c being the confidence degree



	#initialize a matrix to contain all the frames
	#keypointMatrix = []

		# Result for BODY_25 (25 body parts consisting of COCO + foot)
		# const std::map<unsigned int, std::string> POSE_BODY_25_BODY_PARTS {
		#     {0,  "Nose"},
		#     {1,  "Neck"},
		#     {2,  "RShoulder"},
		#     {3,  "RElbow"},
		#    {4,  "RWrist"},
		#     {5,  "LShoulder"},
		#     {6,  "LElbow"},
		#     {7,  "LWrist"},
		#     {8,  "MidHip"},
		#     {9,  "RHip"},
		#     {10, "RKnee"},
		#     {11, "RAnkle"},
		#     {12, "LHip"},
		#     {13, "LKnee"},
		#     {14, "LAnkle"},
		#     {15, "REye"},
		#     {16, "LEye"},
		#     {17, "REar"},
		#     {18, "LEar"},
		#     {19, "LBigToe"},
		#     {20, "LSmallToe"},
		#     {21, "LHeel"},
		#     {22, "RBigToe"},
		#     {23, "RSmallToe"},
		#     {24, "RHeel"},
		#     {25, "Background"}

		#     {25, "Background"}

	keypointMatrix = {
	'nose':[],
	'neck':[],
	'rShoulder' : [],
	'rElbow' : [],
	'rWrist' : [],
	'lShoulder' : [],
	'lElbow' : [],
	'lWrist' : [],
	'midHip' : [],
	'rHip' : [],
	'rKnee' : [],
	'rAnkle' : [],
	'lHip' : [],
	'lKnee' : [],
	'lAnkle' : [],
	'rEye' : [],
	'lEye' : [],
	'rEar' : [],
	'lEar' : [],
	'lBigToe': [],
	'lSmallToe' : [],
	'lHeel' : [],
	'rBigToe' : [],
	'rRSmallToe': [],
	'RHeel' : []}


	print(outputDir)
	jsonFiles = [posJson for posJson in os.listdir(outputDir) if posJson.endswith('.json')]

	print('\nNumber of frames in video:'+str(len(jsonFiles))+'\n')


	jsonFiles.sort()

	for idx,js in enumerate(jsonFiles) :
		with open(os.path.join(outputDir,js)) as jsonFrame:
			jsonContent = json.load(jsonFrame)

			if len(jsonContent['people'])==0:
				print('\nFrame' + str(idx) +'discarded \n')
				continue

		
			keypoints = jsonContent['people'][0]['pose_keypoints_2d']
			xCords=keypoints[0:len(keypoints):3]
			yCords=keypoints[1:len(keypoints):3]
			conf=keypoints[2:len(keypoints):3]

			#discard frames where the hip cannot be identified
			if(conf[8]<CONFIDENCE_THRESHOLD):
				continue

			keypointMatrix['nose'].append((xCords[0]-xCords[8],yCords[0]-yCords[8],conf[0]))
			keypointMatrix['neck'].append((xCords[1]-xCords[8],yCords[1]-yCords[8],conf[1]))
			keypointMatrix['rShoulder'].append((xCords[2]-xCords[8],yCords[2]-yCords[8],conf[2]))
			keypointMatrix['rElbow'].append((xCords[3]-xCords[8],yCords[3]-yCords[8],conf[3]))
			keypointMatrix['rWrist'].append((xCords[4]-xCords[8],yCords[4]-yCords[8],conf[4]))
			keypointMatrix['lShoulder'].append((xCords[5]-xCords[8],yCords[5]-yCords[8],conf[5]))
			keypointMatrix['lElbow'].append((xCords[6]-xCords[8],yCords[6]-yCords[8],conf[6]))
			keypointMatrix['lWrist'].append((xCords[7]-xCords[8],yCords[7]-yCords[8],conf[7]))
			keypointMatrix['midHip'].append((0,0,conf[8]))
			keypointMatrix['rHip'].append((xCords[9]-xCords[8],yCords[9]-yCords[8],conf[9]))
			keypointMatrix['rKnee'].append((xCords[10]-xCords[8],yCords[10]-yCords[8],conf[10]))
			keypointMatrix['rAnkle'].append((xCords[11]-xCords[8],yCords[11]-yCords[8],conf[11]))
			keypointMatrix['lHip'].append((xCords[12]-xCords[8],yCords[12]-yCords[8],conf[12]))
			keypointMatrix['lKnee'].append((xCords[13]-xCords[8],yCords[13]-yCords[8],conf[13]))
			keypointMatrix['lAnkle'].append((xCords[14]-xCords[8],yCords[14]-yCords[8],conf[14]))
			keypointMatrix['rEye'].append((xCords[15]-xCords[8],yCords[15]-yCords[8],conf[15]))
			keypointMatrix['lEye'].append((xCords[16]-xCords[8],yCords[16]-yCords[8],conf[16]))
			keypointMatrix['rEar'].append((xCords[17]-xCords[8],yCords[17]-yCords[8],conf[17]))
			keypointMatrix['lEar'].append((xCords[18]-xCords[8],yCords[18]-yCords[8],conf[18]))
			keypointMatrix['lBigToe'].append((xCords[19]-xCords[8],yCords[19]-yCords[8],conf[19]))
			keypointMatrix['lSmallToe'].append((xCords[20]-xCords[8],yCords[20]-yCords[8],conf[20]))
			keypointMatrix['lHeel'].append((xCords[21]-xCords[8],yCords[21]-yCords[8],conf[21]))
			keypointMatrix['rBigToe'].append((xCords[22]-xCords[8],yCords[22]-yCords[8],conf[22]))
			keypointMatrix['rRSmallToe'].append((xCords[23]-xCords[8],yCords[23]-yCords[8],conf[23]))
			keypointMatrix['RHeel'].append((xCords[24]-xCords[8],yCords[24]-yCords[8],conf[24]))




	return processOutputs.getCoherentMatrix(keypointMatrix)
	#processOutputs.processOutputs(keypointMatrix)






	

if __name__ == "__main__":
	readOutputs();
#


































