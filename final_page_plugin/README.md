# Page Plugin (Final)

## Features
- Uses `url_alias` for flexible URL management
- Delegates to dynamic content type models
- Integrates with external Paragraph plugin via `ParagraphRenderer`

## Usage
- Register routes with `Route::get('/{page:url_alias}', ...)`
- Ensure your Paragraph plugin is available under `YourVendor\Paragraphs\Models\Paragraph`
