from app.services.image_service import ImageService

class LLMService:
    def __init__(self, db: Session):
        self.image_service = ImageService(db)

    async def process_images(self, project_id: int):
        # Get only unprocessed images
        images = await self.image_service.get_unprocessed_images(project_id)
        
        for image in images:
            try:
                # Your LLM processing logic
                result = await self._call_llm_api(image.filepath)
                
                # Update status via ImageService
                await self.image_service.update_llm_status(
                    image_id=image.id,
                    llm_response=result
                )
            except Exception as e:
                await self.image_service.update_llm_status(
                    image_id=image.id,
                    llm_response=str(e),
                    is_success=False
                )
