from typing import Union
from fastapi import FastAPI
from youtube import youtube_search_reviews

app = FastAPI()

# Process the HTTP get request for "/"
@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/moviereviews/{movie_name}")
def get_movie_reviews(movie_name: str):
    reviews = youtube_search_reviews(movie_name)
    return reviews