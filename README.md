# list hidden 文件
ls -a

# start virtual environment 
source .venv/bin/activate

# 切换 git branch
git fetch origin
git checkout luna/2-feature-find-movie-commentaryreviews-through-youtube-api

# show content of a file 
cat requirements.txt

# To get the dependencies in a virtual environment, run the command: 
python3 -m pip freeze > requirements.txt

# install google API
pip install google-api-python-client

#run test
pytest --cov=.

# check which lines are not covered by the test
pytest --cov=. --cov-report term-missing

# run youtube API to see 10 reviews for movie "Inception"
python youtube.py "Inception"

# run fast API app
uvicorn main:app --reload