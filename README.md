# Internship_Tasks-Codetech-

*COMPANY*: CODETECH IT SOLUTIONS

*NAME*: VARSHINI B

*INTERN ID*: CTIS5595

*DOMAIN*: DATA ANALYTICS INTERN

*DURATION*: 12 WEEKS

*MENTOR*: NEELA SANTOSH

*DESCRIPTION*:

This project integrates Big Data Analytics, Machine Learning, Sentiment Analysis, and Data Visualization Dashboard to extract meaningful insights from different datasets and present them in an interactive manner.

Task 1 : Big Data Analysis Module

The Big Data module uses Apache Spark to process and analyze large-scale sales data efficiently. The dataset is loaded using Spark, and various operations such as schema analysis, descriptive statistics, and aggregation are performed. Key insights like total sales by category and average sales by region are derived.

To enhance understanding, the processed data is converted into Pandas format and visualized using graphs such as box plots, bar charts, histograms, pie charts, and heatmaps. These visualizations help in identifying sales distribution, trends, and correlations among different variables.

Task 2 : Machine Learning Module

The Machine Learning module focuses on predicting house prices using a Linear Regression model. The dataset contains features like area, number of bedrooms, and bathrooms.

The data is split into training and testing sets, and the model is trained to learn the relationship between features and house prices. Predictions are made on test data, and performance is evaluated using Mean Squared Error (MSE).

Multiple visualizations such as scatter plots, residual plots, feature importance graphs, and correlation heatmaps are used to analyze model performance and feature impact. This module demonstrates how predictive analytics can be applied to real-world problems.

Task 3 : Interactive Dashboard Module

The Dashboard module provides a user-friendly interface to visualize sales data interactively. It is built using Dash and Plotly.

The dashboard includes multiple charts such as bar charts, pie charts, and line charts to represent sales distribution, category-wise performance, and trends. This enables users to quickly interpret data insights without analyzing raw datasets.

Task 4 : Sentiment Analysis Module

The Sentiment Analysis module analyzes textual review data to determine whether the sentiment is positive, negative, or neutral.

Using Natural Language Processing (NLP) techniques and the VADER sentiment analyzer from NLTK, each review is assigned a sentiment score. Based on this score, reviews are categorized into sentiment classes.

The results are visualized using bar charts, showing the distribution of sentiments, which helps in understanding user opinions and feedback patterns.


*OUTPUT*:

task 1 :

<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/56f0a660-046d-48fa-a5bd-9b939d0c1e3c" />

This graph shows how sales change over time (or index values).
Sales are not constant; they fluctuate. The highest sales occur in the middle, and the lowest sales occur at the end.

<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/3e008e16-4213-4e36-babc-565292d32b6a" />

This chart shows how total sales are divided among different categories.
Electronics is the top-performing category, while Clothing has the lowest share.

<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/13bb0a8f-b61f-4bbf-b9d2-db01ec764920" />

This graph compares total sales for each category.
Electronics category dominates overall sales performance.

<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/46589d58-0d8d-4e93-a004-cd99c1bca009" />

This heatmap shows the relationship between numerical variables.
Since only one variable (Sales) is present, the correlation value is 1.
There are no multiple features to compare, so correlation analysis is limited.

<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/51cdd30d-aa0a-439b-a39a-59e446054145" />

Sales Distribution (Histogram)

This graph shows how frequently different sales values occur.
Sales are evenly distributed without any repeated patterns.

Task 2 :

<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/f530e247-60f6-4ebe-a9c9-cb727fba7533" />

The residual plot shows the difference between the actual values and predicted values of the model.
The model’s predictions are very accurate, as the residuals are close to zero. This indicates that the model fits the data well and has minimal prediction error.

<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/ab9121f8-29b4-4c70-b7b4-166c1ef2dd5c" />

Feature Importance (Bar Graph)

This graph shows how much each feature affects house price prediction.
Bathrooms are the most important factor influencing house prices in this model.

<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/eb979c84-076a-4390-a726-c91e0354d797" />

Correlation Between Features (Heatmap)

This heatmap shows relationships between all features.
All features positively influence price, with area being the strongest predictor.

<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/b398586c-a100-4eae-b0a9-1a79c6c7fbcc" />

Area vs Price (Scatter Plot)

This graph shows the relationship between house area and price.
Bigger houses cost more, showing a direct relationship between area and price.

<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/1ec5aee8-2fbb-4b2b-bf86-39a736fe838d" />

This chart shows how total price is distributed based on the number of bedrooms.
3-bedroom houses contribute the most to total price, making them the most significant category.

<img width="640" height="480" alt="Image" src="https://github.com/user-attachments/assets/d3264ae6-8a1b-4438-b5b9-1a5a017af581" />

Price Density Distribution (KDE Plot):

This graph shows how house prices are distributed across the dataset.
House prices follow a normal distribution, with most properties priced around the average range.

Task 3 :



