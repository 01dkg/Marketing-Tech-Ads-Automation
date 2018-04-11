CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_AddUpdateLikes`(
    p_keyword_id int,
    p_user_id int,
    p_like int
)
BEGIN
    if (select exists (select 1 from tbl_likes where keyword_id = p_keyword_id and user_id = p_user_id)) then
 
        update tbl_likes set keyword_like = p_like where keyword_id = p_keyword_id and user_id = p_user_id;
         
    else
         
        insert into tbl_likes(
            keyword_id,
            user_id,
            keyword_like
        )
        values(
            p_keyword_id,
            p_user_id,
            p_like
        );
 
    end if;
END