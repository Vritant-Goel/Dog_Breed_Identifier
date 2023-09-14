# Dog_Breed_Identifier

The goal is to build a model that can identify the breed of a dog when given an image. The challenge here is that there are 120 breeds, and a relatively small number of training images per class, which makes the problem harder than it orginally seems.

# Methodology

The most apparent solution for tackling an image recognition challenge is the utilization of a convolutional neural network (CNN). However, the challenge arises from the scarcity of training data, as relying solely on the provided training images would inevitably result in severe overfitting. To address this issue, I opted for a transfer learning approach, leveraging Resnet18 to provide my model with a beneficial starting point, effectively reducing the complexities associated with training.

I selected Resnet18 as my initial model due to its relatively deep architecture and its ability to combat the vanishing gradient problem. The depth of this model allowed it to possess the necessary complexity to accurately identify the characteristics of dogs. While deeper models like Resnet34 or others might potentially achieve even higher accuracy, I chose Resnet18 due to limitations in available computational resources. Additionally, Resnet employs residual blocks to address the vanishing gradient problem, ensuring that each training example contributes significantly to optimizing the model. This mechanism facilitates the model's convergence toward an optimal solution, which is particularly advantageous when dealing with such a restricted training dataset.

# Future

If I wanted to improve the accuracy of this model, I would have to do one of two things: use a deeper model or use a larger training set. If using a deeper model improves the accuracy, that would mean that my current model is underfitting the data. Using a larger training set, such as the Stanford Dogs Dataset, would reduce overfitting, is almost guaranteed to improve accuracy. However, it will also take much more computation power. Going forward, it would also be a good idea to do error analysis and plot a confusion matrix to see exactly what kinds of images it is getting wrong. It may turn out that it is incorrectly classifying breeds that are very similar to begin with.
