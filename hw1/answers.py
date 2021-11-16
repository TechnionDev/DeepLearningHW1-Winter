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

True - 

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
instead to introducing new data to the CV (as in the regular setting) we will decrease our generalization for outside samples.
2.in this case we will over-fit to in respect to the test-set. 
instead of tuning our parameters in accordance to multiple different samples from our universe and then test the model against an unseen samples,
we are fitting the model to pass the test-set
"""

# ==============

# ==============
# Part 3 answers

part3_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part3_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============

# ==============
# Part 4 answers

part4_q1 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q2 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

part4_q3 = r"""
**Your answer:**


Write your answer using **markdown** and $\LaTeX$:
```python
# A code block
a = 2
```
An equation: $e^{i\pi} -1 = 0$

"""

# ==============
