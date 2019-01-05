from numpy import *

num_movies = 10

num_users = 5

ratings = random.randint(11, size = (num_movies,num_users))

print ratings

did_rate = ( ratings != 0 ) * 1

print did_rate

print ratings.shape

james_ratings = zeros((num_movies,1))

print james_ratings

james_ratings[0] = 8
james_ratings[4] = 7
james_ratings[7] = 3

print james_ratings

#axis = 1 column append
ratings = append(james_ratings, ratings, axis = 1)
print ratings

did_rate = append(((james_ratings != 0 )*1), did_rate, axis = 1)
print did_rate

a = [10, 20, 30]

print sum(a)

meanA = mean(a)
print meanA

a = [10 - meanA, 20 - meanA, 30 - meanA]

print a

i = 0
idx = where(did_rate[i] == 1)[0]
print "idx"
print idx

def normalize_ratings(ratings, did_rate):
    num_movies = ratings.shape[0]
    print num_movies

    ratings_mean = zeros(shape = (num_movies, 1))
    print ratings_mean
    ratings_norm = zeros(shape = ratings.shape)
    print ratings_norm
    
    for i in range(num_movies): 
        # Get all the indexes where there is a 1
        # Note that idx is an array
        idx = where(did_rate[i] == 1)[0]
        
        #  Calculate mean rating of ith movie only from user's that gave a rating
        ratings_mean[i] = mean(ratings[i, idx])
        ratings_norm[i, idx] = ratings[i, idx] - ratings_mean[i]
    
    return ratings_norm, ratings_mean


ratings, ratings_mean = normalize_ratings(ratings, did_rate)

print ratings
print ratings_mean

num_users = ratings.shape[1]
#features must be characters shared by users and movies (e.g. comedy, action, romantic)
num_features = 3

movies_features = random.randn( num_movies, num_features );
users_features  = random.randn( num_users, num_features );
initial_X_and_theta = r_[movies_features.T.flatten(), users_features.T.flatten()];

print movies_features
print users_features
print initial_X_and_theta

print movies_features.shape
print users_features.shape
print initial_X_and_theta.shape

#
# Need to revisit these code.
#
# Gradient Descent is used heavily.
#
# https://github.com/Nikhil22/netflix-style-recommender/blob/master/movie_recommender.py
# https://www.youtube.com/watch?v=9Ky-Zn9AoDE&index=3&list=PLseNcwx1RJ4WdgtrMTXndw4B4nlf4-pgS
#
#

def unroll_params(X_and_theta, num_users, num_movies, num_features):
	# Retrieve the X and theta matrixes from X_and_theta, based on their dimensions (num_features, num_movies, num_movies)
	# --------------------------------------------------------------------------------------------------------------
	# Get the first 30 (10 * 3) rows in the 48 X 1 column vector
	first_30 = X_and_theta[:num_movies * num_features]
	# Reshape this column vector into a 10 X 3 matrix
	X = first_30.reshape((num_features, num_movies)).transpose()
	# Get the rest of the 18 the numbers, after the first 30
	last_18 = X_and_theta[num_movies * num_features:]
	# Reshape this column vector into a 6 X 3 matrix
	theta = last_18.reshape(num_features, num_users ).transpose()
	return X, theta


# In[59]:

def calculate_gradient(X_and_theta, ratings, did_rate, num_users, num_movies, num_features, reg_param):
	X, theta = unroll_params(X_and_theta, num_users, num_movies, num_features)
	
	# we multiply by did_rate because we only want to consider observations for which a rating was given
	difference = X.dot( theta.T ) * did_rate - ratings
	X_grad = difference.dot( theta ) + reg_param * X
	theta_grad = difference.T.dot( X ) + reg_param * theta
	
	# wrap the gradients back into a column vector 
	return r_[X_grad.T.flatten(), theta_grad.T.flatten()]


# We want the cost to be minimum.
# Cost means the the Y-axis difference between the best fit line
# and (x1,y1) points.
# This will run many times according maxiter=100.
# Note that calculate_cost() and calculate_gradient() have same parameters.
#
#
def calculate_cost(X_and_theta, ratings, did_rate, num_users, num_movies, num_features, reg_param):
	X, theta = unroll_params(X_and_theta, num_users, num_movies, num_features)
	
	# we multiply (element-wise) by did_rate because we only want to consider observations for which a rating was given
	cost = sum( (X.dot( theta.T ) * did_rate - ratings) ** 2 ) / 2
	# '**' means an element-wise power
	regularization = (reg_param / 2) * (sum( theta**2 ) + sum(X**2))
	return cost + regularization


# import these for advanced optimizations (like gradient descent)

from scipy import optimize


# In[65]:

# regularization paramater

reg_param = 30


# perform gradient descent, find the minimum cost (sum of squared errors) and optimal values of X (movie_features) and Theta (user_prefs)

minimized_cost_and_optimal_params = optimize.fmin_cg(calculate_cost, fprime=calculate_gradient, x0=initial_X_and_theta, 
           args=(ratings, did_rate, num_users, num_movies, num_features, reg_param), maxiter=100, disp=True, full_output=True ) 


cost, optimal_movie_features_and_user_prefs = minimized_cost_and_optimal_params[1], minimized_cost_and_optimal_params[0]


# unroll once again

movie_features, user_prefs = unroll_params(optimal_movie_features_and_user_prefs, num_users, num_movies, num_features)

print movie_features

print user_prefs

# Make some predictions (movie recommendations). Dot product

all_predictions = movie_features.dot( user_prefs.T )

print 'all_predictions'
print all_predictions

# add back the ratings_mean column vector to my (our) predictions
predictions_for_james = all_predictions[:, 0:1] + ratings_mean

#This is how James will predict each movie based on his features.
print 'predictions for james'
print predictions_for_james

print 'james ratings'
print james_ratings