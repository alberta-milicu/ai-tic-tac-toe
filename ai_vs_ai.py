import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
import play

df = pd.read_csv('tic-tac-toe.data', header=None)
df.replace(['x', 'o', 'b'], [1, -1, 0], inplace=True)
df.replace(['positive', 'negative'], [1, 0], inplace=True)

X = df.iloc[:, :-1]
y = df.iloc[:, -1]

gradient_boosting = GradientBoostingClassifier()
random_forest = RandomForestClassifier()
decision_tree = DecisionTreeClassifier()
mlp = MLPClassifier(hidden_layer_sizes=(100, 100), max_iter=500)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)

gradient_boosting.fit(X_train, y_train)
random_forest.fit(X_train, y_train)
decision_tree.fit(X_train, y_train)
mlp.fit(X_train, y_train)


play.play_game(random_forest, mlp)
