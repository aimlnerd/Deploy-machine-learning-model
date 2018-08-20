# Dockerize and deploy machine learning model as REST API using Flask
A simple Flask application that can serve predictions machine learning model. Reads a pickled sklearn model into memory when the Flask app is started and returns predictions through the /predict endpoint. You can also use the /train endpoint to train/retrain the model.

1. ### Install PIP requirements 
    ```
    pip install -r requirements.txt
    ```
2. ### Running API

    ```
    python main.py <port>
    ```

3. ### Endpoints
    ### /predict (POST)
    Returns an array of predictions given a JSON object representing independent variables. Here's a sample input:
    ```
    [
        {"Age": 14, "Sex": "male", "Embarked": "S"},
        {"Age": 68, "Sex": "female", "Embarked": "C"},
        {"Age": 45, "Sex": "male", "Embarked": "C"},
        {"Age": 32, "Sex": "female", "Embarked": "S"}
    ]
    ```
    
    and sample output:
    ```
    {"prediction": [0, 1, 1, 0]}
    ```
    
    
    ### /train (GET)
    Trains the model. This is currently hard-coded to be a random forest model that is run on a subset of columns of the titanic dataset.
    
    ### /wipe (GET)
    Removes the trained model.

the step by step flow is as follows:

1. Install Flask
2. Serialise your model (this can be done using Pickle, or JobLib)
3. [optional] Serialise your columns
4. Create a separate [insert name here].py file in the same directory as your serialised model, which will build the web service using Flask
5. Run [insert name here].py file from terminal/command line
6. Go to http address to check if its working
7. Make a http POST call with some data, and receive the prediction back.

# Docker commands
# docker build
# docker build -t <app name> .

# docker run
# docker run ml_app -p 9999 # to make the port externally avaiable for browsers

# show all running containers
# docker ps

# Kill and remove running container
# docker rm <containerid> -f

# open bash in a running docker container
# docker exec -ti <containerid> bash

# docker compose
# run and interact between multiple docker containers

Appendix
- http://docs.python-requests.org/en/latest/index.html
- https://www.ibm.com/developerworks/webservices/library/ws-restful/
- https://blog.hyperiondev.com/index.php/2018/02/01/deploy-machine-learning-model-flask-api/
- https://medium.com/@amirziai/a-flask-api-for-serving-scikit-learn-models-c8bcdaa41daa