from sqlalchemy.orm import Session
import os
import pandas as pd
from app.services.csv_processor import clean_transactions
from app.crud import save_transactions
from app.crud import (
    create_job,
    get_job,
    update_job_counts,
    update_clean_count
)

from app.crud import (
    create_job,
    get_job,
    update_job_counts,
    update_clean_count,
    save_anomalies,
    get_anomalies_by_job
)

from app.crud import (
    create_job,
    get_job,
    update_job_counts,
    update_clean_count,
    save_anomalies,
    get_anomalies_by_job,
    update_job_status
)
from app.crud import get_all_jobs
from app.services.anomaly_detector import detect_anomalies

from fastapi import APIRouter, UploadFile, File, Depends, HTTPException

from app.dependencies import get_db
from app.crud import create_job, get_job, update_job_counts
from app.crud import save_anomalies
from app.services.anomaly_detector import detect_anomalies
from app.crud import get_transactions_by_job
from app.crud import get_transaction_count_by_job
from app.services.llm_summary import generate_summary
from app.tasks import process_csv

router = APIRouter()

UPLOAD_DIR = "uploads"


@router.post("/jobs/upload")
async def upload_csv(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:

        # Create uploads folder if not exists
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        # Save uploaded file
        file_path = os.path.join(
            UPLOAD_DIR,
            file.filename
        )

        with open(file_path, "wb") as buffer:
            content = await file.read()
            buffer.write(content)

        # Create job record
        job = create_job(
            db=db,
            filename=file.filename
        )

        # Start background processing
        process_csv.delay(
            job.id,
            file_path
        )

        return {
            "job_id": job.id,
            "filename": job.filename,
            "status": "pending",
            "message": "CSV uploaded successfully. Processing started in background."
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Upload failed: {str(e)}"
        )

@router.get("/jobs/{job_id}/status")
def job_status(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = get_job(db, job_id)

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    return {
        "job_id": job.id,
        "filename": job.filename,
        "status": job.status,
        "row_count_raw": job.row_count_raw,
        "row_count_clean": job.row_count_clean,
        "completed_at": job.completed_at,
        "error_message": job.error_message
    }

@router.get("/test/anomalies")
def test_anomalies():

    file_path = "uploads/transactions.csv"

    clean_df = clean_transactions(file_path)

    anomalies = detect_anomalies(clean_df)

    return {
        "count": len(anomalies),
        "anomalies": anomalies[:5]
    }

@router.get("/jobs/{job_id}/anomalies")
def get_job_anomalies(
    job_id: int,
    db: Session = Depends(get_db)
):

    anomalies = get_anomalies_by_job(
        db=db,
        job_id=job_id
    )

    return {
        "job_id": job_id,
        "count": len(anomalies),
        "anomalies": [
            {
                "txn_id": a.txn_id,
                "reason": a.reason
            }
            for a in anomalies
        ]
    }

@router.get("/jobs/{job_id}/summary")
def job_summary(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = get_job(db, job_id)

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    anomalies = get_anomalies_by_job(
        db=db,
        job_id=job_id
    )

    success_rate = 0

    if job.row_count_raw > 0:
        success_rate = round(
            (job.row_count_clean / job.row_count_raw) * 100,
            2
        )

    return {
        "job_id": job.id,
        "raw_records": job.row_count_raw,
        "clean_records": job.row_count_clean,
        "anomalies": len(anomalies),
        "success_rate": success_rate
    }

@router.get("/jobs")
def list_jobs(
    status: str = None,
    db: Session = Depends(get_db)
):

    jobs = get_all_jobs(
        db=db,
        status=status
    )

    return [
        {
            "job_id": job.id,
            "filename": job.filename,
            "status": job.status,
            "row_count_raw": job.row_count_raw,
            "row_count_clean": job.row_count_clean,
            "created_at": job.created_at
        }
        for job in jobs
    ]

@router.get("/jobs/{job_id}/transactions")
def get_job_transactions(
    job_id: int,
    db: Session = Depends(get_db)
):

    transactions = get_transactions_by_job(
        db=db,
        job_id=job_id
    )

    return {
        "job_id": job_id,
        "count": len(transactions),
        "transactions": [
            {
                "txn_id": tx.txn_id,
                "amount": tx.amount,
                "merchant": tx.merchant,
                "category": tx.category,
                "currency": tx.currency
            }
            for tx in transactions
        ]
    }

@router.get("/jobs/{job_id}/report")
def job_report(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = get_job(db, job_id)

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    anomalies = get_anomalies_by_job(
        db=db,
        job_id=job_id
    )

    tx_count = get_transaction_count_by_job(
        db=db,
        job_id=job_id
    )

    success_rate = 0

    if job.row_count_raw > 0:
        success_rate = round(
            (job.row_count_clean / job.row_count_raw) * 100,
            2
        )

    return {
        "job_id": job.id,
        "filename": job.filename,
        "status": job.status,
        "raw_records": job.row_count_raw,
        "clean_records": job.row_count_clean,
        "transactions": tx_count,
        "anomalies": len(anomalies),
        "success_rate": success_rate,
        "completed_at": job.completed_at
    }

@router.get("/jobs/{job_id}/results")
def get_job_results(
    job_id: int,
    db: Session = Depends(get_db)
):

    job = get_job(db, job_id)

    if not job:
        raise HTTPException(
            status_code=404,
            detail="Job not found"
        )

    transactions = get_transactions_by_job(
        db=db,
        job_id=job_id
    )

    anomalies = get_anomalies_by_job(
        db=db,
        job_id=job_id
    )

    category_breakdown = {}

    for tx in transactions:

        if tx.category not in category_breakdown:
            category_breakdown[tx.category] = 0

        category_breakdown[tx.category] += tx.amount

    total_inr = sum(
        tx.amount
        for tx in transactions
        if tx.currency == "INR"
    )

    total_usd = sum(
        tx.amount
        for tx in transactions
        if tx.currency == "USD"
    )

    merchant_totals = {}

    for tx in transactions:

        merchant_totals[tx.merchant] = (
            merchant_totals.get(
                tx.merchant,
                0
            ) + tx.amount
        )

    top_merchants = sorted(
        merchant_totals,
        key=merchant_totals.get,
        reverse=True
    )[:3]

    try:

        llm_summary = generate_summary(
            total_inr,
            total_usd,
            top_merchants,
            len(anomalies)
        )

    except Exception as e:

        llm_summary = (
            f"Summary generation failed: {str(e)}"
        )

    return {

        "job_id": job.id,

        "status": job.status,

        "transactions": [

            {
                "txn_id": tx.txn_id,
                "amount": tx.amount,
                "merchant": tx.merchant,
                "category": tx.category,
                "currency": tx.currency
            }

            for tx in transactions
        ],

        "anomalies": [

            {
                "txn_id": a.txn_id,
                "reason": a.reason
            }

            for a in anomalies
        ],

        "category_breakdown": category_breakdown,

        "total_inr": total_inr,

        "total_usd": total_usd,

        "top_merchants": top_merchants,

        "llm_summary": llm_summary
    }