# --------------
# Code starts here

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Load the data stored in path using .read_csv() api.
df=pd.read_csv(path)

#Get an overview of your data by using info() and describe() functions of pandas.
#print(df.info(),df.describe())

#Plot a histogram showing the distribution of the car prices (target variable).
sns.distplot(df['price'])
plt.show()

#Plot a countplot of the 'make' column of the dataset which represents the different car makers.
sns.countplot(data=df,y='make')
plt.show()

#Plot a jointplot that shows the relationship between the 'horsepower' and 'price' of the car.
sns.jointplot(data=df,x='horsepower',y='price',kind='scatter')
plt.show()

#Plot the correlation heatmap of the data.
sns.heatmap(df.corr(),cmap='YlGnBu')
plt.show()

#Plot a boxplot that shows the variability of each 'body-style' with respect to the 'price'.
sns.boxplot(data=df,x='body-style',y='price')
plt.show()

#Dataset 2
#Load the data stored in path2 using .read_csv() api.
df= pd.read_csv(path2)

from sklearn.preprocessing import Imputer,LabelEncoder
#Impute the missing values of the numerical data with mean of the particular column (Make sure you replace "?" by "NaN" before Imputing).
df=df.replace('?','NaN')
numeric_imp=Imputer(missing_values='NaN',strategy='mean',axis=0)
df['normalized-losses']=numeric_imp.fit_transform(df[['normalized-losses']])
df['horsepower']=numeric_imp.fit_transform(df[['horsepower']])

from scipy.stats import skew
import numpy as np
#Check the skewness of the numeric features and apply square root transformation on features with skewness greater than 1.
numeric_features=df.select_dtypes(include='number').columns
for features in numeric_features:
  if skew(df[features])>1:
    print(features)
    df[features]=np.sqrt(df[features])
    
#Label Encode the categorical features.
cat_features=df.select_dtypes(include=['category','object']).columns
for features in cat_features:
  le=LabelEncoder()
  print(df[features].head())
  df[features]=le.fit_transform(df[features])
  print(df[features].head())

#Combine the 'height' and 'width' to make a new feature 'area' of the frame of the car.
df['area']=df['height']*df['width']

# Code ends here


