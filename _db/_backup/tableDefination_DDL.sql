CREATE TABLE `tbl_status` (
  `keyword_id` int(11) NOT NULL,
  `Status_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `keyword_Status` int(11) DEFAULT '0',
  PRIMARY KEY (`Status_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1

CREATE TABLE `tbl_user` (
  `user_id` bigint(20) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(45) DEFAULT NULL,
  `user_username` varchar(45) DEFAULT NULL,
  `user_password` varchar(1500) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1


CREATE TABLE `tbl_keyword` (
  `keyword_id` int(11) NOT NULL AUTO_INCREMENT,
  `keyword_title` varchar(45) DEFAULT NULL,
  `keyword_description` varchar(5000) DEFAULT NULL,
  `keyword_user_id` int(11) DEFAULT NULL,
  `keyword_date` datetime DEFAULT NULL,
  `keyword_file_path` varchar(200) DEFAULT NULL,
  `keyword_accomplished` int(11) DEFAULT '0',
  `keyword_private` int(11) DEFAULT '0',
  PRIMARY KEY (`keyword_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1



CREATE DEFINER=`root`@`localhost` FUNCTION `getSum`(
    p_keyword_id int
) RETURNS int(11)
BEGIN
    select sum(keyword_Status) into @sm from tbl_status where keyword_id = p_keyword_id;
RETURN @sm;
END

CREATE DEFINER=`root`@`localhost` FUNCTION `hasStatus`(
    p_keyword int,
    p_user int
) RETURNS int(11)
BEGIN
     
    select keyword_Status into @myval from tbl_status where keyword_id =  p_keyword and user_id = p_user;
RETURN @myval;
END