import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load data
df = pd.read_csv("studentScore.csv")

# Optional: check columns
print(df.columns)
print(df.head())

# Features and target
X = df[['hours']]      # 2D
Y = df['score']        # 1D

# Train-test split (NOTE: correct order!)
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Create model
model = LinearRegression()

# ✅ Fit on TRAIN data
model.fit(X_train, Y_train)

# ✅ Predict on TEST data
Y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(Y_test, Y_pred)
print("MSE:", mse)

r2 = r2_score(Y_test, Y_pred)
print("R2:", r2)

# Plot regression line on all data
plt.scatter(df['hours'], df['score'], label='Actual data')
plt.plot(df['hours'], model.predict(df[['hours']]), label='Regression line')
plt.xlabel("hours studied")
plt.ylabel("score")
plt.title("Hours vs Score with Regression Line")
plt.legend()
plt.show()
