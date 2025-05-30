<?php

namespace YourVendor\Paragraphs\Providers;

use Illuminate\Support\ServiceProvider;
use YourVendor\Paragraphs\View\Components\ParagraphRegion;

class ParagraphsServiceProvider extends ServiceProvider
{
    public function boot()
    {
        $this->loadViewsFrom(__DIR__.'/../../resources/views', 'paragraphs');

        $this->loadViewComponentsAs('paragraphs', [
            ParagraphRegion::class,
        ]);
    }

    public function register()
    {
        //
    }
}
