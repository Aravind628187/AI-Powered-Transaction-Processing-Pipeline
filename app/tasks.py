from app.celery_app import celery

import pandas as pd

from app.database import SessionLocal

from app.crud import (
    update_job_status,
    update_job_counts,
    update_clean_count,
    save_transactions,
    save_anomalies
)

from app.services.csv_processor import clean_transactions
from app.services.anomaly_detector import detect_anomalies


@celery.task
def process_csv(job_id, file_path):

    db = SessionLocal()

    try:

        update_job_status(
            db=db,
            job_id=job_id,
            status="processing"
        )

        df = pd.read_csv(file_path)

        update_job_counts(
            db=db,
            job_id=job_id,
            raw_count=len(df)
        )

        clean_df = clean_transactions(file_path)

        update_clean_count(
            db=db,
            job_id=job_id,
            clean_count=len(clean_df)
        )

        save_transactions(
            db=db,
            job_id=job_id,
            records=clean_df
        )

        anomalies = detect_anomalies(clean_df)

        save_anomalies(
            db=db,
            job_id=job_id,
            anomalies=anomalies
        )

        update_job_status(
            db=db,
            job_id=job_id,
            status="completed"
        )

        print(f"Job {job_id} completed")

    except Exception as e:

        update_job_status(
            db=db,
            job_id=job_id,
            status="failed",
            error_message=str(e)
        )

        print(f"Job {job_id} failed: {e}")

    finally:
        db.close()