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
| `kinesis_producer.py` | Python script to simulate streaming sales data |
| `glue_job_script.py` | AWS Glue PySpark script to clean and transform data |
| `athena_queries.sql` | Athena SQL queries for analysis |
| `sample_raw_data.json` | Example raw Kinesis record |
| `sample_clean_data.json` | Output after Glue transformation |
| `dashboard_screenshot.png` | (Optional) QuickSight dashboard snapshot |
| `architecture-diagram.png` | (Optional) Architecture of the AWS pipeline |

---

## 📈 Sample Output

*Include screenshots of your Athena queries or QuickSight dashboard here.*

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
