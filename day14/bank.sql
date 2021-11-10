/*
Navicat MySQL Data Transfer

Source Server         : sch
Source Server Version : 50623
Source Host           : localhost:3306
Source Database       : bank

Target Server Type    : MYSQL
Target Server Version : 50623
File Encoding         : 65001

Date: 2021-11-10 11:01:08
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
  `account` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `country` varchar(20) NOT NULL,
  `province` varchar(20) NOT NULL,
  `street` varchar(255) NOT NULL,
  `door` varchar(20) NOT NULL,
  `money` double(50,0) NOT NULL,
  `registerDate` datetime NOT NULL,
  `bankname` varchar(50) NOT NULL,
  PRIMARY KEY (`account`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('11111', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
INSERT INTO `user` VALUES ('22222', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
INSERT INTO `user` VALUES ('33333', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
INSERT INTO `user` VALUES ('44444', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
INSERT INTO `user` VALUES ('45678', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
INSERT INTO `user` VALUES ('55555', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
INSERT INTO `user` VALUES ('66666', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
INSERT INTO `user` VALUES ('77777', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
INSERT INTO `user` VALUES ('88888', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
INSERT INTO `user` VALUES ('99996', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
INSERT INTO `user` VALUES ('99997', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
INSERT INTO `user` VALUES ('99998', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
INSERT INTO `user` VALUES ('99999', 'user1', '123456', 'china', 'BeiJing', 'shahe', '10', '5000', '2021-11-10 11:00:50', '昌平支行');
