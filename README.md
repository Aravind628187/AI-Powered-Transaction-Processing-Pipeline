<<<<<<< HEAD
# 🚀 AI Transaction Processing Pipeline

An AI-powered transaction processing system built using **FastAPI, PostgreSQL, Redis, Celery, Pandas, and Gemini AI**. The application processes transaction CSV files asynchronously, performs data cleaning, detects anomalies, generates analytics, and provides AI-powered summaries through REST APIs.

---

# 📌 Project Overview

The AI Transaction Processing Pipeline automates the processing of financial transaction data.

### Features

* Upload transaction CSV files
* Background processing using Celery
* Data cleaning and validation
* Transaction storage in PostgreSQL
* Anomaly detection
* Category-wise spending analysis
* Job tracking and monitoring
* AI-generated transaction summaries
* REST APIs with Swagger documentation

---

# 🏗️ Architecture Diagram

```text
                +------------------+
                |     CSV Upload   |
                +--------+---------+
                         |
                         v
                +------------------+
                |     FastAPI      |
                +--------+---------+
                         |
                         v
                +------------------+
                |  Celery Worker   |
                +--------+---------+
                         |
       +----------------+----------------+
       |                                 |
       v                                 v
+--------------+                +----------------+
| Data Cleaning|                | Anomaly Check |
+------+-------+                +-------+--------+
       |                                |
       +---------------+----------------+
                       |
                       v
              +------------------+
              | PostgreSQL DB    |
              +--------+---------+
                       |
                       v
              +------------------+
              | Analytics Engine |
              +--------+---------+
                       |
                       v
              +------------------+
              | Gemini AI Summary|
              +--------+---------+
                       |
                       v
              +------------------+
              | REST APIs        |
              +------------------+

# AI-Powered Transaction Processing Pipeline

An intelligent transaction processing system built using FastAPI, PostgreSQL, Redis, Celery, Docker, and Gemini AI.

The system uploads transaction CSV files, cleans data, detects anomalies, stores records in PostgreSQL, generates reports, and produces AI-powered summaries using Google Gemini.

---

## Features

### CSV Processing
- Upload transaction CSV files
- Background processing using Celery
- Redis task queue

### Data Cleaning
- Remove invalid records
- Normalize transaction data
- Generate clean transaction dataset

### Transaction Storage
- Store processed transactions in PostgreSQL
- Track job metadata and processing status

### Anomaly Detection
- Detect abnormal transactions
- Flag transactions exceeding 3x account median spending

### Reporting
- Processing statistics
- Success rate calculation
- Category-wise spending breakdown
- Merchant-wise spending analysis

### AI Summary
- Generate transaction insights using Google Gemini
- Top merchants
- Total INR spend
- Total USD spend
- Anomaly count summary

### Docker Support
- FastAPI container
- Celery Worker container
- PostgreSQL container
- Redis container

---

# Architecture

```text
                +----------------+
                |   CSV Upload   |
                +--------+-------+
                         |
                         v
                +----------------+
                |    FastAPI     |
                +--------+-------+
                         |
                         v
                +----------------+
                |     Celery     |
                +--------+-------+
                         |
         +---------------+---------------+
         |                               |
         v                               v
+----------------+             +----------------+
| Data Cleaning  |             | Anomaly Check  |
+----------------+             +----------------+
         |                               |
         +---------------+---------------+
                         |
                         v
                +----------------+
                | PostgreSQL DB  |
                +----------------+
                         |
                         v
                +----------------+
                | Gemini AI LLM  |
                +----------------+
                         |
                         v
                +----------------+
                | Final Report   |
                +----------------+
