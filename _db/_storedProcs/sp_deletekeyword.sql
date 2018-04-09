CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_deletekeyword`(
IN p_keyword_id bigint,
IN p_user_id bigint
)
BEGIN
delete from tbl_keyword where keyword_id = p_keyword_id and keyword_user_id = p_user_id;
END