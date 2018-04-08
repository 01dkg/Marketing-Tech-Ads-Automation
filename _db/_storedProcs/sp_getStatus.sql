CREATE DEFINER=`root`@`localhost` PROCEDURE `sp_getStatus`(
    IN p_keyword_id int,
    IN p_user_id int
)
BEGIN
    select getSum(p_keyword_id),hasLiked(p_keyword_id,p_user_id);
END