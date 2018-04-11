USE `keyWordGen`;
DROP procedure IF EXISTS `sp_GetkeywordByUser`;
 
DELIMITER $$
USE `keyWordGen`$$
CREATE PROCEDURE `sp_GetkeywordByUser` (
IN p_user_id bigint
)
BEGIN
    select * from tbl_keyword where keyword_user_id = p_user_id;
END$$
 
DELIMITER 