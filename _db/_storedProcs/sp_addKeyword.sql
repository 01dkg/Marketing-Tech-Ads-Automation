USE `keyWordGen`;
DROP procedure IF EXISTS `keyWordGen`.`sp_addkeyword`;
 
DELIMITER $$
USE `keyWordGen`$$
CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_addkeyword`(
    IN p_title varchar(45),
    IN p_description varchar(1000),
    IN p_user_id bigint
)
BEGIN
    insert into tbl_keyword(
        keyword_title,
        keyword_description,
        keyword_user_id,
        keyword_date
    )
    values
    (
        p_title,
        p_description,
        p_user_id,
        NOW()
    );
END$$
 
