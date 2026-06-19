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
```

---

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

# ⚙️ Setup Instructions

## Clone Repository

```bash
git clone https://github.com/yourusername/ai-transaction-pipeline.git
cd ai-transaction-pipeline
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

Expected:

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

# 📸 Screenshots

### CSV Upload

Add screenshot here

```text
screenshots/upload.png
```

### Job Status

Add screenshot here

```text
screenshots/status.png
```

### Report API

Add screenshot here

```text
screenshots/report.png
```

### Results API

Add screenshot here

```text
screenshots/results.png
```

### Anomaly Detection

Add screenshot here

```text
screenshots/anomalies.png
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
