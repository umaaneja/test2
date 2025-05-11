def update_image_llm_data(db: Session, image_id: int, llm_data: ImageLLMUpdate) -> Optional[Image]:
    db_image = get_image(db, image_id)
    if not db_image:
        return None
    db_image.llm_processed = llm_data.llm_processed
    db_image.llm_response = llm_data.llm_response
    db.commit()
    db.refresh(db_image)
    return db_image
