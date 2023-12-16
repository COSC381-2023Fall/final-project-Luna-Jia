from typing import Union
from fastapi import FastAPI, HTTPException
from youtube import youtube_search_reviews, get_video_description

app = FastAPI()

# Process the HTTP get request for "/"
@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/moviereviews/{movie_name}")
def get_movie_reviews(movie_name: str):
    reviews = youtube_search_reviews(movie_name)
    return reviews

@app.get("/descriptions/{video_id}")
def get_description(video_id: str):
    description = get_video_description(video_id)
    return {"video_id": video_id, "description": description}