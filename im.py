image_service.py


from sqlalchemy.orm import Session
from app.models.image import Image
from app.crud.image import (
    get_image,
    update_image_llm_data,
    get_images_by_project
)

class ImageService:
    def __init__(self, db: Session):
        self.db = db

    async def update_llm_status(
        self,
        image_id: int,
        llm_response: str,
        is_success: bool = True
    ) -> bool:
        """Updates LLM processing status (internal use only)"""
        updated = await update_image_llm_data(
            db=self.db,
            image_id=image_id,
            llm_processed=is_success,
            llm_response=llm_response
        )
        return updated is not None

    async def get_unprocessed_images(self, project_id: int) -> list[Image]:
        """For LLM service to fetch images needing processing"""
        return get_images_by_project(
            db=self.db,
            project_id=project_id
        ).filter(Image.llm_processed == False).all()
