#!/usr/bin/python
import sys
import config
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

DEVELOPER_KEY = config.API_KEY
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search_reviews(query_term, max_results=10):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=f"{query_term} review|commentary",
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

def get_video_description(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    video_response = youtube.videos().list(
        id=video_id,
        part='snippet',
        maxResults=1
    ).execute()

    video_description = video_response.get('items', [{}])[0].get('snippet', {}).get('description', '')
    return video_description

if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '--description':
        video_id = sys.argv[2]
        print(get_video_description(video_id))

    else:
        query_term = sys.argv[1]
        review_videos = youtube_search_reviews(query_term)
        for video in review_videos:
            print(f"Video ID: {video['videoId']}")
            print(f"Title: {video['title']}")
            print(f"Description: {video['description']}\n")