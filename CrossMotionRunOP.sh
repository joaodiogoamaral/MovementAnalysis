



SCRIPT_DIR=$(pwd)

VIDEO_RELATIVE_PATH=$1

if [ -z "$VIDEO_RELATIVE_PATH" ]
then
	printf "USAGE: ./CrossMotionOP.sh <PathToVideo> \n"
	exit
fi



OUTPUT_DIR="$(pwd)/output/"

#check if output directory is empty and clean outputs



if [ ! -z "$(ls -a $OUTPUT_DIR)" ]
then
	printf "\nCleaning previous output data...\n"
	rm -rf output/*
fi



VIDEO_ABS_PATH="$(pwd)/$VIDEO_RELATIVE_PATH"




if [ ! -f $VIDEO_ABS_PATH ]
then
	printf "Could not find video!!! \n"
	exit 1
fi 



#RUN OPEN POSE
#KEYPOINT SCALE:
# 0 to scale it to the original source resolution; 
# 1 to scale it to the net output size (set with net_resolution); 
# 2 to scale it to the final output size (set with resolution);
# 3 to scale it in the range [0,1], where (0,0) would be the top-left corner of the image, and (1,1) the bottom-right one; 
# 4 for range [-1,1], where (-1,-1) would be the top-left corner of the image, and (1,1) the bottom-right one. 

cd ../openpose/

./build/examples/openpose/openpose.bin --video $VIDEO_ABS_PATH --write_json $OUTPUT_DIR


cd $SCRIPT_DIR

#execute python program to process outputs

python ReadOutput.py $OUTPUT_DIR






