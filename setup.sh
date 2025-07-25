#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Download model/data files from GitHub Releases
echo "Downloading movie_dict.pkl and similarity.pkl..."


wget -O similarity.pkl https://github.com/vanshikasing/Movie-Recommendation-System/releases/download/movie/similarity.pkl
echo "Download complete."