flowchart TB
    A[Drupal Legacy Site] -->|Scrape HTML, CSS, JS, Entities| B(Scraper Engine)
    A -->|Analyze Custom Code Modules PHP| C[Custom Code Analyzer]
    A -->|Analyze Database Schema Entities| D[Database Schema Extractor]

    B --> C1[Extract Pages, Blocks, Content Nodes]
    B --> C2[Extract CSS and JS Assets]
    B --> C3[Extract Webforms, Forms]
    B --> C4[Extract Entities Users, Taxonomy, Files]
    B --> C5[Extract Redirect Rules and Custom Modules]

    subgraph AI_Layer [GenAI Processing Layer]
        C1 --> D1[GenAI Classify Pages, Blocks, Templates]
        C1 --> D6[GenAI Identify Global/Re-usable Blocks e.g. Header, Footer, CTAs]
        D6 --> E6[Generate Laravel Blade Components for Reusable Blocks]

        C2 --> D2[GenAI Analyze CSS/JS Roles and Dependencies]
        C3 --> D3[GenAI Interpret Forms into Laravel Livewire or Inertia.js Components]
        C4 --> D4[GenAI Map Entities to Laravel Models Eloquent ORM]
        C5 --> D5[GenAI Analyze Custom Functions and Suggest Laravel Rebuilds]

        D1 --> E1[Auto-generate Laravel Views and Routes with Reusable Components]
        D2 --> E2[Bundle and Optimize Assets for Laravel Mix Webpack]
        D3 --> E3[Generate Livewire or Inertia.js Components for Dynamic Forms]
        D4 --> E4[Create Models, Factories, and Migrations for Taxonomy, Users, Files]
        D5 --> E5[Suggest Rebuild of Custom Functions using Laravel Helper Methods]

        %% Page Types and Layouts
        D1 --> D7[Identify Page Types Homepage, Post, Archive]
        D7 --> E7[Create Blade Templates e.g. index.blade.php, show.blade.php]

        %% Database Migration
        D --> D8[GenAI Migrate Drupal Entities to Laravel Models]
        D8 --> E8[Create Database Migrations and Relationships]

        %% Custom Code Migration
        C --> F1[GenAI Analyze Custom Modules/Functions]
        F1 --> F2[Rebuild Custom Logic in Laravel Controllers, Middleware, Services]

        %% Redirect Rules
        C5 --> R1[Extract Redirects]
        R1 --> R2[GenAI Suggest Updated Redirect Strategies for Laravel]
        R2 --> F
    end

    E1 --> F[Laravel Views and Routes Directory]
    E6 --> F
    E2 --> F
    E3 --> F
    E4 --> F
    E5 --> F
    E7 --> F
    E8 --> F

    F --> G[Laravel Build and Test Preview]
    G --> H[Production Deployment Forge, Envoyer, DigitalOcean, AWS]
