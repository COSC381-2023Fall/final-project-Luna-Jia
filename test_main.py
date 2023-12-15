from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "world"}

# Mock the youtube_search_reviews function to control its output
@patch('main.youtube_search_reviews')
def test_get_movie_reviews(mock_youtube_search):
    # Define the mock return value
    mock_youtube_search.return_value = [
        {
            'videoId': 'test_video_id_1',
            'title': 'Test Movie Review Title 1',
            'description': 'Test Movie Review Description 1'
        },
        # Add more mock video data as needed
    ]

    # Make a request to the test client
    response = client.get("/moviereviews/Inception")

    # Assert that the status code is 200 OK
    assert response.status_code == 200

    # Assert that the returned JSON matches the mock return value
    assert response.json() == mock_youtube_search.return_value

    # Assert that the mock function was called with the correct arguments
    mock_youtube_search.assert_called_once_with("Inception")

