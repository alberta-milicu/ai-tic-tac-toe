import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import play


df = pd.read_csv('tic-tac-toe.data', header=None)
df.replace(['x', 'o', 'b'], [1, -1, 0], inplace=True)
df.replace(['positive', 'negative'], [1, 0], inplace=True)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]


model = RandomForestClassifier()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)


play.play_gameAI(model)
