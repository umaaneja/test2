<?php
namespace App\Http\Controllers;

use App\Models\Page;
use Illuminate\Support\Str;
use Illuminate\Http\Request;
use App\Services\ParagraphRenderer;

class PageController extends Controller
{
    public function show($url_alias)
    {
        $page = Page::where('url_alias', $url_alias)->firstOrFail();

        $modelClass = 'App\\Models\\' . Str::studly($page->content_type);
        $content = class_exists($modelClass) ? $modelClass::find($page->content_id) : null;

        $paragraphs = ParagraphRenderer::getByPage($page->id);

        return view("content.{$page->content_type}.show", compact('page', 'content', 'paragraphs'));
    }
}
