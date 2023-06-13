import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier
import play

df = pd.read_csv('tic-tac-toe.data', header=None)
df.replace(['x', 'o', 'b'], [1, -1, 0], inplace=True)
df.replace(['positive', 'negative'], [1, 0], inplace=True)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

nn_model = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=500)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
nn_model.fit(X_train, y_train)

nn_model.fit(X_train, y_train)
nn_y_pred = nn_model.predict(X_test)
nn_accuracy = accuracy_score(y_test, nn_y_pred)
print("Neural Network Accuracy:", nn_accuracy)

play.play_gameAI(nn_model)
