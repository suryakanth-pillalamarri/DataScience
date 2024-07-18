# DataScience

docker image was created and uploaded to docker hub
 to pull the image from docker hub repo
 login to docker by giving below command
   docker login

   then pull the the image by below command
    docker pull srivenkatesasrinivasagovindha/datasceiencelearningrepo:v3

  then run the container by below command
    docker run -d -p 8000:8000 --name svmfastapimodel imageid

  hit the url http://0.0.0.0:8000/predict    with below data as json will work fine

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
