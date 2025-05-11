from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ImageBase(BaseModel):
    project_id: int
    filename: str
    filepath: str
    content_type: str

class ImageCreate(ImageBase):
    file_size: int
    width: Optional[int] = None
    height: Optional[int] = None
    original_filename: Optional[str] = None

class ImageUpdate(BaseModel):
    alt_text: Optional[str] = None
    llm_processed: Optional[bool] = None
    llm_response: Optional[str] = None

class ImageInDB(ImageBase):
    id: int
    upload_date: datetime
    file_size: int
    width: Optional[int]
    height: Optional[int]
    alt_text: Optional[str]
    llm_processed: bool
    llm_response: Optional[str]

    class Config:
        orm_mode = True

class ImageLLMUpdate(BaseModel):
    llm_processed: bool
    llm_response: str
