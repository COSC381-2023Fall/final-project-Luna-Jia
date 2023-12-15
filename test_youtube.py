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
            "id": {"kind": "youtube#video", "videoId": "sample_video_id_1"},
            "snippet": {
                "title": "Sample Review 1",
                "description": "This is the description for Sample Review 1"
            },
        },
        
    ]
}

@patch('youtube.build')
def test_youtube_search_reviews(mock_build):
    mock_service = Mock()
    mock_build.return_value = mock_service
    mock_service.search().list().execute.return_value = SAMPLE_API_RESPONSE
    
    results = youtube_search_reviews("Sample Movie")
    
    assert mock_build.called
    assert len(results) == 1
    assert results[0]['videoId'] == 'sample_video_id_1'
    assert results[0]['title'] == 'Sample Review 1'
    assert 'Sample Review 1' in results[0]['description']

def test_script_no_args():
    result = subprocess.run(['python', 'youtube.py'], capture_output=True, text=True)
    assert 'Usage: python youtube.py' in result.stdout or 'Usage: python youtube.py' in result.stderr

def test_script_valid_input():
    result = subprocess.run(['python', 'youtube.py', 'Inception'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'Inception' in result.stdout  