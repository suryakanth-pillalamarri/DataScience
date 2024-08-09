Open your terminal, navigate to the directory containing your Dockerfile, and run the following command to build the Docker image:

docker build -t fastapi-breast-cancer-app .


Step 4: Run the Docker Container
Once the image is built, you can run the container with the following command:

docker run -d -p 8000:8000 fastapi-breast-cancer-app



now give the below command for getting ipaddress
>hostname -I

replace the first ip address from the output and place it in the postman url and senf the request

like below

http://172.25.27.53:8000/predict

with tbelow data

{
    "concave_points_worst": 0.3,
    "perimeter_worst": 150.0,
    "concave_points_mean": 0.1,
    "radius_worst": 25.0,
    "perimeter_mean": 85.0,
    "area_worst": 2000.0,
    "radius_mean": 14.0,
    "area_mean": 700.0,
    "concavity_mean": 0.2,
    "concavity_worst": 0.3
}

You can now test your API by sending a request to http://127.0.0.1:8000/predict using Postman or any other HTTP client.
