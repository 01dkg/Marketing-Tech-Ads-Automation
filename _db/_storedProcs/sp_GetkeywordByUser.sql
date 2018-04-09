CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_GetkeywordByUser`(
IN p_user_id bigint,
IN p_limit int,
IN p_offset int,
out p_total bigint
)
BEGIN
     
    select count(*) into p_total from tbl_keyword where keyword_user_id = p_user_id;
 
    SET @t1 = CONCAT( 'select * from tbl_keyword where keyword_user_id = ', p_user_id, ' order by keyword_date desc limit ',p_limit,' offset ',p_offset);
    PREPARE stmt FROM @t1;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END