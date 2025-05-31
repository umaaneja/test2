<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;
use ParagraphPlugin\Models\Paragraph;

class Page extends Model
{
    protected $fillable = ['url', 'url_alias', 'content_type_id'];

    public function contentType()
    {
        return $this->belongsTo(ContentType::class);
    }

    public function paragraphs()
    {
        return $this->hasMany(Paragraph::class);
    }

    public function fieldValues()
    {
        return $this->hasMany(PageFieldValue::class);
    }

    // Get value of a field by field name
    public function getFieldValue($fieldName)
    {
        $field = $this->contentType->fields->where('name', $fieldName)->first();
        if (!$field) return null;

        $valueObj = $this->fieldValues->where('content_type_field_id', $field->id)->first();
        return $valueObj ? $valueObj->value : null;
    }
}
