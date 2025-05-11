from app.services.image_service import ImageService


async def update_llm_status(
    image_id: int,
    llm_response: str,
    is_success: bool = True
):
    db = SessionLocal()
    try:
        image_service = ImageService(db)
        success = await image_service.update_llm_status(
            image_id=image_id,
            llm_response=llm_response,
            is_success=is_success
        )
        if not success:
            raise HTTPException(status_code=404, detail="Image not found")
        return {"status": "updated"}
    finally:
        db.close()
