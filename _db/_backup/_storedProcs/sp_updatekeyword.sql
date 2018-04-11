CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_updatekeyword`(
IN p_title varchar(45),
IN p_description varchar(1000),
IN p_keyword_id bigint,
In p_user_id bigint,
IN p_file_path varchar(200),
IN p_is_private int,
IN p_is_done int
)
BEGIN
update tbl_keyword set
    keyword_title = p_title,
    keyword_description = p_description,
    keyword_file_path = p_file_path,
    keyword_private = p_is_private,
    keyword_accomplished = p_is_done
    where keyword_id = p_keyword_id and keyword_user_id = p_user_id;
END