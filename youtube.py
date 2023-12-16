#!/usr/bin/python
import sys
import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = config.API_KEY
TRANSLATE_DEVELOPER_KEY = config.TRANSLATE_API_KEY

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

# Function to translate text using Google Translate
def translate_text(text, target_language):
    translate_service = build('translate', 'v2', developerKey=TRANSLATE_DEVELOPER_KEY)
    translation = translate_service.translations().list(source='en', target=target_language, q=[text]).execute()
    return translation['translations'][0]['translatedText']

# Function to search for YouTube reviews in a specific language
def youtube_search_reviews(query_term, target_language='en', max_results=10):
    # Only translate if the target language is different from the source language
    translated_term = query_term if target_language == 'en' else translate_text(query_term, target_language)
    
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    search_response = youtube.search().list(
        q=f"{translated_term} review|commentary",
        part='id,snippet',
        maxResults=max_results,
        type='video',
        order='relevance'
    ).execute()

    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append({
                'videoId': search_result['id']['videoId'],
                'title': search_result['snippet']['title'],
                'description': search_result['snippet']['description']
            })

    return videos

# Function to get the description of a YouTube video
def get_video_description(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
    video_response = youtube.videos().list(
        id=video_id,
        part='snippet',
        maxResults=1
    ).execute()

    video_description = video_response.get('items', [{}])[0].get('snippet', {}).get('description', '')
    return video_description

# Command-line interface for the script
if __name__ == '__main__':

    if sys.argv[1] == '--description':
        
        video_id = sys.argv[2]
        print(get_video_description(video_id))
    else:
        query_term = sys.argv[1]
        target_language = sys.argv[2] if len(sys.argv) > 2 else 'en'
        review_videos = youtube_search_reviews(query_term, target_language)
        for video in review_videos:
            print(f"Video ID: {video['videoId']}")
            print(f"Title: {video['title']}")
            print(f"Description: {video['description']}\n")

