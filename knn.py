import numpy as np
import matplotlib.pyplot as plt


datas = [[1, 1], [19, 18], [6, 2], [3, 4], [13, 12], [15, 15], [5, 5], [18, 13], [1, 5], [13, 15], [16, 17], [5, 3], [3, 1], [16, 13], [2, 6], [18, 15], [14, 18], [2, 3]]
classifications = [0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0 ]

[plt.scatter(datas[i][0], datas[i][1], color='b' if classifications[i] == 0 else 'r') for i in range(len(classifications))]
plt.title('KNN')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

def most_label(lst):
  return max(set(lst), key=lst.count)


def eucDistance(x_test_data, x_train_data):
  distance = 0
  for p0, p1 in zip(x_test_data, x_train_data):
    distance += (p0 - p1) ** 2
  return np.sqrt(distance)

def k_closest(row, x_train_data, y_train_data, k):
  knn_labels = []
  neighbors_distance = []
  
  for i in range(0, len(x_train_data)):
    distance = eucDistance(row, x_train_data[i])
    neighbors_distance.append(distance)
  
  sorted_distances = np.array(neighbors_distance)
  knn = sorted_distances.argsort()[:k]

  for i in knn:
    knn_labels.append(y_train_data[i])

  return most_label(knn_labels)

def predict(input_data, x_train_data, y_train_data, k):
  predictions = []
  for row in input_data:
    label = k_closest(row, x_train_data, y_train_data, k)
    predictions.append(label)
  return predictions


input_features = [[6, 4], [16, 11]]

predictions = predict(input_features, datas, classifications, 5)

[plt.scatter(input_features[i][0], input_features[i][1], color='g') for i in range(len(input_features))]
[plt.scatter(datas[i][0], datas[i][1], color='b' if classifications[i] == 0 else 'r') for i in range(len(classifications))]
plt.title('KNN')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

for i in range(len(input_features)):
    datas.append(input_features[i])
    classifications.append(predictions[i])

print(f'Prediction={predictions}')
