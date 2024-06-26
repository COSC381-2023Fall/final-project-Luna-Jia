from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "world"}

@patch('main.youtube_search_reviews')
def test_get_movie_reviews(mock_youtube_search):
    mock_youtube_search.return_value = [
        {'videoId': 'test_video_id_1', 'title': 'Test Movie Review Title 1', 'description': 'Test Movie Review Description 1'},
        # Add more mock video data as needed
    ]
    response = client.get("/moviereviews/Inception")
    assert response.status_code == 200
    assert response.json() == mock_youtube_search.return_value
    mock_youtube_search.assert_called_once_with("Inception")

@patch('main.get_video_description')
def test_get_video_description(mock_get_description):
    mock_video_id = "test_video_id"
    mock_description = "This is a test description for the video."
    mock_get_description.return_value = mock_description

    response = client.get(f"/descriptions/{mock_video_id}")

    assert response.status_code == 200
    assert response.json() == {"video_id": mock_video_id, "description": mock_description}
    mock_get_description.assert_called_once_with(mock_video_id)

@patch('main.translate_text')
@patch('main.youtube_search_reviews')
def test_get_movie_reviews_by_language(mock_youtube_search, mock_translate_text):
    mock_translate_text.return_value = "Incepción" # Assume this is the translated text
    mock_youtube_search.return_value = [
        {'videoId': 'test_video_id_2', 'title': 'Test Movie Review Title 2', 'description': 'Test Movie Review Description 2'},
        # Add more mock video data as needed
    ]

    response = client.get("/moviereviews/es/Inception")
    
    assert response.status_code == 200
    assert response.json() == mock_youtube_search.return_value
    mock_translate_text.assert_called_once_with("Inception", "es")
    mock_youtube_search.assert_called_once_with("Incepción", "es")
