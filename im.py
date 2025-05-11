image_processing.py

class ImageProcessingService:
    def __init__(self, db: Session):
        self.db = db

    async def mark_as_processed(
        self,
        image_id: int,
        llm_response: str,
        success: bool = True
    ) -> bool:
        """Service method for internal use only"""
        updated = await update_llm_processing(
            db=self.db,
            image_id=image_id,
            processed=success,
            response=llm_response
        )
        return updated is not None
