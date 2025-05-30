@foreach($paragraphs as $para)
    @php
        $viewName = 'paragraphs.' . strtolower(class_basename($para->paragraphable_type));
    @endphp
    @includeIf($viewName, ['data' => $para->paragraphable, 'region' => $para->region])
@endforeach
