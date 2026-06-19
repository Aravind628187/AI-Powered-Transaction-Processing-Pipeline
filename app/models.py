from sqlalchemy import Column,Integer,String,DateTime
from datetime import datetime
from app.database import Base
from sqlalchemy import Float


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String)

    status = Column(String, default="pending")

    row_count_raw = Column(Integer, default=0)

    row_count_clean = Column(Integer, default=0)

    created_at = Column(DateTime, default=datetime.utcnow)

    completed_at = Column(DateTime, nullable=True)

    error_message = Column(String, nullable=True)

class Anomaly(Base):
    __tablename__ = "anomalies"

    id = Column(Integer, primary_key=True, index=True)

    job_id = Column(Integer)

    txn_id = Column(String)

    reason = Column(String)

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)

    job_id = Column(Integer)

    txn_id = Column(String)

    amount = Column(Float)

    merchant = Column(String)

    category = Column(String)

    currency = Column(String)