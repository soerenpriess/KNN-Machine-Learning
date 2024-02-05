# KNN-Machine-Learning

The K-nearest neighbor algorithm is a learning classifier that makes classifications or predictions about the grouping of a single data point.

This algorithm can be used for regression and classification problems, whereby it is generally used as a classification algorithm. In this example, the algorithm is used for the classification of data points.

1. [How does KNN work?](#how-does-KNN-work?)
   - [Euclidean distanc](#euclidean-distanc)
   - [Define k](#define-k)
2. [Advantages and disadvantages](#advantages-and-disadvantages)
3. [Use cases](#use-cases)

# How does KNN work?

KNN is based on the assumption that similar points can be found in the vicinity of each other. The aim is to find out which data points have the smallest distance to an input data point in order to then be able to classify the input data point.
To be able to do this, the distance between an input data point and other data points must be calculated. There are different distance metrics that can be used for this. In this example, the Euclidean distance is used for this.

## Euclidean distanc

This is the most commonly used distance measure that is restricted to real-valued vectors. Using the following formula, the distance is measured via a straight line between the input data point and the other data points.

$$d(x,y) = \sqrt{(x_1 - y_1)^2 + (x_2 - y_2)^2 + ... + (x_n - y_n)^2}$$

$$= \sqrt{\sum_{k=1}^n (x_i - y_i)^2} $$

![](./pictures/distance.png)

## Define k

The k value in the KNN algorithm determines how many neighbors are checked to determine the classification of a particular input data point. For example, if k = 1, the instance is assigned to the same class as its only nearest neighbor. An odd number should be chosen for k to avoid a "tie" in the classification.

# Advantages and disadvantages

| Advantages          |                 Disadvantages                 |
| ------------------- | :-------------------------------------------: |
| ease of use         |                 poor scaling                  |
| easy to fit         |             prone to overfitting              |
| few hyperparameters | does not work well with high-dimensional data |

# Use cases

- Fraud prevention in the banking industry

  - KNN can be used to identify suspicious transactions by recognizing patterns of fraudulent activity.

- Facial recognition

  - KNN can be used in facial recognition by identifying similar faces based on features such as eyes, nose and mouth.

- Network security

  - KNN can be used to detect anomalies in network traffic and identify potential security breaches.

- Traffic flow prediction

  - KNN can analyze traffic patterns and be used to predict traffic flow disruptions or changes in real time.

- Finance

  - KNN can help banks to assess the risk of a loan to a company or individual based on credit data. It is therefore used to determine the creditworthiness of a loan applicant.

- Robotics

  - KNN can be used in robotics to recognize and classify objects in the environment.

- etc.
