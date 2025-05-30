<div class="gallery-block" style="margin-bottom: 2rem;">
    <h3>{{ $data->title }}</h3>
    <div class="gallery-grid" style="display: flex; gap: 1rem; flex-wrap: wrap;">
        @foreach(json_decode($data->images, true) as $img)
            <img src="{{ $img }}" alt="" style="width: 150px; height: auto; border-radius: 8px; box-shadow: 0 2px 6px rgba(0,0,0,0.1);">
        @endforeach
    </div>
</div>
