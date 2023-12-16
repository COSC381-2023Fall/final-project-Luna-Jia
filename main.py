from typing import Union
from fastapi import FastAPI, HTTPException
from youtube import youtube_search_reviews, get_video_description, translate_text

app = FastAPI()

# Process the HTTP get request for "/"
@app.get("/")
def read_root():
    return {"Hello": "world"}

@app.get("/moviereviews/{movie_name}")
def get_movie_reviews(movie_name: str):
    reviews = youtube_search_reviews(movie_name)
    return reviews

@app.get("/moviereviews/{language}/{movie_name}")
def get_movie_reviews_by_language(language: str, movie_name: str):
    # Translate the movie name into the target language
    translated_movie_name = translate_text(movie_name, language)
    # Get reviews in the specified language
    reviews = youtube_search_reviews(translated_movie_name, language)
    return reviews

@app.get("/descriptions/{video_id}")
def get_description(video_id: str):
    description = get_video_description(video_id)
    return {"video_id": video_id, "description": description}
