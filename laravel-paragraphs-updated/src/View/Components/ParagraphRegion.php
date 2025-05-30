<?php

namespace YourVendor\Paragraphs\View\Components;

use Illuminate\View\Component;
use YourVendor\Paragraphs\Models\Paragraph;

class ParagraphRegion extends Component
{
    public $paragraphs;

    public function __construct($page, string $region)
    {
        $pageId = is_numeric($page) ? $page : $page->id;

        $this->paragraphs = Paragraph::query()
            ->where('page_id', $pageId)
            ->region($region)
            ->with('paragraphable')
            ->orderBy('position')
            ->get();
    }

    public function render()
    {
        return view('paragraphs::components.paragraph-region');
    }
}
