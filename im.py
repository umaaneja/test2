from app.schemas.image import ImageInDB, ImageCreate, ImageLLMUpdate


@router.patch("/images/{image_id}/llm", response_model=ImageInDB)
def update_llm_processing_result(
    image_id: int,
    llm_data: ImageLLMUpdate,
    db: Session = Depends(get_db)
):
    db_image = get_image(db, image_id)
    if not db_image:
        raise HTTPException(status_code=404, detail="Image not found")
    return update_image_llm_data(db, image_id=image_id, llm_data=llm_data)
