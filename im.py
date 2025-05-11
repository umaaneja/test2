from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.sql import func
from app.db.base_class import Base

class Image(Base):
    __tablename__ = 'tbl_images'

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey('tbl_projects.id', ondelete="CASCADE"), nullable=False)
    filename = Column(String(255), nullable=False)
    filepath = Column(String(512), nullable=False)
    content_type = Column(String(100), nullable=False)
    upload_date = Column(DateTime, server_default=func.now())
    file_size = Column(Integer)
    width = Column(Integer)
    height = Column(Integer)
    alt_text = Column(String(255))
    llm_processed = Column(Boolean, nullable=False, server_default='0')
    llm_response = Column(Text)
