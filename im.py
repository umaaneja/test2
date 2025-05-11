from app.schemas.image import ImageInDB, ImageCreate, ImageWithAnalysis



@router.get("/projects/{project_id}/analysis", response_model=List[ImageWithAnalysis])
def get_project_images_with_analysis(
    project_id: int,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Get all images for a project with analyzed LLM response data.
    Returns:
        - List of image details with:
            - Image metadata
            - Analysis of LLM response including:
                - total_components
                - reusable_components
                - components_details
            - raw_llm_response
    """
    images = get_images_by_project(db, project_id=project_id, skip=skip, limit=limit)
    if not images:
        raise HTTPException(
            status_code=404,
            detail=f"No images found for project {project_id}"
        )
    return images
