<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use YourVendor\Paragraphs\Models\Paragraph;

class GalleryBlock extends Model
{
    protected $fillable = ['title', 'images'];

    public function paragraph()
    {
        return $this->morphOne(Paragraph::class, 'paragraphable');
    }
}
