#using the official python image from the Docker HUB
FROM python:3.9-slim

#setting the work directory in the container
WORKDIR /app


#copying the requiremets file into the container
COPY requirements.txt .

#installing the dependencies

RUN pip install --no-cache-dir -r requirements.txt


#copy the rest of the application code into the container

COPY . .

# expose the port that app runs on

EXPOSE 8000


# command to run the application
CMD [ "uvicorn","fastapiapp:app","--host","0.0.0.0","--port","8000" ]
