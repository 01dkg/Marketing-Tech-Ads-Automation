CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_GetkeywordByUser`(
IN p_user_id bigint,
IN p_limit int,
IN p_offset int,
out p_total bigint
)
BEGIN
     
    select count(*) into p_total from tbl_keyword where keyword_user_id = p_user_id;
 
    