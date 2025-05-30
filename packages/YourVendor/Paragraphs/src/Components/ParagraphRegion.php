<?php

namespace YourVendor\Paragraphs\Components;

use Illuminate\View\Component;
use YourVendor\Paragraphs\Models\Paragraph;

class ParagraphRegion extends Component
{
    public $paragraphs;

    public function __construct($page, string $region)
    {
        $this->paragraphs = $page->paragraphs()->region($region)->get();
    }

    public function render()
    {
        return view('paragraphs::components.paragraph-region');
    }
}
