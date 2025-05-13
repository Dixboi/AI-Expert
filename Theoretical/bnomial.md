## Unsatisfactory test

**Situation**

Mckenna has been struggling with the Decision Tree model for her dataset.

Although her model performs exceptionally well on the training data, its test performance is far from satisfactory.

Upon consulting her mentor, she was advised to prune the tree. However, Mckenna is unclear about how this would help resolve the issue.

**Explanation**

A Decision Tree is an algorithm with low bias and high variance. A Decision Tree makes almost no assumptions about the target function.

Because of its high variance, Decision Trees overfit easily to the training dataset. Mckenna experienced this when she tested the model on her test data.

To avoid overfitting, Mckenna should prune the tree. By doing so, she forces the tree to generalize better and make assumptions by reducing the number of nodes. In other words, by pruning the tree, she increases its bias and decreases its variance.
