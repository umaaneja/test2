async def update_llm_processing(
    db: Session,
    image_id: int,
    processed: bool,
    response: str
) -> Optional[Image]:
    """Direct database update without Pydantic overhead"""
    image = db.query(Image).filter(Image.id == image_id).first()
    if not image:
        return None
    
    image.llm_processed = processed
    image.llm_response = response
    db.commit()
    db.refresh(image)
    return image
