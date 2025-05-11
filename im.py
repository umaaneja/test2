from app.schemas.image import ImageInDB, ImageCreate, ImageWithAnalysis

@router.get("/images/{image_id}/analysis", response_model=ImageWithAnalysis)
def get_image_with_analysis(
    image_id: int,
    db: Session = Depends(get_db)
):
    """
    Get image details with analyzed LLM response data.
    Returns:
        - Image details
        - Analysis of LLM response including:
            - total_components
            - reusable_components
            - components_details (raw components data)
    """
    db_image = get_image(db, image_id)
    if not db_image:
        raise HTTPException(status_code=404, detail="Image not found")
    
    return db_image
