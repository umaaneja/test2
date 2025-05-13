Discovery	Understand what exists	- Inventory of all content (pages, files, taxonomies, users, etc.)
- Identify custom modules, templates, data structures
- Identify 3rd-party dependencies
Analysis	Understand how to migrate it	- Assess content quality and relevance
- Identify what to migrate, transform, or archive
- Map old structures (Drupal nodes, fields) to new (Hugo front matter, Laravel DB schema)
- Identify challenges or blockers

Transformation	Convert content/data into the right format for the target system	- Convert HTML to Markdown (for Hugo)
- Rewrite URLs and internal links
- Extract and convert media files
- Normalize data fields
- Adjust content structure
Execution	Actually move the data/content	- Import Markdown files into Hugo
- Populate Laravel databases
- Push media files to the new hosting
- Run migration scripts
- Trigger builds/deployments
