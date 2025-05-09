flowchart TB
    A[Drupal Legacy Site] -->|Scrape HTML, CSS, JS, Entities| B(Scraper Engine)

    B --> C1[Extract Pages, Blocks, Content Nodes]
    B --> C2[Extract CSS and JS Assets]
    B --> C3[Extract Webforms, Forms]
    B --> C4["Extract Entities (Users, Taxonomy, Files)"]
    B --> C5[Extract Redirect Rules and Custom Modules]

    subgraph AI_Layer [GenAI Processing Layer]
        C1 --> D1[GenAI: Classify Pages, Blocks, Templates]
        C1 --> D6["GenAI: Identify Global/Re-usable Blocks (e.g., Header, Footer, CTAs)"]
        D6 --> E6[Generate Hugo Partials/Shortcodes for Reusable Blocks]

        C2 --> D2[GenAI: Analyze CSS/JS Roles and Dependencies]
        C3 --> D3[GenAI: Interpret Forms into Static+JS/Serverless]
        C4 --> D4["GenAI: Map Entities to Hugo Data (YAML/JSON)"]
        C5 --> D5[GenAI: Analyze Custom Functions and Suggest Rebuilds]

        D1 --> E1["Auto-generate Hugo Markdown and Front Matter (using Reusable Blocks)"]
        D2 --> E2[Bundle and Optimize Assets for Hugo]
        D3 --> E3[Generate Static Form Handlers with JS Functions]
        D4 --> E4[Create Data Files for Taxonomy, Users, Files]
        D5 --> E5["Suggest Shortcodes, Widgets, or Serverless Functions"]

        %% Page Types and Layouts
        D1 --> D7["Identify Page Types (Homepage, Post, Archive)"]
        D7 --> E7["Create Layout Templates (e.g., single.html, list.html)"]
    end

    E1 --> F[Hugo Content Directory]
    E6 --> F
    E2 --> F
    E3 --> F
    E4 --> F
    E5 --> F
    E7 --> F

    F --> G[Hugo Build and Test Preview]
    G --> H["Production Deployment (Netlify, Vercel, S3, CloudFront)"]

    C5 --> R1["Extract Redirects"]
    R1 --> R2[GenAI: Suggest Updated Redirect Strategies]
    R2 --> F



%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#ffdfd3', 'edgeLabelBackground':'#fff', 'tertiaryColor': '#dcd0ff'}}}%%
graph TD
    %% Infrastructure Components
    A[("Drupal Legacy Site
    (PHP/MySQL)")] -->|API/Scraping| B[["Scraper Engine
    (Node.js/Python)"]]
    
    B -->|Raw Data| C[["AI Processing Layer
    (LLM Orchestration)"]]
    
    C -->|Structured Content| D[["Hugo Generator
    (Go Templates)"]]
    
    D -->|Static Site| E[["CDN Hosting
    (Netlify/Vercel/S3)"]]
    
    %% Subsystems
    subgraph ExtractionLayer["Extraction Layer"]
        B1[["Content Crawler"]] 
        B2[["Asset Downloader"]]
        B3[["Database Dumper"]]
    end
    
    subgraph AILayer["AI Processing Layer"]
        C1[["Content Classifier
        (GenAI)"]]
        C2[["CSS/JS Analyzer"]]
        C3[["Form Converter"]]
        C4[["Entity Mapper"]]
    end
    
    subgraph HugoLayer["Hugo Generation"]
        D1[["Template Engine"]]
        D2[["Shortcode Generator"]]
        D3[["Data Processor"]]
    end
    
    %% Data Flow
    A --> ExtractionLayer
    ExtractionLayer --> AILayer
    AILayer --> HugoLayer
    HugoLayer --> E
    
    %% Supporting Systems
    F[["Redis Cache
    (Temporary Storage)"]] --> ExtractionLayer
    G[["Vector DB
    (AI Context)"]] --> AILayer
    H[["CI/CD Pipeline"]] --> E
    
    %% Styling
    classDef legacy fill:#f9d5e5,stroke:#333;
    classDef tool fill:#e3eaa7,stroke:#333;
    classDef ai fill:#b2d3c2,stroke:#333;
    classDef static fill:#82b4d6,stroke:#333;
    classDef infra fill:#ffb347,stroke:#333;
    classDef storage fill:#dac4f7,stroke:#333;
    
    class A legacy;
    class B,B1,B2,B3 tool;
    class C,C1,C2,C3,C4 ai;
    class D,D1,D2,D3 static;
    class E,H infra;
    class F,G storage;
