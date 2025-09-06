# ShoppingMart Analytics – End-to-End Microsoft Fabric Data Engineering Project

## 📌 Project Overview
This project demonstrates an **End-to-End E-Commerce Analytics Data Engineering Pipeline** using **Microsoft Fabric Medallion Architecture** (Bronze → Silver → Gold layers).  
It includes **structured and unstructured data ingestion**, transformation using **Fabric Notebooks**, and final **Power BI reporting** built on a semantic model.

---

## 🏗 Architecture


The solution follows the **Medallion Architecture**:
- **Bronze Layer** → Raw data ingestion (Structured + Unstructured)
- **Silver Layer** → Data cleaning, transformation, and normalization
- **Gold Layer** → Aggregated and curated datasets for analytics & reporting

---

## 📂 Datasets Used
- **Structured Files**:  
  - `orders_data.csv`  
  - `customers.csv`  
  - `products.csv`  

- **Unstructured Files**:  
  - `reviews.json`  
  - `social_media.json`  
  - `web_logs.json`  

---

## 🛠 Microsoft Fabric Services Used
- **Lakehouse** (Bronze, Silver, Gold)
- **Data Pipelines**
- **Shortcuts**
- **Notebooks** (PySpark / Pandas transformations)
- **Power BI Semantic Model**
- **Power BI Service for Reporting**

---

## 📜 Detailed Steps

### 1️⃣ Workspace & Architecture Setup
- Created a workspace **`Shopping Project`**.
- Selected **pre-designed Medallion Architecture task flow**.

<img width="1919" height="824" alt="image" src="https://github.com/user-attachments/assets/0eb796e0-4e0d-418a-96e2-f9f162c65a61" />

---

### 2️⃣ Bronze Layer – Data Ingestion

Created Lakehouse **`ShoppingMart_Bronze`**.

#### Structured Data
1. Saved structured pipeline as `ShoppingMart_StructuredDataIngest_BronzeLayer`.
2. Added **Copy Data Activity** (`Copy_ShoppingMart_Structured_MetaDataFiles`) for **metadata ingestion** with **HTTP Connector**.
3. Configured source API URL & tested connection ✅.
4. Added **Lookup** and **ForEach** activities to loop over structured CSV files.
5. Pipeline run → Orders file successfully created in Bronze Lakehouse.
6. All 3 CSV files successfully ingested into Bronze Lakehouse.

<img width="1846" height="760" alt="image" src="https://github.com/user-attachments/assets/96b5a6d3-6f8e-4798-924c-331c6f0ee434" />


#### Unstructured Data
1. Saved unstructured pipeline as `ShoppingMart_UnstructuredDataIngest_BronzeLayer`.
2. Modified source & destination for unstructured JSON files.
3. Configured lookup & ForEach activities.
4. Successfully ingested all 3 unstructured JSON files into Bronze Lakehouse.

---

### 3️⃣ Silver Layer – Transformation
1. Created Lakehouse **`ShoppingMart_Silver`**.
2. Developed transformation notebook **`SilverTransformation_ShoppingMartData`**.
3. Created **shortcuts** to read from Bronze Lakehouse.
4. Cleaned structured data → wrote results as parquet files in Silver Layer.
5. Created shortcuts for unstructured data → transformed & stored in Silver Layer as parquet.

<img width="1847" height="813" alt="image" src="https://github.com/user-attachments/assets/3086ee6f-aaff-46ae-9c34-1bd05b06df3a" />

---

### 4️⃣ Gold Layer – Aggregation & Curation
1. Created Lakehouse **`ShoppingMart_Gold`**.
2. Created notebook **`ShoppingMart_GoldTransformation`**.
3. Created shortcuts to Silver Layer data.
4. Performed business aggregations & transformations.
5. Wrote final curated datasets to Gold Lakehouse (Parquet format).

---

### 5️⃣ Delta Tables & Semantic Model
1. Loaded final datasets as **Delta Tables**.
2. Created a **Semantic Model** from Gold Layer tables.
3. Built relationships between fact & dimension tables.
4. Created a **Date Table** and linked it with Orders.
5. Adjusted datatypes and column formatting.

---

### 6️⃣ Power BI Reporting
1. Built Power BI report **directly in Fabric Service** on the Semantic Model.
2. Created visualizations for key KPIs, trends, and sales insights.

<img width="1848" height="787" alt="image" src="https://github.com/user-attachments/assets/3d502b96-e93c-4af7-82cd-cfbf6879f208" />

<img width="1419" height="728" alt="image" src="https://github.com/user-attachments/assets/9d9377fb-dedb-4bc0-9120-b413635b87e4" />

<img width="1354" height="524" alt="image" src="https://github.com/user-attachments/assets/5f007198-ee34-4f6f-9141-8aacda8a6ee5" />

<img width="1353" height="704" alt="image" src="https://github.com/user-attachments/assets/df9c6c5e-a326-44bb-ba51-ac77f8062ebf" />

---

### 7️⃣ Master Orchestration Pipeline
1. Created **`ShoppingMart_Master_pipeline`**.
2. Added **Invoke Pipeline** for Structured and Unstructured Ingestion.
4. Added **Notebook Activity** for Silver and Gold Layer transformations.
6. Ran the Master Pipeline → all processes executed successfully ✅.

<img width="1919" height="819" alt="image" src="https://github.com/user-attachments/assets/149cb7f5-2936-412b-91c9-a2f37b1e179b" />

---

## 📊 Final Output
- **Automated ingestion** of structured & unstructured data.
- **Clean, aggregated datasets** stored in Lakehouse.
- **Semantic model** with relationships for reporting.
- **Power BI dashboards** providing e-commerce analytics insights.

---
