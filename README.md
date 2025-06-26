# Real-Time Data Engineering Pipeline on AWS 🚀

This project implements a real-time data ingestion and analytics pipeline using AWS services including **Kinesis**, **Lambda**, **S3**, **Glue**, **Athena**, and **QuickSight**.

---

## 📌 Project Overview

- Simulates real-time sales data streaming through **Amazon Kinesis**
- Processes records using **AWS Lambda** and stores raw data in **S3**
- Transforms and cleans data using **AWS Glue ETL jobs**
- Queries structured data with **Amazon Athena**
- Visualizes insights with **Amazon QuickSight**

---

## 🛠 Tech Stack

- **AWS Kinesis** – Real-time data ingestion
- **AWS Lambda** – Serverless compute for data processing
- **Amazon S3** – Raw and cleaned data lake storage
- **AWS Glue** – ETL jobs and schema mapping
- **AWS Athena** – SQL querying on S3 data
- **Amazon QuickSight** – Dashboards and data visualization
- **Python**, **PySpark**, **SQL**

---

## 📂 Repository Structure

| File | Description |
|------|-------------|
| `simulate_sales.py` | Python script to simulate streaming sales data |
| `glue_job_script.py` | AWS Glue PySpark script to clean and transform data |
| `athena_queries.sql` | Athena SQL queries for analysis |
| `Sample_raw_data.json` | Example raw Kinesis record |
| `Sample_Clean_data.json` | Output after Glue transformation |
| `Sales_Dashboard.pdf` | QuickSight dashboard snapshot |
| `architecture-diagram.png` | Architecture of the AWS pipeline |

---

## 📈 Sample Output

![Architecture Diagram](images/architecture.png)

---

## 🔐 IAM & Permissions

IAM roles were configured with access to:
- `AmazonKinesisFullAccess`
- `AWSLambdaExecute`
- `AmazonS3FullAccess`
- `AWSGlueServiceRole`
- `AmazonAthenaFullAccess`
- `AmazonQuickSightFullAccess`

---

## 📬 Contact

Feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/pavan-kumar-chintala-1879b4228/) or message me with any questions!