```

---

<<<<<<< HEAD
# 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* SQLAlchemy

### Database

* PostgreSQL

### Background Processing

* Celery
* Redis

### Data Processing

* Pandas

### AI Integration

* Google Gemini AI

### API Documentation

* Swagger UI

---

# 📂 Project Structure

```text
ai-transaction-pipeline/
│
├── app/
│   ├── api/
│   │   └── jobs.py
│   │
│   ├── services/
│   │   ├── csv_processor.py
│   │   ├── anomaly_detector.py
│   │   └── llm_summary.py
│   │
│   ├── celery_app.py
│   ├── tasks.py
│   ├── crud.py
│   ├── models.py
│   ├── database.py
│   ├── dependencies.py
│   └── main.py
│
├── uploads/
├── requirements.txt
└── README.md
```

---

# 🔥 API Endpoints

# Tech Stack

## Backend

- FastAPI
- SQLAlchemy
- PostgreSQL

## Background Tasks

- Celery
- Redis

## Data Processing

- Pandas

## AI

- Google Gemini API

## DevOps

- Docker
- Docker Compose

---

# API Endpoints


## Upload CSV

```http
POST /jobs/upload
```

<<<<<<< HEAD
Uploads a CSV file and starts background processing.

---

## Job Status

```http
GET /jobs/{job_id}/status
```

<<<<<<< HEAD
Returns processing status and statistics.

---

## List Jobs

## All Jobs


```http
GET /jobs
```

Returns all jobs.

---

## Transactions

```http
GET /jobs/{job_id}/transactions
```

<<<<<<< HEAD
Returns cleaned transaction records.

---

## Anomalies

```http
GET /jobs/{job_id}/anomalies
```


Returns detected anomalies.

---

## Summary

```http
GET /jobs/{job_id}/summary
```

## Report

```http
GET /jobs/{job_id}/report
```


Returns analytics report.

Example:

```json
{
  "job_id": 20,
  "raw_records": 95,
  "clean_records": 85,
  "transactions": 85,
  "anomalies": 5,
  "success_rate": 89.47
}
```

---

## Results

```http
GET /jobs/{job_id}/results
```


Returns:

* Transactions
* Anomalies
* Category Breakdown
* Total INR Spend
* Total USD Spend
* Top Merchants
* AI Summary

---

# ⚙️ Setup Instructions

---

# Setup Instructions


## Clone Repository

```bash

git clone https://github.com/yourusername/ai-transaction-pipeline.git
cd ai-transaction-pipeline
git clone https://github.com/Aravind628187/AI-Powered-Transaction-Processing-Pipeline.git

cd AI-Powered-Transaction-Processing-Pipeline

```

---

## Create Virtual Environment

```bash

python -m venv venu
source venu/bin/activate
```

Windows:

```bash
venu\Scripts\activate

python -m venv venv

source venv/bin/activate

```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start PostgreSQL

Ensure PostgreSQL is running.

---

## Start Redis

## Run Redis

```bash
redis-server
```


Verify:

```bash
redis-cli ping
```

Expected:

```text
PONG
```

---

## Start Celery Worker

---

## Run Celery Worker


```bash
celery -A app.tasks worker --loglevel=info
```

---

## Start FastAPI

## Run FastAPI


```bash
uvicorn app.main:app --reload
```

---

<<<<<<< HEAD
## Open Swagger

## Swagger UI

```text
http://127.0.0.1:8000/docs
```

---

# 📈 Sample Output

```json
{
  "job_id": 20,
  "status": "completed",
  "raw_records": 95,
  "clean_records": 85,
  "anomalies": 5,
  "success_rate": 89.47
}

# Docker Setup

```bash
docker compose up --build
```

Swagger:

```text
http://localhost:8000/docs
```

---

<<<<<<< HEAD
# 🎯 Future Enhancements

* Docker Containerization
* Kubernetes Deployment
* JWT Authentication
* User Management
* Real-Time Dashboard
* Email Notifications
* Advanced Fraud Detection Models
* Kafka Event Streaming
* Multi-file Batch Processing
* Cloud Deployment (AWS)

---

# 👨‍💻 Author

**Aravind Kumar**

* GitHub: https://github.com/Aravind628187
* LinkedIn: https://www.linkedin.com/in/chinthamanuaravindkumar/

---

# ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.

# Sample Workflow

1. Upload CSV
2. Create Job
3. Background Processing Starts
4. Clean Data
5. Store Transactions
6. Detect Anomalies
7. Generate AI Summary
8. View Results & Reports

---

# Future Enhancements

- JWT Authentication
- User Management
- Dashboard UI (React)
- Real-time Notifications
- Multi-file Upload
- Kafka Integration
- ML-based Fraud Detection
- Cloud Deployment (AWS)

---

# Author

**Aravind Kumar**

B.Tech CSE (AI & ML)

GitHub:
https://github.com/Aravind628187


---

