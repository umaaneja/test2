<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class ContentTypeField extends Model
{
    protected $fillable = ['content_type_id', 'name', 'field_type', 'settings'];

    protected $casts = [
        'settings' => 'array',
    ];

    public function contentType()
    {
        return $this->belongsTo(ContentType::class);
    }
}
