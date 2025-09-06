#!/usr/bin/env python
# coding: utf-8

# ## ShoppingMart_GoldTransformation
# 
# New notebook

# # Gold Layer Transformations & Aggregations

# In[1]:


from pyspark.sql.functions import *


# In[2]:


orders_df = spark.read.parquet("Files/ShoppingMartSilver_Orders/ShoppingMart_Customers_Order_Data")
reviews_df = spark.read.parquet("Files/ShoppingMartSilver_Reviews/ShoppingMart_review")
social_df = spark.read.parquet("Files/ShoppingMartSilver_Social_Media/ShoppingMart_social_media")
weblogs_df = spark.read.parquet("Files/ShoppingMartSilver_Web_Logs/ShoppingMart_web_logs")


# In[3]:


display(reviews_df)


# ##### KPI1:  Aggregate web log data to measure engagement per user on each page and actions

# In[4]:


weblogs_df = weblogs_df.groupBy("user_id", "page", "action").count()
display(weblogs_df)


# #### KPI2: Aggregate unstructured social media data to track sentiment trends across different platforms

# In[5]:


social_df = social_df.groupBy("platform", "sentiment").count()
display(social_df)


# ##### KPI3: Aggregate product reviews to calculate the average rating per product

# In[6]:


reviews_df = reviews_df.groupBy("product_id").agg(avg("rating").alias("AvgRating"))
display(reviews_df)


# #### Write data to Gold Lakehouse

# In[7]:


weblogs_df.write.mode("overwrite").parquet("Files/ShoppingMartGold_Web_Logs/ShoppingMart_web_logs")
social_df.write.mode("overwrite").parquet("Files/ShoppingMartGold_Social_Media/ShoppingMart_social_media")
reviews_df.write.mode("overwrite").parquet("Files/ShoppingMartGold_Reviews/ShoppingMart_reviews")
orders_df.write.mode("overwrite").parquet("Files/ShoppingMartGold_Orders/ShoppingMart_customers_orders")

