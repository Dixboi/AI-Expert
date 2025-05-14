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
