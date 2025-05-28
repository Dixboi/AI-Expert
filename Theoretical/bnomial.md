## Unsatisfactory test

**Situation**

Mckenna has been struggling with the Decision Tree model for her dataset.

Although her model performs exceptionally well on the training data, its test performance is far from satisfactory.

Upon consulting her mentor, she was advised to prune the tree. However, Mckenna is unclear about how this would help resolve the issue.

**Explanation**

A Decision Tree is an algorithm with low bias and high variance. A Decision Tree makes almost no assumptions about the target function.

Because of its high variance, Decision Trees overfit easily to the training dataset. Mckenna experienced this when she tested the model on her test data.

To avoid overfitting, Mckenna should prune the tree. By doing so, she forces the tree to generalize better and make assumptions by reducing the number of nodes. In other words, by pruning the tree, she increases its bias and decreases its variance.

## Course notes

**Situation**

Alivia, a student taking a deep learning class on YouTube, is writing notes about the course and wants to capture the correct output size of a convolutional layer.

Her layer receives an input image of size 64x64. She is using a kernel size of 13, padding of 3, and a stride of 2.

What is the output size of the convolutional layer?

**Explanation**

Convolutions have many parameters that influence the output size, so let's go through the properties of the convolutional layer one by one.

First, we know the input size to be 64×64.

Next, we know that the kernel size is 13. This means we will move a sliding window of size 13×13 over the entire image. The window must fit entirely in the picture, so we cannot compute the convolution for the eight rows/columns on the border. Therefore, the resulting output so far would be 52×52.

Adding padding to the image is a way to avoid the reduction of the size. In this case, we added a padding of 3, giving us an extra 6 pixels in each direction for an output of 58x58.

Finally, we have a stride of 2. This means the sliding window will move by two rows/columns every time, reducing each output dimension's size by half.

Therefore, the final output size of the convolutional layer will be 29×29.

## Familiar loss

**Situation**

Adriana is a Machine Learning enthusiast.

She recently learned about "binary cross-entropy" during a colleague's discussion. Although familiar with various Machine Learning techniques, binary cross-entropy was new to her.

She opened a book and started reading about this loss function. Unfortunately, there was a question she couldn't answer.

Which neural network problems should use binary cross-entropy as their loss function?

**Explanation**

Binary cross-entropy is the loss function we use when training binary classifiers. When working on a binary classification task, we categorize every sample into two classes. For example, given images of dogs or cats, a binary classifier will decide whether a picture shows a dog or a cat.

But binary classifiers aren't the only time we use binary cross-entropy.

Binary cross-entropy is also the loss function we use in multi-label classification problems. These are problems where we categorize every sample into one or more classes. For example, organizing movies based on the type of content, for instance, violence, adult language, smoking, or sex, where each film could belong to one or more categories.

In multi-label classification models, the output layer returns values independently. It's helpful to think of a model that outputs ten possible classes as a combination of ten different binary classifiers, and thus binary cross-entropy helps.

Neither multi-class classification nor regression problems use binary-cross entropy.

## Sample arrays

**Situation**

Margot is a data analyst working at a financial technology company. Her team is developing a model to predict stock prices based on various features, such as company performance and market trends.

Margot is using the NumPy library to manipulate the data, and she wants to filter her dataset to return every sample corresponding to class 0. Every feature of her data is stored in a NumPy array `X`, and the target values are in a NumPy array `y`.

Margot can use `X[y == 0, :]` or `X[y == 0]` to filter the data and return every sample that belongs to class 0. To understand how this expression works, we can break it down:

We have `y == 0`, which will return `True` for every sample that belongs to class 0, and `False` otherwise. We use this as a selection mask on the set `X`, which will return every row that belongs to class 0.

To return every feature from `X`, we can use `:`. When slicing arrays, we can use `:` to specify a range of values along a particular axis. In this case, using `:` alone will return every column of the array. In this case, we can accomplish the same by omitting `:`.

The following code snippet illustrates how these two options work:
```
import numpy as np

X = np.array([[2, 1], [4, 3], [6, 5], [8, 7]])
y = np.array([0, 1, 1, 0])
print(X[y == 0, :])
print(X[y == 0])
```

You should get the following result:
```
[[2 1] [8 7]]
[[2 1] [8 7]]
```

## Blog encoding techniques

**Situation**

Stevie is writing a blog post about encoding techniques for handling categorical features in a dataset. She wants to add a fun question at the end of the post to test her readers' understanding of the topic.

She writes many different ideas, and now it's your turn to decide how Stevie should mark each statement.

Which statements regarding Label encoding and One-Hot encoding techniques are correct?

• One-Hot encoding generates new columns for each categorical feature.

• One-Hot encoding creates a unique numerical representation for each categorical feature.

• Label encoding generates two new labels for each categorical feature.

• Label encoding generates new columns for each categorical feature.

**Explanation**

Before analyzing this question, we must understand what "categorical data" means.

Categorical data are variables that contain label values rather than numeric values. For example, a variable representing the weather with values "sunny," "cloudy," and "rainy" is a categorical variable.

