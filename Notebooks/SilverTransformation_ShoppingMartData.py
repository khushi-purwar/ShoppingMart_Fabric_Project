#!/usr/bin/env python
# coding: utf-8

# ## SilverTransformation_ShoppingMartData
# 
# New notebook

# ### SILVER Layer Notebook: Data Cleaning & Integration

# ##### Load Bronze Data

# In[5]:


from pyspark.sql.functions import *


# In[10]:


# Structured Data
df_customers = spark.read.format("csv").option("header", "true").load("Files/StructuredFiles/Customers.csv")
df_orders = spark.read.format("csv").option("header", "true").load("Files/StructuredFiles/Orders.csv")
df_products = spark.read.format("csv").option("header", "true").load("Files/StructuredFiles/Products.csv")

# Unstructured Data
df_reviews = spark.read.json("Files/UnStructuredFiles/Review.json")
df_social = spark.read.json("Files/UnStructuredFiles/SocialMedia.json")
df_weblogs = spark.read.json("Files/UnStructuredFiles/WebLogs.json")


# In[6]:


display(df_orders)


# ##### Data Cleaning & Enriching

# In[7]:


df_orders = df_orders.dropna(subset=["OrderID", "CustomerID", "ProductID", "OrderDate", "TotalAmount"])
df_orders = df_orders.withColumn("OrderDate", to_date(col("OrderDate")))
# display(df_orders)


# ##### Join With Products & Customers

# In[8]:


df_orders = df_orders \
    .join(df_customers, on = "CustomerID", how = "inner") \
    .join(df_products, on = "ProductID", how = "inner")

# display(df_orders)


# ##### Write data to Silver Lakehouse

# In[9]:


df_orders.write.mode("overwrite").parquet("Files/ShoppingMartSilver_Orders/ShoppingMart_Customers_Order_Data")


# In[11]:


df_reviews.write.mode("overwrite").parquet("Files/ShoppingMartSilver_Reviews/ShoppingMart_review")
df_social.write.mode("overwrite").parquet("Files/ShoppingMartSilver_Social_Media/ShoppingMart_social_media")
df_weblogs.write.mode("overwrite").parquet("Files/ShoppingMartSilver_Web_Logs/ShoppingMart_web_logs")

