# FastAPI Project Guide

###### This project is built using FastAPI, a modern, fast web framework for building APIs with Python.

#### Follow the following steps to run the project:

1. download the project to your machine
`git clone git@github.com:COSC381-2023Fall/final-project-Luna-Jia.git`

2. at the project directory, create vertual enviroment
`python3 -m venv .venv`

3. run vertual enviroment
`source .venv/bin/activate`

4. make sure pip is pointing to the right path
`which pip`

5. To install the dependencies in batch(set up a virtual environement), run the command:
	`python3 -m pip install -r requirements.txt`

6. To run the fast API application, use the following command:
`uvicorn main:app --reload`

7. In the browser, go to [http://127.0.0.1:8000](http://127.0.0.1:8000), the webpage will return a JSON response:
 `{"Hello": "world"}`

8. Run test, in termial, type `pytest --cov=.`

9. run `youtube.py` to see 10 reviews for movie "Inception", in terminal, type:
`python youtube.py "Inception"`

10. To run the fast API application, and search for 10 reviews/comments for a movie, in the web browser, type:`http://127.0.0.1:8000/moviereviews/<movie name>`. For example, to search reviews for movie Inception, go to: 
[http://127.0.0.1:8000/moviereviews/Inception](http://127.0.0.1:8000/moviereviews/Inception)

11. To retrieve the description of a specific video by its ID, in terminal, type:
`python youtube.py --description "VIDEO_ID"`

12. To test for different API endpoints, go to [FastAPI Doc](http://127.0.0.1:8000/docs) in your browser.

