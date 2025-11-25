#step 1: import Requiredd libaries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from sklearn.datasets import load_iris

#step2 load and explore the dataset
iris = load_iris()
X = iris.data
Y = iris.target

print("Features", iris.feature_names)
print("target classes", iris.target_names)
print("shape of data", X.shape)

#step 3 convert to data frame
df = pd.DataFrame(X, columns=iris.feature_names)
df['species' ]= iris.target
print(df.head())

#step 4 visualize the data
sns.pairplot(df,hue='species')
plt.show()

#step 5 split data into train and test sets
X_train,X_test,Y_train,Y_test = train_test_split(X, Y,test_size=0.2,random_state=42)

#step 6
model = LogisticRegression(max_iter=200)
model.fit(X_train,Y_train)

#step 7

Y_pred = model.predict(X_test)

#step 8
print("Accuracy", accuracy_score(Y_test,Y_pred))
print("\nClassification Report:\n", classification_report(Y_test,Y_pred))


#step 9
cm = confusion_matrix(Y_test, Y_pred)
sns.heatmap(cm, annot=True, cmap="Blues", xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()