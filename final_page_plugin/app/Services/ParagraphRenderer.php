<?php
namespace App\Services;

use YourVendor\Paragraphs\Models\Paragraph;

class ParagraphRenderer
{
    public static function getByPage($pageId)
    {
        return Paragraph::where('page_id', $pageId)
            ->orderBy('region')
            ->orderBy('position')
            ->get()
            ->groupBy('region');
    }
}
