


import json
import os
import sys
import numpy
import processOutputs 


n2DKeypoints = 25
outputDir = sys.argv[1]
jsonFiles = [posJson for posJson in os.listdir(outputDir) if posJson.endswith('.json')]

print('\nNumber of frames in video:'+str(len(jsonFiles))+'\n')


jsonFiles.sort()

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
		#     {25, "Background"}
#xCords = []
#yCords = []
#conf = []
#for loop to iterate through each json file in the directory

def readOutputs():

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


			keypointMatrix['nose'].append((xCords[0],yCords[0],conf[0]))
			keypointMatrix['neck'].append((xCords[1],yCords[1],conf[1]))
			keypointMatrix['rShoulder'].append((xCords[2],yCords[2],conf[2]))
			keypointMatrix['rElbow'].append((xCords[3],yCords[3],conf[3]))
			keypointMatrix['rWrist'].append((xCords[4],yCords[4],conf[4]))
			keypointMatrix['lShoulder'].append((xCords[5],yCords[5],conf[5]))
			keypointMatrix['lElbow'].append((xCords[6],yCords[6],conf[6]))
			keypointMatrix['lWrist'].append((xCords[7],yCords[7],conf[7]))
			keypointMatrix['midHip'].append((xCords[8],yCords[8],conf[8]))
			keypointMatrix['rHip'].append((xCords[9],yCords[9],conf[9]))
			keypointMatrix['rKnee'].append((xCords[10],yCords[10],conf[10]))
			keypointMatrix['rAnkle'].append((xCords[11],yCords[11],conf[11]))
			keypointMatrix['lHip'].append((xCords[12],yCords[12],conf[12]))
			keypointMatrix['lKnee'].append((xCords[13],yCords[13],conf[13]))
			keypointMatrix['lAnkle'].append((xCords[14],yCords[14],conf[14]))
			keypointMatrix['rEye'].append((xCords[15],yCords[15],conf[15]))
			keypointMatrix['lEye'].append((xCords[16],yCords[16],conf[16]))
			keypointMatrix['rEar'].append((xCords[17],yCords[17],conf[17]))
			keypointMatrix['lEar'].append((xCords[18],yCords[18],conf[18]))
			keypointMatrix['lBigToe'].append((xCords[19],yCords[19],conf[19]))
			keypointMatrix['lSmallToe'].append((xCords[20],yCords[20],conf[20]))
			keypointMatrix['lHeel'].append((xCords[21],yCords[21],conf[21]))
			keypointMatrix['rBigToe'].append((xCords[22],yCords[22],conf[22]))
			keypointMatrix['rRSmallToe'].append((xCords[23],yCords[23],conf[23]))
			keypointMatrix['RHeel'].append((xCords[24],yCords[24],conf[24]))



	processOutputs.processOutputs(keypointMatrix)



	

if __name__ == "__main__":
	readOutputs();



































