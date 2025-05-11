ALTER TABLE `tbl_images` 
ADD COLUMN `llm_processed` TINYINT(1) NOT NULL DEFAULT 0 COMMENT '0=not processed, 1=processed',
ADD COLUMN `llm_response` TEXT DEFAULT NULL COMMENT 'LLM response data';
