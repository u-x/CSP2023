#   a421_multi_movie_recommender.py
#   A basic movie recommendation code with normalization.
#   This code is based on the netflix-style-recommender project shared on GitHub.
#   All statistical functions were written by Nikhil22.
#   The code has been modified from its original version.
import numpy as np 

# define the movies, users, and different ratings
movies = ["Back to the Future", "Guardians of the Galaxy", "Avatar", "Trolls", "Black Panther"]
genres = ["Action", "Adventure", "Science Fiction", "Comedy"]

#TODO 1 change these values to the names of the students in your group
users = ["MEHRING", "Tremelling", "wimalaratne", "gardipee", "Mahr", "mehring", "Welke", "verstrate", "Croke"]

#TODO 2 paste your ratings tables here
movie_ratings = [[7,7,8,9,7,7,6,5,5],[7,8,8,10,9,6,8,5,5],[5,6,7,8,10,4,10,7,5],[8,5,9,8,8,6,0,4,5],[0,0,0,6,0,0,5,0,0]]				
user_preferences = [[3,3,4,4,4,3,3,3,3],[5,2,5,4,5,4,4,4,2],[5,4,4,4,5,5,3,5,1],[3,3,5,5,3,4,5,1,5]]				
movie_genre = [[0.6,0.3,0.0,0.1],[0.2,0.3,0.3,0.2],[0.3,0.3,0.4,0.0],[0.6,0.2,0.0,0.2],[0.4,0.0,0.6,0.0]]				

# TODO Your ratings, rate the five movies in the list below
# notice how your recommendations change when you add a rating for 1 movie
your_ratings = np.zeros((5, 1))
your_ratings[0] = 1 # rating for Back to the Future
your_ratings[1] = 2 # rating for Guardians of the Galaxy
your_ratings[2] = 3 # rating for Avatar
your_ratings[3] = 4 # rating for Trolls
your_ratings[4] = 5 # rating for Black Panther

# --- Normalization Process ---
# ratings, movies_features, and user_prefs are arrays which are more structured lists
ratings = np.array(movie_ratings)
movie_features = np.array(movie_genre)
user_prefs = np.array(user_preferences)

# append your ratings to the data representing everyone elses
ratings = np.append(your_ratings, ratings, axis=1)

# to check if a user has rated a movie, create a matrix that shows
# a 1 if the user rated it and a 0 if not
did_rate = (ratings != 0 ) * 1

# function to normalize the data
def normalize_ratings(ratings, did_rate):
    num_movies = ratings.shape[0]
    
    ratings_mean = np.zeros(shape = (num_movies, 1))
    ratings_norm = np.zeros(shape = ratings.shape)
    
    for i in range(num_movies): 
        # Get all the indexes where there is a 1
        idx = np.where(did_rate[i] == 1)[0]
        #  Calculate mean rating of ith movie only from user's that gave a rating
        ratings_mean[i] = np.mean(ratings[i, idx])
        ratings_norm[i, idx] = ratings[i, idx] - ratings_mean[i]
    
    return ratings_norm, ratings_mean

# use the fuction to get normalized data sets
ratings_norm, ratings_mean = normalize_ratings(ratings, did_rate)

# print the predictions in a nice way:
for index in range(len(movies)):
    # grab index (integer), which remember, are all sorted based on the prediction values 
    print("%.1f is predicted for the movie %s" % (ratings_mean[index], movies[index]))
