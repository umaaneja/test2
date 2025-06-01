<?php

use App\Http\Controllers\PageController;

Route::get('/{page:url_alias}', [PageController::class, 'show'])->name('page.show');
