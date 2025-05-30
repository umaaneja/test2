<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration {
    public function up()
    {
        Schema::create('gallery_blocks', function (Blueprint $table) {
            $table->id();
            $table->string('title');
            $table->json('images');
            $table->timestamps();
        });
    }

    public function down()
    {
        Schema::dropIfExists('gallery_blocks');
    }
};
