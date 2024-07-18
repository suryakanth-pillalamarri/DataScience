Open your terminal, navigate to the directory containing your Dockerfile, and run the following command to build the Docker image:

docker build -t fastapi-breast-cancer-app .


Step 4: Run the Docker Container
Once the image is built, you can run the container with the following command:

docker run -d -p 8000:8000 fastapi-breast-cancer-app



You can now test your API by sending a request to http://127.0.0.1:8000/predict using Postman or any other HTTP client.
