CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_updatekeyword`(
IN p_title varchar(45),
IN p_description varchar(1000),
IN p_keyword_id bigint,
In p_user_id bigint,
IN p_file_path varchar(200),
IN p_is_private int,
IN p_is_done int
)
