



SCRIPT_DIR=$(pwd)

OUTPUT_DIR="$(pwd)/output/"


FLAG=$1 	#flag can be --compare(compare 2 vids), --store (store a model) , or --check(to check a certain video among the models)



#RUN OPEN POSE
#KEYPOINT SCALE:
# 0 to scale it to the original source resolution; 
# 1 to scale it to the net output size (set with net_resolution); 
# 2 to scale it to the final output size (set with resolution);
# 3 to scale it in the range [0,1], where (0,0) would be the top-left corner of the image, and (1,1) the bottom-right one; 
# 4 for range [-1,1], where (-1,-1) would be the top-left corner of the image, and (1,1) the bottom-right one. 


runOpenPose()
{
	cd ../openpose/

	./build/examples/openpose/openpose.bin --video $1 --write_json $2 --keypoint_scale 4


	cd $SCRIPT_DIR
}


#execute python program to process outputs










clearOutput() 
	{
		if [ ! -z "$(ls -a $OUTPUT_DIR)" ]
		then
			printf "\nCleaning previous output data...\n"
			rm -rf output/*
		fi
	}

checkVideoExists ()
	{
		if [ ! -f $1 ]
		then
			printf "Could not find video!!! \n"
			exit 1
		fi 
	}




#test input arguments

case "$1" in

	--compare)
		ARG=""
		if [ "$#" -lt 2 ]; then
    		echo "USAGE: ./CrossMotionOP.sh --compare <PathToVideo1> <PathToVideo1> ... (as many as you want to compare)\n"
    		exit 1
		fi
		rm -rf temp  
		mkdir temp #temporary directory to store json files with 

		for ((i=2;i<=$#;i++)); 
		do
			mkdir temp/vid$((i-1))
			VIDEO_RELATIVE_PATH=${!i}
			echo $VIDEO_RELATIVE_PATH

			VIDEO_ABS_PATH="$(pwd)/$VIDEO_RELATIVE_PATH"
			checkVideoExists $VIDEO_ABS_PATH
			OUTPUT_DIR="$(pwd)/temp/vid$((i-1))"
			runOpenPose $VIDEO_ABS_PATH $OUTPUT_DIR
			ARG="$ARG $OUTPUT_DIR"
		done

		
		

		
		

		echo $ARG

		python compareVideos.py $ARG 

		#



		exit 0
		;;

	--store)
		
		if [ "$#" -ne 3 ]; then
    		echo "USAGE: ./CrossMotionOP.sh --store <PathToVideo> <exercise>\n"
    		exit 1
		fi

		VIDEO_RELATIVE_PATH=$2
		EXERCISE=$3

		clearOutput
		VIDEO_ABS_PATH="$(pwd)/$VIDEO_RELATIVE_PATH"
		checkVideoExists $VIDEO_ABS_PATH

		runOpenPose



		python storeModel.py $OUTPUT_DIR $EXERCISE


		;;










	--check)
		echo "to be implemented!!!\n"
		exit 0  ;;

	*) 
	echo "Incorrect Flags!!!\n"
	exit 1 ;;


esac

#if [ "$#" -ne 1 ]; then
 #   echo "Illegal number of parameters"
#fi


#VIDEO_RELATIVE_PATH=$1

#if [ -z "$VIDEO_RELATIVE_PATH" ]
#then
#	printf "USAGE: ./CrossMotionOP.sh <PathToVideo> \n"
#	exit
#fi



#OUTPUT_DIR="$(pwd)/output/"

#check if output directory is empty and clean outputs







VIDEO_ABS_PATH="$(pwd)/$VIDEO_RELATIVE_PATH"







