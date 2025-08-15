🎬 Movie Recommendation System

This is a Content-Based Movie Recommendation System built with Python, Scikit-learn, and Streamlit.
It recommends movies similar to a user-selected movie using CountVectorizer and Cosine Similarity.

🚀 Features

Recommend top 5 similar movies based on plot keywords, genres, and cast.

Simple and interactive Streamlit web app.

Works without any external API — fully offline processing.

Uses Bag-of-Words (CountVectorizer) for feature extraction.

📂 Dataset

Source: TMDB 5000 Movie Dataset

Preprocessed to create a tags column containing combined plot, genre, cast, and crew info.

🛠️ Tech Stack

Python

Pandas, NumPy (data handling)

Scikit-learn (CountVectorizer, Cosine Similarity)

Streamlit (web interface)

⚙️ How It Works

Load dataset (movies.pkl).

Convert text data into vectors using CountVectorizer.

Calculate cosine similarity between movies.

Recommend top 5 similar movies.

▶️ Run Locally
# 1️⃣ Clone the repo
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system

# 2️⃣ Install dependencies
pip install -r requirements.txt

# 3️⃣ Run Streamlit app
streamlit run app.py

🌐 Live Demo
Streamlit Link: https://movies-recommender-app-t5nhnadyk6aexxhw2ssappk.streamlit.app/
