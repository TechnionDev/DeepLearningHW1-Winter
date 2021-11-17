r"""
Use this module to write your answers to the questions in the notebook.

Note: Inside the answer strings you can use Markdown format and also LaTeX
math (delimited with $$).
"""

# ==============
# Part 1 answers

part1_q1 = r"""

False- 
 “in- sample errors” is the error you get on the same data you used to train your predictor and not in the test set. 
 The test set is The sample of data used to provide an unbiased evaluation of a final model fit on the training dataset.

False - 
in the edge case where the data is split in to two classes of data - A and B. if the train set will 
contain all of the A samples and the test set will contain all of the B samples then the outcome will be bad.
a shuffle is needed for the model train-test split.

True - The test set should never be used to change the model. if it will be used,
 then our model will be skewed towards the test set and 
 the model hyperparmeters will be compromised towards the test set and we will get to good of a results in the test stage  

True - in each fold we estimating the with the validation set the out of sample error of the fold and fit the hyper parameters, 
so the score of the validation is a telling sign to the generalization error.

"""

part1_q2 = r"""

this is the wrong approach to do hyperparameter tuning. 
in that setting the hyperparameters will be find-tuned to fit the test set. 
and the error of the model with respect to the test set, won't represent the real generalization power of the model.

"""

# ==============
# Part 2 answers

part2_q1 = r"""
for k=1 the result will be the nearest neighbour to the test sample 
for k=num_samples the result will end up to be the most common class in our samples.
from Rolle's lemma and from the wet part (were we saw improving results as the K increases) - 
there must be a maximum point were the K is optimal, 
and from there increase in K will result in decrease in the generalization
"""

part2_q2 = r"""

1. in this case we would result in over-fitting our model to our train-set. 
instead to introducing new data to the CV (as in the regular setting) 
we will decrease our generalization for outside samples - because of the over-fitting 
2.in this case we will over-fit to in respect to the test-set. 
instead of tuning our parameters in accordance to multiple different samples from our universe and then test the model 
against an unseen samples, we are fitting the model to pass the test-set
"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""

We will get weights with the same performance or almost the same for different Delta>0.
It happens because the regularization gives us weights that will fit (and work well) for the delta we use.

"""

part3_q2 = r"""

1. the linear model is learning the best representations of the classes based on the samples that were given to it. 
that will result in a weight matrix that can classify test samples to the most similar class that resembles that sample - 
so when there is a weird sample (like 6 that looks like 4) the weight matrix will classify it to the closest class - in this case 4.

2. This is different from KNN. In KNN we use relatively small set of data because we use the k nearest neighbors to the data. And in SVM we use all the data.  
"""

part3_q3 = r"""
1. we think that the learning rate we chose is good.
 We can see in the loss graph that the loss value decreases rapidly and improves as long as the epoch becomes larger.
  In the accuracy graph we can see that the accuracy value increases rapidly and continues to increase relatively.
2. we think that the model is slightly over-fitted to the training set.
 That is, the model fits to the training set without much better generalization.
We can see in the loss graph that the loss of the train improves but the loss of the valid not getting much better.

"""

# ==============

# ==============
# Part 4 answers

part4_q1 = r"""
we can see that the first residual plot of the top-5 fetures is more scattered then the plot after the CV 
and the CV plot is  more concentrated in the near 0 diff.
this is the expected result (close to zero line and with low variance)- as CV should improve the model and reduce the error
"""

part4_q2 = r"""
1. the use of non-linear features in the data of our model doesnt change the underlining fact that the model works in 
the same way as before regardless to the type of features the data has - that is that the model is still WX+B and the loss and training stage stays the same.
we can see that in the PolynomialFeatures part we are using the same linear class as before but the data has polynomial features. the linearity depends on the weight matrix.

2. yes, we can generate more new features by applying a non-linear function on the old features, and get larger dimentions to the data.
and then use our linear model and these new features  and approximate the real-world function.

3. the hyperplane will change as a result of the addition of new non-linear features.
 and hopefully will separate the data in a better way then before


"""

part4_q3 = r"""

1. np.logspace returns numbers spaced evenly on a log scale and np.linspace returns evenly spaced numbers over a specified
interval. We used np.logspace because we would prefer to give lambda values that they are very different. In that way we
 will get that the effect of cross validation changes with those values that they are exponentially bigger and smaller.
 
2.The lambda range is 20 values and we 3 different degrees in the cross validation, it's gives us 20*3=60 combinations. K_fold=3 and each combination is fitted to each fold. 
Therefore we will get 20*3*3=180 fits.

"""

# ==============
