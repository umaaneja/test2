CREATE TABLE `tbl_images` (
  `id` int NOT NULL AUTO_INCREMENT,
  `project_id` int NOT NULL,
  `filename` varchar(255) NOT NULL,
  `filepath` varchar(512) NOT NULL,
  `content_type` varchar(100) NOT NULL,
  `upload_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `file_size` int DEFAULT NULL,
  `width` int DEFAULT NULL,
  `height` int DEFAULT NULL,
  `alt_text` varchar(255) DEFAULT NULL,
  `llm_processed` tinyint(1) NOT NULL DEFAULT '0' COMMENT '0=not processed, 1=processed',
  `llm_response` text DEFAULT NULL COMMENT 'LLM response data',
  PRIMARY KEY (`id`),
  KEY `fk_image_project` (`project_id`),
  CONSTRAINT `fk_image_project` FOREIGN KEY (`project_id`) REFERENCES `tbl_projects` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
