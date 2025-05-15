from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database.database import Base

class GeneratedProject(Base):
    __tablename__ = "projects"
    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, unique=True, index=True)
    prompt = Column(String)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    error_log = Column(String, nullable=True)