import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


# Load dataset
data = pd.read_csv("datasets/house_price.csv")

# Show first 5 rows
print(data.head())

#Select Features
X = data[['area','bedrooms','bathrooms']]
y = data['price']

#Step 5: Split Data
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

#print("X_train:\n", X_train)
#print("X_test:\n", X_test)
#print("y_train:\n", y_train)
#print("y_test:\n", y_test)

print("Training size:", X_train.shape)
print("Testing size:", X_test.shape)

#Train model
model = LinearRegression()
model.fit(X_train, y_train)

#Predict
predictions = model.predict(X_test)

#Evaluate
mse = mean_squared_error(y_test, predictions)
print("MSE:", mse)

#Graph
plt.scatter(y_test, predictions)
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Actual vs Predicted")
plt.show()

#Line plot 
plt.plot(y_test.values, label="Actual", marker='o')
plt.plot(predictions, label="Predicted", marker='x')
plt.legend()
plt.title("Actual vs Predicted Comparison")
plt.xlabel("Data Points")
plt.ylabel("Price")
plt.show()

#Residual Plot
residuals = y_test - predictions

plt.scatter(predictions, residuals)
plt.axhline(y=0, color='r')
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.title("Residual Plot")
plt.show()

#Histogram of Errors
plt.hist(residuals, bins=5)
plt.title("Error Distribution")
plt.xlabel("Error")
plt.ylabel("Frequency")
plt.show()

features = X.columns
coefficients = model.coef_

plt.bar(features, coefficients)
plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Impact on Price")
plt.show()

#Correlation Heatmap
import seaborn as sns

sns.heatmap(data.corr(), annot=True)
plt.title("Correlation Between Features")
plt.show()

plt.scatter(data['area'], data['price'])
plt.xlabel("Area")
plt.ylabel("Price")
plt.title("Area vs Price (Bigger houses cost more)")
plt.show()

import seaborn as sns

sns.boxplot(x=data['bedrooms'], y=data['price'])
plt.title("Bedrooms vs Price Distribution")
plt.xlabel("Bedrooms")
plt.ylabel("Price")
plt.show()

sns.barplot(x=data['bathrooms'], y=data['price'])
plt.title("Bathrooms vs Average Price")
plt.xlabel("Bathrooms")
plt.ylabel("Average Price")
plt.show()

plt.scatter(y_test, predictions)
plt.plot(y_test, y_test, color='red')  # perfect line
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Model Accuracy (Actual vs Predicted)")
plt.show()

errors = y_test - predictions

plt.hist(errors, bins=10)
plt.title("Prediction Error Distribution")
plt.xlabel("Error")
plt.ylabel("Frequency")
plt.show()

features = X.columns
coefficients = model.coef_

plt.bar(features, coefficients)
plt.title("Feature Importance (Impact on Price)")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.show()

bedroom_price = data.groupby('bedrooms')['price'].sum()

plt.pie(bedroom_price, labels=bedroom_price.index, autopct='%1.1f%%')
plt.title("Price Contribution by Bedrooms")
plt.show()

import seaborn as sns

sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

import squarify

sizes = data.groupby('bedrooms')['price'].sum()
labels = sizes.index.astype(str)

squarify.plot(sizes=sizes, label=labels)
plt.title("Treemap of Price by Bedrooms")
plt.axis('off')
plt.show()

sns.pairplot(data)
plt.show()

plt.hist(data['price'], bins=10)
plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

sns.kdeplot(data['price'], fill=True)
plt.title("Price Density Distribution")
plt.show()

sns.violinplot(x=data['bedrooms'], y=data['price'])
plt.title("Price Distribution by Bedrooms")
plt.show()

grouped = data.groupby(['bedrooms', 'bathrooms']).size().unstack()

grouped.plot(kind='bar', stacked=True)
plt.title("Bedrooms vs Bathrooms Distribution")
plt.show()

sorted_data = data.sort_values('price')
cumulative = sorted_data['price'].cumsum()

plt.plot(cumulative)
plt.title("Cumulative Price Growth")
plt.show()

plt.scatter(data['area'], data['price'], c=data['bedrooms'], cmap='viridis')
plt.colorbar(label='Bedrooms')
plt.title("Area vs Price with Bedrooms")
plt.xlabel("Area")
plt.ylabel("Price")
plt.show()

plt.hist(np.log(data['price']))
plt.title("Log Transformed Price Distribution")
plt.show()