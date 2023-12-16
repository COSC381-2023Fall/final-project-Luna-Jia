import pytest
from unittest.mock import Mock, patch
from googleapiclient.errors import HttpError
import subprocess
import youtube

from youtube import youtube_search_reviews

# Sample data to mock YouTube API response
SAMPLE_API_RESPONSE = {
    "items": [
        {
            "id": {"kind": "youtube#video", "videoId": "RNjdepthRrg"},
            "snippet": {
                "title": "Inception - Movie Review by Chris Stuckmann",
                "description": "By request, another classic review from my previous channel, this time, it's Christopher Nolan's Inception."
            },
        },
    ]
}

MOCK_VIDEO_DESCRIPTION_RESPONSE = {
    "items": [
        {
            "kind": "youtube#video",
            "id": "RNjdepthRrg",
            "snippet": {
                "description": "By request, another classic review from my previous channel, this time, it's Christopher Nolan's Inception."
            },
        },
    ]
}

@patch('youtube.build')
def test_youtube_search_reviews(mock_build):
    mock_service = Mock()
    mock_build.return_value = mock_service
    mock_service.search().list().execute.return_value = SAMPLE_API_RESPONSE
    
    results = youtube_search_reviews("Inception")
    
    assert mock_build.called
    assert len(results) == 1
    assert results[0]['videoId'] == 'RNjdepthRrg'
    assert results[0]['title'] == 'Inception - Movie Review by Chris Stuckmann'
    assert "By request, another classic review" in results[0]['description']

@patch('youtube.build')
def test_get_video_description(mock_build):
    mock_service = Mock()
    mock_build.return_value = mock_service
    mock_service.videos().list().execute.return_value = MOCK_VIDEO_DESCRIPTION_RESPONSE

    video_description = youtube.get_video_description("RNjdepthRrg")

    assert mock_build.called
    assert video_description == "By request, another classic review from my previous channel, this time, it's Christopher Nolan's Inception."
    mock_service.videos().list.assert_any_call(id="RNjdepthRrg", part='snippet', maxResults=1)

# test_script_valid_input remains the same


# def test_script_no_args():
#     result = subprocess.run(['python', 'youtube.py'], capture_output=True, text=True)
#     assert 'Usage: python youtube.py' in result.stdout or 'Usage: python youtube.py' in result.stderr

def test_script_valid_input():
    result = subprocess.run(['python', 'youtube.py', 'Inception'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'Inception' in result.stdout

def test_script_with_description_flag():
    # Simulate running the script with `--description` and a video ID
    result = subprocess.run(['python', 'youtube.py', '--description', 'RNjdepthRrg'], capture_output=True, text=True)

    # Check that the output is as expected (adjust according to actual expected output)
    assert "By request, another classic review" in result.stdout.strip()
