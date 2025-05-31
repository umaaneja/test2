<?php
use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

class CreateContentTypeFieldsTable extends Migration
{
    public function up()
    {
        Schema::create('content_type_fields', function (Blueprint $table) {
            $table->id();
            $table->foreignId('content_type_id')->constrained()->onDelete('cascade');
            $table->string('name');
            $table->string('field_type'); // e.g. text, textarea, date, number, checkbox, etc.
            $table->json('settings')->nullable(); // extra options
            $table->timestamps();
        });
    }
    public function down()
    {
        Schema::dropIfExists('content_type_fields');
    }
}
