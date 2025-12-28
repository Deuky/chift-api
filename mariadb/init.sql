CREATE DATABASE chift;

USE chift;

DROP TABLE IF EXISTS `contact`;
CREATE TABLE `contact` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `external_id` INTEGER NOT NULL,
  `name` varchar(255),
  `email` varchar(255),
  PRIMARY KEY (`id`)
);
