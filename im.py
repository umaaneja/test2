class LLMResponseAnalysis(BaseModel):
    total_components: int
    reusable_components: int
    components_details: Optional[Dict[str, Any]] = None

class ImageWithAnalysis(ImageInDB):
    llm_analysis: Optional[LLMResponseAnalysis] = None

    @validator('llm_analysis', pre=True, always=True)
    def parse_llm_response(cls, v, values):
        if 'llm_response' not in values or not values['llm_response']:
            return None
        
        try:
            response_data = json.loads(values['llm_response'])
            analysis = {
                'total_components': len(response_data.get('components', [])),
                'reusable_components': sum(
                    1 for comp in response_data.get('components', []) 
                    if comp.get('is_reusable', False)
                ),
                'components_details': response_data.get('components')
            }
            return LLMResponseAnalysis(**analysis)
        except (json.JSONDecodeError, AttributeError):
            return None