Although some algorithms can use categorical data directly, most can't: they require the data to be numeric. We can use One-Hot or Label encoding to do this.

One-Hot encoding creates a new feature for each unique value of the original categorical variable.

For example, assume we have a dataset with a single feature called "weather" that could have the values "sunny," "cloudy," and "rainy." Applying One-Hot Encoding will get us a new dataset with three features, one for each value of the original "weather" column.

A sample that had the value "cloudy" in the previous column will now have the value 0 for both "sunny" and "rainy" and the value 1 under the "cloudy" feature.

On the other hand, Label encoding replaces each categorical value with a consecutive number starting from 0.

For example, Label Encoding would replace our weather feature with a new one containing the values 0 instead of "cloudy," 1 instead of "rainy," and 2 instead of "sunny."

## Chat application

**Situation**

Raegan is a software engineer at a company that builds a chat application. Recently, she started taking an online course on machine learning and came across the concept of splitting datasets before training a model.

Although the course discussed the importance of splitting the data into train, validation, and test sets, it didn't mention why we do this.

Which of the following statements explain why we split a dataset before training a model?

• We split the dataset to prevent the model from overfitting.

• We split the dataset to reduce the memory needed to train the model.

• We split the dataset to make the training process faster.

• We split the dataset to evaluate the model's performance accurately.

**Explanation**

Imagine teaching a math class, and it's time to evaluate your students. You decide to leave them 100 exercises as their homework. These problems cover the content they need to master to ace the exam.

How can you design an exam that effectively identifies those who learned the material?

Let's assume you pick 20 of the same homework exercises and use them in your test. This strategy might result in false positives: students who memorize the solutions to their homework may get a high score, although they don't necessarily know how to reason. In machine learning, we call this "overfitting."

To ensure students don't overfit to their training exercises, you don't want to use the same homework to test their knowledge. Instead, you want to find new problems that evaluate the same material but are different enough to force the students to show their skills.

We want to do the same when training machine learning models. If we only evaluate our work in the same data we use to train the model, we might overfit and have a model that isn't capable of generalizing to different data. In other words, the model may "memorize" the training data and learn to return excellent predictions when tested.

If we split the dataset and leave a portion to evaluate how much the model learned, we will ensure that overfit won't happen. Therefore, we can accurately assess the model's performance and avoid overfitting.

## Animal characteristics

**Situation**

Kaylani is the tech lead of a project that aims to classify pictures of animals based on 10 different characteristics. Each animal can have one or more of these features, so the system should recognize and tag the animal photos appropriately.

The team used a convolutional neural network to build this system. The only question that remains is the best approach for designing the network.

Which would be the best approach for Kaylani and her team to design the network for classifying the photos?

• Kaylani should use a sigmoid activation function in the output layer. The loss function should be binary cross-entropy.

• Kaylani should use a sigmoid activation function in the output layer. The loss function should be categorical cross-entropy.

• Kaylani should use a softmax activation function in the output layer. The loss function should be binary cross-entropy.

• Kaylani should use a softmax activation function in the output layer. The loss function should be categorical cross-entropy.

**Explanation**

The team is trying to build a multi-label classification model. Every animal will be classified with one or more of the 10 characteristics in multi-label classification. This differs from multi-class classification, where every animal will only be classified into one category.

When building multi-label classification models, we need an output layer where every class is independent. Remember that we can have more than one active class for each input. The softmax activation function doesn't work because it uses every score to output the probabilities of each class.

Softmax is the correct output for multi-class classification. Sigmoid is the correct output for multi-label classification problems. The sigmoid function converts output scores to a value between 0 and 1, independently of all the other scores.

Multi-label classification problems borrow the same principles from binary classification problems. The difference is that we end up with multiple sigmoid outputs instead of one. In our example problem, we combine three different binary classifiers. This is why we should use a binary cross-entropy as the loss function.

In summary, multi-class classification models should use a softmax output with the categorical cross-entropy loss function. Multi-label classification models should use a sigmoid output and the binary cross-entropy loss function.

## Marine biologist

**Situation**

Aniyah is a marine biologist using machine learning to study the migratory patterns of various sea creatures. She needs to determine how close different species are to one another during their migrations.

Aniyah is considering using clustering algorithms like K-Means. These algorithms require measuring the similarity between observations in her dataset.

Euclidean distance is one of the most popular distance metrics for this task.

From the following list, select every correct statement about the Euclidean distance.

• The Euclidean distance between two points does not depend on which of the two points is the start and which is the destination. In other words, the distance between p and q is the same as between q and p.

• The Euclidean distance is a way to compute the distance between two points in two-dimensional spaces. The Euclidean distance doesn't work in multidimensional spaces.

• The Euclidean distance between two distinct points is always positive.

• Traveling from a point p to a point q via a point r cannot be any shorter than traveling directly from p to q.

**Explanation**

In one or more dimensions, we can use the Euclidean distance. For example, in a line, the distance between two points is the numerical difference between their coordinates. In a plane, the distance is the Pythagorean distance.

