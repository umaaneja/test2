<?php
namespace App\Http\Controllers;

use App\Models\Page;
use Illuminate\Http\Request;

class PageController extends Controller
{
    public function show($url)
    {
        $page = Page::with(['contentType.fields', 'fieldValues', 'paragraphs' => function($q) {
            $q->orderBy('order');
        }])->where('url', $url)->firstOrFail();

        $paragraphsByRegion = $page->paragraphs->groupBy('region');

        return view('pages.show', compact('page', 'paragraphsByRegion'));
    }
}
