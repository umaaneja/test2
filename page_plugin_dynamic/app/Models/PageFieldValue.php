<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class PageFieldValue extends Model
{
    protected $fillable = ['page_id', 'content_type_field_id', 'value'];

    public function page()
    {
        return $this->belongsTo(Page::class);
    }

    public function contentTypeField()
    {
        return $this->belongsTo(ContentTypeField::class);
    }
}
