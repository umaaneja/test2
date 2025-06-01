<?php
namespace App\Models;

use Illuminate\Database\Eloquent\Model;

class Page extends Model
{
    protected $fillable = ['url_alias', 'url', 'content_type', 'content_id'];

    public function getRouteKeyName()
    {
        return 'url_alias';
    }
}
