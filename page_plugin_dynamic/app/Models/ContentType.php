<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class ContentType extends Model
{
    protected $fillable = ['name', 'description'];

    public function fields()
    {
        return $this->hasMany(ContentTypeField::class);
    }

    public function pages()
    {
        return $this->hasMany(Page::class);
    }
}
