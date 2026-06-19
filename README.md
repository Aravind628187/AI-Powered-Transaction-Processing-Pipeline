# 🚀 AI Transaction Processing Pipeline

An AI-powered transaction processing system built using **FastAPI, PostgreSQL, Redis, Celery, Pandas, Docker, and Gemini AI**. The application processes transaction CSV files asynchronously, performs data cleaning, detects anomalies, generates analytics, and provides AI-powered summaries through REST APIs.

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
* AI-generated transaction summaries using Gemini AI
* REST APIs with Swagger documentation
* Dockerized deployment using Docker Compose

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
              | Docker Compose   |
              +--------+---------+
                       |
                       v
              +------------------+
              | REST APIs        |
              +------------------+
```

---

# 🛠️ Tech Stack

## Backend

* Python
* FastAPI
* SQLAlchemy

## Database

* PostgreSQL

## Background Processing

* Celery
* Redis

## Data Processing

* Pandas

## AI Integration

* Google Gemini AI

## Containerization

* Docker
* Docker Compose

## API Documentation

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
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── requirements.txt
└── README.md
```

---

# 🔥 API Endpoints

## Upload CSV

```http
POST /jobs/upload
```

Uploads a CSV file and starts background processing.

---

## Job Status

```http
GET /jobs/{job_id}/status
```

Returns processing status and statistics.

---

## List Jobs

```http
GET /jobs
```

Returns all jobs.

---

## Transactions

```http
GET /jobs/{job_id}/transactions
```

Returns cleaned transaction records.

---

## Anomalies

```http
GET /jobs/{job_id}/anomalies
```

Returns detected anomalies.

---

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

# ⚙️ Local Setup Instructions

## Clone Repository

```bash
git clone https://github.com/Aravind628187/AI-Powered-Transaction-Processing-Pipeline.git
cd AI-Powered-Transaction-Processing-Pipeline
```

---

## Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
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

```bash
redis-server
```

Verify:

```bash
redis-cli ping
```

Expected Output:

```text
PONG
```

---

## Start Celery Worker

```bash
celery -A app.tasks worker --loglevel=info
```

---

## Start FastAPI

```bash
uvicorn app.main:app --reload
```

---

## Open Swagger

```text
http://127.0.0.1:8000/docs
```

---

# 🐳 Docker Setup

## Build and Run

```bash
docker compose up --build
```

---

## Run in Detached Mode

```bash
docker compose up -d
```

---

## Stop Containers

```bash
docker compose down
```

---

## Services Started

* FastAPI API Server
* PostgreSQL Database
* Redis Queue
* Celery Worker

---

## Swagger URL

```text
http://localhost:8000/docs
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
```

---

# ✅ Current Status

Implemented Features:

* FastAPI REST APIs
* PostgreSQL Integration
* Redis Queue
* Celery Background Processing
* CSV Upload & Cleaning
* Transaction Analytics
* Anomaly Detection
* Gemini AI Summary Generation
* Swagger Documentation
* Docker Support
* Docker Compose Support

---

# 🎯 Future Enhancements

* JWT Authentication
* User Management
* Role-Based Access Control (RBAC)
* Real-Time Dashboard
* Email Notifications
* Advanced Fraud Detection Models
* Kafka Event Streaming
* Multi-file Batch Processing
* Kubernetes Deployment
* AWS Cloud Deployment

---

# 👨‍💻 Author

**Aravind Kumar**

* GitHub: https://github.com/Aravind628187

---

# ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.
