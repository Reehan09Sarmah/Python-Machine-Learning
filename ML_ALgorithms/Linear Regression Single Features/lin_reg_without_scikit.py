from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt

# Linear Regression Class
class LR:
    def __init__(self):
        self.w = None
        self.b = None

    def fit(self, X_train, y_train):
        numerator = 0
        denominator = 0

        for i in range(X_train.shape[0]):
            # These equations come after you minimize the cost function w.r.t 'w' and 'b'. Check copy
            numerator = numerator + ((y_train[i] - y_train.mean()) * (X_train[i] - X_train.mean()))
            denominator = denominator + ((X_train[i] - X_train.mean()) * (X_train[i] - X_train.mean()))

        self.w = numerator / denominator
        self.b = y_train.mean() - (self.w * X_train.mean())
        print(f"w: {self.w}")
        print(f"b: {self.b}")

    def predict(self, X_test):
        return self.w * X_test + self.b


data = pd.read_csv("canada_per_capita_income.csv")
X = data.iloc[:, 0].values
y = data.iloc[:, 1].values
# Create a linear regression object
reg = LR()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=2)
reg.fit(X_train, y_train)

print(f"Predicted: {reg.predict(2020)}")

# Let's plot the data along with the linear regression model
plt.xlabel('year', fontsize=20)
plt.ylabel('per capita income (US$)', fontsize=20)
plt.scatter(data.year, data.per_capita_income, color='red', marker='+')
plt.plot(data.year, reg.predict(data[['year']]), color='blue')
plt.show()