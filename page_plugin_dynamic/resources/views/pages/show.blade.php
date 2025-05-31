@extends('layouts.app')

@section('content')
<h1>{{ $page->contentType->name }} Page: {{ $page->url }}</h1>

<div class="dynamic-fields">
    @foreach($page->contentType->fields as $field)
        <div class="field">
            <label>{{ ucfirst($field->name) }}:</label>
            <div class="value">
                @php
                    $value = $page->getFieldValue($field->name);
                @endphp
                @if($field->field_type === 'textarea')
                    <p>{!! nl2br(e($value)) !!}</p>
                @else
                    {{ $value }}
                @endif
            </div>
        </div>
    @endforeach
</div>

@foreach(['content', 'sidebar', 'footer'] as $region)
    @if(isset($paragraphsByRegion[$region]))
        <div class="region region-{{ $region }}">
            @foreach($paragraphsByRegion[$region] as $paragraph)
                {{-- Paragraph partial views from Paragraph plugin --}}
                @includeIf("paragraphs.types.{$paragraph->type}", ['paragraph' => $paragraph])
            @endforeach
        </div>
    @endif
@endforeach
@endsection
