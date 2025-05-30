<?php

namespace YourVendor\Paragraphs\Models;

use Illuminate\Database\Eloquent\Model;

class Paragraph extends Model
{
    protected $fillable = ['paragraphable_id', 'paragraphable_type', 'region', 'position', 'page_id'];

    public function paragraphable()
    {
        return $this->morphTo();
    }

    public function scopeRegion($query, $region)
    {
        return $query->where('region', $region);
    }

    public function page()
    {
        return $this->belongsTo(\App\Models\Page::class);
    }
}
