CREATE TABLE `tbl_keyword` (
    `keyword_id` int(11) NOT NULL AUTO_INCREMENT,
    `keyword_title` varchar(45) DEFAULT NULL,
    `keyword_description` varchar(5000) DEFAULT NULL,
    `keyword_user_id` int(11) DEFAULT NULL,
    `keyword_date` datetime DEFAULT NULL,
    PRIMARY KEY (`keyword_id`)
  ) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
