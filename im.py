response_data = json.loads(values['llm_response'])
components = response_data.get('components', [])

global_count = 0
component_details = []

  for comp in components:
    if not isinstance(comp, dict):
        continue
     element_type = comp.get('element_type', '').lower()
     if element_type == "global":
        global_count += 1
                        
