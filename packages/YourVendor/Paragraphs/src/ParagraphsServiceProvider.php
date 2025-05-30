<?php

namespace YourVendor\Paragraphs;

use Illuminate\Support\ServiceProvider;
use Illuminate\Support\Facades\Blade;
use YourVendor\Paragraphs\Components\ParagraphRegion;

class ParagraphsServiceProvider extends ServiceProvider
{
    public function boot()
    {
        $this->loadViewsFrom(__DIR__.'/../resources/views', 'paragraphs');
        $this->loadMigrationsFrom(__DIR__.'/../database/migrations');

        Blade::component('paragraph-region', ParagraphRegion::class);
    }

    public function register()
    {
        //
    }
}