But can we use it in multidimensional spaces?

The answer is yes; the Euclidean distance works in multidimensional spaces. Intuitively, this should make sense because we can use it as the metric to compute the distance between multi-feature observations in our dataset.

The distance from a point p to another point q is the same regardless of whether we start from p or q. This distance is always a positive value as long as p and q are different points. If p and q are the same point, the distance is 0.

In the Euclidean plane, the distance between any two distant points is the length of the line segment joining them. So this segment joining points p and q can't be any shorter, regardless of whether we get from p to q via a third point r.

## Piece replacement

**Situation**

Lucille is a data scientist writing an article about a model developed to predict if a piece of equipment has to be replaced.

The model takes in the piece's characteristics and outputs a prediction based on the relationships between the input features and the target variable.

Lucille wants to explain how the coefficients, the parameters learned by the model during training, influence the final prediction.

Which of the following options represents the best way for Lucille to describe the role of the coefficients in the model?

• A positive coefficient suggests that the feature does not affect the prediction.

• A negative coefficient suggests that the feature does not affect the prediction.

• A positive coefficient suggests that the feature has a higher probability of positively affecting the prediction.

• A positive coefficient suggests that the feature has a higher probability of negatively affecting the prediction.

**Explanation**

The coefficients in the context of a model are the parameters learned by the model during training. They determine the relationship between the input features and the output predictions.

In this example, the coefficients are used to predict whether the piece has to be replaced. The coefficients weigh the input features and determine the final prediction.

The best way to describe the role of the coefficients is by saying that a positive coefficient indicates that the variable is more likely to influence the outcome positively. This means that the variable has a positive relationship with the target variable and increases the probability of the target being positive.

On the other hand, a negative coefficient indicates that the variable has a higher likelihood of negatively influencing the outcome. This means that the variable has a negative relationship with the target variable and decreases the probability of the target being positive.

## Specific outcomes

**Situation**

Tessa is a data scientist working in the field of Computer Vision. She has been assigned a project that involves building a model to predict specific outcomes based on visual data.

Before training her model, Tessa divides her dataset into a training set and a test set. She understands that shuffling the dataset before dividing it is crucial in ensuring accurate results.

What is the primary reason for shuffling the dataset before dividing it into a training and test set?

• To make sure the training set contains more data than the test set.

• To make sure the features in the training and test sets are the same.

• To make sure the class labels are evenly split between the training and test sets.

• To make sure the training set contains the same number of samples as the test set.

**Explanation**

The main reason for shuffling the dataset before dividing it into a training and test set is to ensure that the class labels are evenly distributed between the two sets.

This is important because if the class labels are not evenly distributed, one of the sets might not contain data that belongs to some of the labels. For example, assuming our dataset is sorted by the class label, we might assign every sample from one class to the training set and every sample from another to a test set.

Shuffling the dataset helps to mitigate this issue by randomly reordering the data, which helps to ensure that the training and test sets are representative samples of the entire data population.

## Main technique

**Situation**

Clara is a data scientist working for a weather forecasting company.

The company wants to improve its temperature forecasting capabilities, so Clara is tasked with building a model that can accurately predict the temperature of a city based on meteorological data such as humidity, pressure, wind speed, and previous temperature records.

Fortunately, she has access to labeled meteorological data and temperatures dataset, so she should be OK with building a model.

Which of the following is the main technique Clara should use to solve this task?

• Clustering

• Regression

• Classification

• Dimensionality Reduction

**Explanation**

The primary technique that Clara should use to solve this problem is regression.

Regression is a supervised learning technique that predicts a continuous value based on input features. In this example, Clara wants to predict the temperature of a city based on meteorological data such as humidity, pressure, wind speed, and previous temperature records. The temperature is a continuous value.

To do this, she will use a dataset of temperature records, with meteorological data and their corresponding temperature values. She can train a model to make predictions on new, unseen data.

## Soccer department

**Situation**

Joanna works in the analytics department of a soccer team. She analyzes player performance data to determine potential strategies for upcoming games.

Joanna is given a dataset with four categorical columns, one of which is the target value she needs to predict. The target class has two possible values. The three features each have 3, 3, and 2 possible values, respectively.

Joanna must generate a synthetic dataset with all unique samples, excluding duplicates.

What will be the length of this dataset?

• The length of the dataset will be 8.

• The length of the dataset will be 18.

• The length of the dataset will be 36.

• The length of the dataset will be 64.

**Explanation**

The length of a synthetic dataset will depend on the number of possible combinations of values that can be generated based on the number of possible values for each attribute.

To determine the number of possible combinations, we can calculate the product of the number of possible values for each attribute. In Joanna's case, there are 3 possible values for the first attribute, 3 for the second attribute, 2 for the third attribute, and 2 for the target class.

The product of these values is 3 x 3 x 2 x 2 = 36. This means Joanna's synthetic dataset will have 36 different examples, each with a different combination of values for the four columns.
