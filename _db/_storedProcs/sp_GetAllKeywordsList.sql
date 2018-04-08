CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_GetAllkeyword`(
    p_user int
)
BEGIN
    select keyword_id,keyword_title,keyword_description,keyword_file_path,getSum(keyword_id),hasLiked(keyword_id,p_user)
    from tbl_keyword where keyword_private = 0;
END