CREATE TABLE `tbl_status` (
  `keyword_id` int(11) NOT NULL,
  `Status_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `keyword_Status` int(11) DEFAULT '0',
  PRIMARY KEY (`Status_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1

