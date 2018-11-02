



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



cd ../openpose/

./build/examples/openpose/openpose.bin --video $VIDEO_ABS_PATH --write_json $OUTPUT_DIR


cd $SCRIPT_DIR

#execute python program to process outputs

python ReadOutput.py $OUTPUT_DIR






