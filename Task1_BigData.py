import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pyspark.sql import SparkSession

# Start Spark
spark = SparkSession.builder.appName("BigData").getOrCreate()

# Read dataset
data = spark.read.csv("datasets/sales.csv", header=True, inferSchema=True)

# Show data
data.show()

#Explore Data
data.printSchema()
data.describe().show()

#Perform Analysis
data.groupBy("Category").sum("Sales").show()
data.groupBy("Region").avg("Sales").show()

#Convert for Graphs
df = data.toPandas()

#Box plot
sns.boxplot(x="Category", y="Sales", data=df)
plt.title("Sales Distribution by Category")
plt.show()

# Bar graph with colors
sns.countplot(x='Category', data=df, palette='Set2')
plt.title("Category Distribution")
plt.show()

sns.countplot(x='Category', data=df, palette='Set2')
plt.title("Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

#Histogram
sns.histplot(df['Sales'], bins=20)
plt.title("Sales Distribution")
plt.show()

# Insights:
# Category A has highest sales
# Region West performs best

#Bar Chart (Category vs Sales)
df.groupby("Category")["Sales"].sum().plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

#Bar Chart (Category vs Sales)
df.groupby("Category")["Sales"].sum().plot(
    kind="bar",
    color=['skyblue', 'orange', 'green']  # add colors here
)

plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

#Pie Chart (Sales Distribution)

df.groupby("Category")["Sales"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Category")
plt.ylabel("")
plt.show()

# Line Chart (Trend)
df["Sales"].plot(kind="line")
plt.title("Sales Trend")
plt.xlabel("Index")
plt.ylabel("Sales")
plt.show()

#Count Plot (Category Frequency)
import seaborn as sns
sns.countplot(x="Category", data=df)
plt.title("Number of Entries per Category")
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession

# Start Spark
spark = SparkSession.builder.appName("BigData").getOrCreate()

# Read dataset
data = spark.read.csv("datasets/sales.csv", header=True, inferSchema=True)

#Convert for Graphs
df = data.toPandas()

# Select only numeric columns
numeric_df = df.select_dtypes(include=['number'])


# Heatmap
sns.heatmap(numeric_df.corr(), annot=True)
plt.title("Correlation Heatmap of Dataset")
plt.show()