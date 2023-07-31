#!/usr/bin/env python
# coding: utf-8

# In[79]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[80]:


data = pd.read_excel('housing.xlsx')


# In[81]:


data.head(5)


# In[82]:


data.shape


# # 1. What is the average median income of the data set and check the distribution of data using appropriate plots. Please explain the distribution of the plot.

# In[83]:


data['median_income'].mean()  # mean() function gives the average of the values for the required column


# In[84]:


data.hist(bins=50, figsize=(15, 10), color='skyblue')

# Show the plot.
plt.show()


# observations:The above plot,it is to be noted that the outliers are present for housing_median_age and for median_house_value.while
#     total_room,total_bedrooms,population,households,median_income are of right skewed.while latitude and longitude are of asymmetric

# # 2. Draw an appropriate plot to see the distribution of housing_median_age and explain your observations.
# 
# 

# In[85]:


# Create a histogram for 'housing_median_age' 
plt.figure(figsize=(8, 6))
plt.hist(data['housing_median_age'], bins=20, color='skyblue', edgecolor='black')
plt.xlabel('Housing Median Age')
plt.ylabel('Frequency')
plt.title('Distribution of Housing Median Age ')
plt.grid()
plt.show()


# observation:- the above hist plot the analysis that it is distributed symmetrically.
# 
# for check the skewness of the  above plot by using skew formula skewed=3*(mean-median)/std()

# In[86]:


data['housing_median_age'].mean()


# In[87]:


data['housing_median_age'].median()


# In[88]:


data['housing_median_age'].std()


# In[89]:


skewed=3*(28.63-29)/12.59
skewed


# # 3. Show with the help of visualization, how median_income and median_house_values are related?

# In[90]:


sns.scatterplot(x="median_house_value", y="median_income", data=data, color="skyblue")  
## scatter plot give a relation between two numrical values


# Show the plot.
plt.show()


# observations:- the above visualisation it is to be analysed that with an incease in the median_house_value there 
# is also an increase in the median income.median_house_value directly proportional to median income

# 
# # 4. Create a data set by deleting the corresponding examples from the data set for which total_bedrooms are not available

# In[91]:


data.shape


# In[92]:


data[data.isnull().any(axis=1)]


# In[93]:


new_data=data.dropna(subset=['total_bedrooms'])
new_data


# # 5. Create a data set by filling the missing data with the mean value of the total_bedrooms in the original data set.

# In[94]:


data['total-bedrooms']=data['total_bedrooms'].fillna(data['total_bedrooms'].mean())
data


# # 6. Write a programming construct (create a user defined function) to calculate the median value of the data set wherever required.
# 
# 

# In[95]:


data.head()


# In[96]:


data['total_bedrooms'].median()


# In[97]:


data['households'].median()


# In[98]:


data['median_house_value'].median()


# # 7. Plot latitude versus longitude and explain your observations.
# 
# 

# In[99]:


sns.scatterplot(x='latitude',y='longitude', data=data,color = 'skyblue')


# # Observations:- the above plot it is to be noted that latitude vs longitude has negative correlation as here y-axis is increasing while  x-axis is decreasing i.e both are moving opposite direction

# # 8. Create a data set for which the ocean_proximity is ‘Near ocean’.
# 
# 

# In[101]:


data.head()


# In[107]:


import pandas as pd

# Read in data from the California Housing Dataset
data = pd.read_excel('housing.xlsx')

# Filter the data where 'ocean_proximity' is 'NEAR OCEAN'
near_ocean_data = data[data['ocean_proximity'] == 'NEAR OCEAN']

# Print the first few rows of the filtered dataset
print(near_ocean_data.head())


# # 9. Find the mean and median of the median income for the data set created in question 8.
# 
# 

# In[109]:


# Calculate the mean of the 'median_income' attribute
mean_median_income = data['median_income'].mean()

# Calculate the median of the 'median_income' attribute
median_median_income = data['median_income'].median()

# Display the results
print("Mean Median Income:", mean_median_income)
print("Median Median Income:", median_median_income)


# # 10. Please create a new column named total_bedroom_size. If the total bedrooms is 10 or less, it should be quoted as small. If the total bedrooms is 11 or more but less than 1000, it should be medium, otherwise it should be considered large.
# 
# 

# In[104]:


def categorize_bedroom_size(total_bedrooms):
    if total_bedrooms <= 10:
        return "small"
    elif total_bedrooms >= 11 and total_bedrooms < 1000:
        return "medium"
    else:
        return "large"

# Apply the function to create the new column 'total_bedroom_size'
data['total_bedroom_size'] = data['total_bedrooms'].apply(categorize_bedroom_size)

# Print the updated DataFrame
print(data)


# In[ ]:





# In[ ]:




