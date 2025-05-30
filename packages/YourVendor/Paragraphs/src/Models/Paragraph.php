<?php

namespace YourVendor\Paragraphs\Models;

use Illuminate\Database\Eloquent\Model;

class Paragraph extends Model
{
    protected $fillable = ['paragraphable_type', 'paragraphable_id', 'region', 'position'];

    public function paragraphable()
    {
        return $this->morphTo();
    }

    public function scopeRegion($query, string $region)
    {
        return $query->where('region', $region)->orderBy('position');
    }
}
