from sqlalchemy.orm import Session
from datetime import datetime

from app.models import Job, Anomaly, Transaction


def create_job(db: Session, filename: str):
    job = Job(
        filename=filename,
        status="pending"
    )

    db.add(job)
    db.commit()
    db.refresh(job)

    return job


def get_job(db: Session, job_id: int):
    return db.query(Job).filter(
        Job.id == job_id
    ).first()


def update_job_counts(
    db: Session,
    job_id: int,
    raw_count: int
):
    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if job:
        job.row_count_raw = raw_count
        db.commit()
        db.refresh(job)

    return job


def update_clean_count(
    db: Session,
    job_id: int,
    clean_count: int
):
    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if job:
        job.row_count_clean = clean_count
        db.commit()
        db.refresh(job)

    return job


def update_job_status(
    db: Session,
    job_id: int,
    status: str,
    error_message: str = None
):
    job = db.query(Job).filter(
        Job.id == job_id
    ).first()

    if job:
        job.status = status

        if status == "completed":
            job.completed_at = datetime.utcnow()

        if status == "failed":
            job.error_message = error_message

        db.commit()
        db.refresh(job)

    return job


def save_anomalies(
    db: Session,
    job_id: int,
    anomalies: list
):
    for anomaly in anomalies:

        item = Anomaly(
            job_id=job_id,
            txn_id=anomaly["txn_id"],
            reason=anomaly["reason"]
        )

        db.add(item)

    db.commit()


def get_anomalies_by_job(
    db: Session,
    job_id: int
):
    return db.query(Anomaly).filter(
        Anomaly.job_id == job_id
    ).all()


def get_all_jobs(
    db: Session,
    status: str = None
):
    query = db.query(Job)

    if status:
        query = query.filter(
            Job.status == status
        )

    return query.all()


def save_transactions(
    db: Session,
    job_id: int,
    records
):
    print("Saving transactions...")
    print("Rows =", len(records))

    for _, row in records.iterrows():

        tx = Transaction(
            job_id=job_id,
            txn_id=str(row["txn_id"]),
            amount=float(row["amount"]),
            merchant=str(row["merchant"]),
            category=str(row["category"]),
            currency=str(row["currency"])
        )

        db.add(tx)

    db.commit()

    print("Transactions saved successfully!")

def get_transactions_by_job(
    db: Session,
    job_id: int
):
    return db.query(Transaction).filter(
        Transaction.job_id == job_id
    ).all()

def get_transaction_count_by_job(
    db: Session,
    job_id: int
):
    return db.query(Transaction).filter(
        Transaction.job_id == job_id
    ).count()