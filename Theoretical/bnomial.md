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
