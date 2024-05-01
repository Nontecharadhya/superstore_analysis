#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns
import os


# In[2]:


os.getcwd()


# In[3]:


os.chdir('C:\\Users\\Abhi\\documents\\readings')


# In[4]:


df=pd.read_csv('Superstore_data.csv',encoding='unicode_escape')


# In[5]:


df.head()


# In[6]:


df.info()


# In[7]:


df.isnull().sum()


# In[8]:


df.dtypes


# In[9]:


df[df.duplicated()]


# In[10]:


df.duplicated(keep=False).sum()


# # EDA : Customer Analysis
# ### Customer Segmentation

# In[10]:


# types of customers
type_of_customers=df['Segment'].unique()
type_of_customers


# In[11]:


noc=df['Segment'].value_counts().reset_index()
noc


# In[12]:


noc=noc.rename(columns={'Segment':'CustomerTypes'})
noc


# In[13]:


plt.figure(figsize=(6,6))
plt.title('Distribution of Customer Types')
plt.pie(noc['count'],labels =noc['CustomerTypes'],autopct='%1.1f%%')
plt.show()


# In[14]:


# Cusotmrs and sales
spc=df.groupby('Segment')['Sales'].sum().reset_index()
spc=spc.rename(columns={'Segment':'CustomerTypes','Sales':'Total Sales'})
spc


# In[15]:


plt.figure(figsize=(5,5))
plt.title('Bar chart of Sales by CustomerTypes')
plt.bar(spc['CustomerTypes'],spc['Total Sales'])
plt.xlabel=('CustomerTypes')
plt.ylabel=('Total Sales')
plt.show()


# # Customers Loyality

# In[16]:


# group data accourding to customer id,segment and calcualte freq of the orders 
cof=df.groupby(['Customer ID','Customer Name','Segment'])['Order ID'].count().reset_index()
# rename the orderid column
cof.rename(columns={'Order ID':'Total Orders'},inplace=True)

# identify repeat customers 
repeat_cus=cof[cof['Total Orders']>=1]

# sorted repeat customers in descending orders
sorted_rc=repeat_cus.sort_values(by='Total Orders',ascending =False)
print(sorted_rc.head(10).reset_index())


# # Ranking customers by sales

# In[17]:


# group data based on : customer id ,customer name and sales
customer_sales =df.groupby(['Customer ID','Customer Name'])['Sales'].sum().reset_index()

# sort in descending order
top_buyer =customer_sales.sort_values(by='Sales',ascending =False)

#print the output
print(top_buyer.head(10).reset_index(drop=True))


# # Analysis of Shipping Method

# In[18]:


tosm =df['Ship Mode'].unique()
tosm


# In[19]:


# frequency use of shipping methods
shipping_mode =df['Ship Mode'].value_counts().reset_index()
shipping_mode =shipping_mode.rename(columns={'index':'Mode of shippment','count':'frequency'})
shipping_mode


# In[20]:


# plot a pie chart of ship mode
plt.figure(figsize=(6,6))
plt.title=('Popular Shipping Mode')
plt.pie(shipping_mode['frequency'],labels=shipping_mode['Ship Mode'],autopct='%1.1f%%')
plt.show()


# # Graphical Analysis

# In[21]:


# customers by states
state =df['State'].value_counts().reset_index()
state =state.rename(columns={'index':'State','count':'No of customers'})
state.head(10)


# In[22]:


# customers by city
city =df['City'].value_counts().reset_index()
city =city.rename(columns={'index':'City','count':'Number of Customers'})
city.head(10)


# In[23]:


# Sales per state
sale_state =df.groupby(['State'])['Sales'].sum().reset_index()

# grouping state by sales
top_state_sales=sale_state.sort_values(by='Sales',ascending=False)

print(top_state_sales.head(5).reset_index(drop=True))


# # Prpduct Category Segmentation

# In[24]:


# types of products
p_cat=df['Category'].value_counts()
p_cat 


# In[25]:


# group data by product category
subcategory_count=df.groupby('Category')['Sub-Category'].nunique().reset_index()

# sort by ascending order
subcategory_count =subcategory_count.sort_values(by='Sub-Category',ascending=False)
print(subcategory_count.reset_index(drop=True))


# In[26]:


# sales by each category
cat_sales=df.groupby(['Category'])['Sales'].sum().reset_index()
cat_sales


# In[71]:


# plotting a pie chart
plt.title=('Top product category based on sales')
plt.pie(cat_sales['Sales'],labels=cat_sales['Category'],autopct='%1.1f%%')
plt.show()


# In[27]:


# group data by product sub-category vs sales
p_sub=df.groupby('Sub-Category')['Sales'].sum().reset_index()

# sorting in descending order
top_p_sub=p_sub.sort_values(by='Sales',ascending=False)

top_p_sub.reset_index(drop=True)


# In[29]:


top_p_sub=top_p_sub.sort_values(by='Sales',ascending=True)

# plotting a pie chart
plt.barh(top_p_sub['Sub-Category'],top_p_sub['Sales'])
plt.title('Top product Sub-Categories based on Sales')
plt.xlabel('Prodect Sub-categories')
plt.ylabel('Total Sales')
plt.show()


# # Sales Trend Analysis

# In[38]:


# convert order date to datetime format
df['Order Date']=pd.to_datetime(df['Order Date'])
df.dtypes


# In[39]:


# grouping by year and suming the sales per year
yearly_sales=df.groupby(df['Order Date'].dt.year)['Sales'].sum()

# setting new indexes and remaining the columns
yearly_sales =yearly_sales.reset_index()
yearly_sales =yearly_sales.rename(columns={'Order Date':'Year','Sales':'Total Sales'})

print(yearly_sales)


# In[40]:


import matplotlib.pyplot as plt
plt.figure(figsize=(6,6))
plt.bar(yearly_sales['Year'], yearly_sales['Total Sales'])
plt.title('Yearly sales')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.xticks(rotation=65)
plt.show()


# In[41]:


# plot a line graph
plt.plot(yearly_sales['Year'],yearly_sales['Total Sales'],marker='o',linestyle='-')
plt.title('Yearly sales')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.xticks(rotation=65)
plt.show()


# # Quartely Sales

# In[43]:


# convert order date to datetime format
df['Order Date'] =pd.to_datetime(df['Order Date'])

# filter data according to year
quartely_sales =df[df['Order Date'].dt.year == 2016]

# calculate data quartely sales for year 2018

quartely_sales =quartely_sales.resample('Q',on='Order Date')['Sales'].sum()
quartely_sales =quartely_sales.reset_index()
quartely_sales =quartely_sales.rename(columns={'Order Date':'Quarter','Sales':'Total Sales'})

print(quartely_sales)


# In[50]:


import matplotlib.pyplot as plt

# Assuming monthly_sales contains the data you calculated earlier

plt.plot(monthly_sales['Month'], monthly_sales['Total Sales by Month'], marker='o', linestyle='-')
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Total Sales')
plt.xticks(rotation=65)
plt.show()


# # Monthly sales

# In[49]:


import pandas as pd

# Assuming df is your DataFrame containing sales data

# Convert 'Order Date' column to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Filter data according to year
yearly_sales = df[df['Order Date'].dt.year == 2014]

# Calculate monthly sales for the year 2014
monthly_sales = yearly_sales.resample('M', on='Order Date')['Sales'].sum()
monthly_sales = monthly_sales.reset_index()
monthly_sales = monthly_sales.rename(columns={'Order Date': 'Month', 'Sales': 'Total Sales by Month'})

print(monthly_sales)


# In[ ]:




