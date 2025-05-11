from app.services.image_processing import ImageProcessingService
  db = SessionLocal()
    service = ImageProcessingService(db)

 success = await service.mark_as_processed(
            image_id=test_image_id,
            llm_response=test_response,
            success=True
        )
        
