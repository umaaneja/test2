<h1>{{ \$content->title }}</h1>
<p>{{ \$content->body }}</p>

@if(!empty(\$paragraphs['content']))
    @foreach(\$paragraphs['content'] as \$paragraph)
        @includeIf('paragraphs.types.' . \$paragraph->paragraphable_type, [
            'data' => \$paragraph->paragraphable
        ])
    @endforeach
@endif
