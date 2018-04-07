USE `keyWordGen`;
DROP procedure IF EXISTS `keyWordGen`.`sp_addkeyword`;
 
DELIMITER $$
USE `keyWordGen`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_addkeyword`(
    IN p_title varchar(45),
    IN p_description varchar(1000),
    IN p_user_id bigint
)
