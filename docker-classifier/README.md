# docker-classifier

This contains an extremely simple (and probably **insecure & dangerous**) dockerized flask-onnx multiclassifier. It accepts base64 image json data and returns multiclass scores, from 0.0 (low) to 1.0 (high)

## To setup:

### Option 1:

Build the docker image, then deploy using docker-compose

    docker build -t interviewclassifier .
    docker-compose up

### Option 2:

Use the run.sh to do the same thing

    sh run.sh

## To Run:

Convert your image to a base64 string, and post it to:

    localhost:8080/api/classifier

Post JSON to /api/classify as application/json in the format:

    {"data": "base64_string" }

and you will get back results:
  

    {
	    "result": [
		    0.0,
		    0.0,
		    0.0,
		    8.607723510543571e-16,
		    2.4869624556107196e-19,
		    3.6599193994009065e-27,
		    7.588453480689467e-20,
		    0.0,
		    1.0
	    ],
	    "time": 0.008291482925415039
    }

Where result is a ordered list of scores per class (class 0, class 1, etc.)

	"result": [
		    class0_score,
		    class1_score,
		    class2_score,
		    class3_score,
		    class4_score,
		    class5_score,
		    class6_score,
		    class7_score,
		    class8_score
	    ]