from app.db.session import SessionLocal
from app.services.image_service import ImageService

async def your_existing_processing_loop():
    db = SessionLocal()
    image_service = ImageService(db)
    
    try:
        for image_id, llm_response in your_llm_results:  # Your existing loop
            try:
                # Your existing processing logic...
                
                # Update status within the same DB session
                success = await image_service.update_llm_status(
                    image_id=image_id,
                    llm_response=llm_response,
                    is_success=True
                )
                
                if not success:
                    print(f"Failed to update image {image_id}")
                    
            except Exception as e:
                # Mark as failed if error occurs
                await image_service.update_llm_status(
                    image_id=image_id,
                    llm_response=str(e),
                    is_success=False
                )
                raise  # Re-raise if you want to stop the loop
                
    finally:
        db.close()  # Single session for all updates
