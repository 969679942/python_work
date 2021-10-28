/*
Navicat MySQL Data Transfer

Source Server         : sch
Source Server Version : 50623
Source Host           : localhost:3306
Source Database       : bank

Target Server Type    : MYSQL
Target Server Version : 50623
File Encoding         : 65001

Date: 2021-10-28 15:53:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `user`
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user` (
`account`  int(11) NOT NULL ,
`username`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`password`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`country`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`province`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`street`  varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`door`  varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
`money`  double(50,0) NOT NULL ,
`registerDate`  datetime NOT NULL ,
`bankname`  varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL ,
PRIMARY KEY (`account`)
)
ENGINE=InnoDB
DEFAULT CHARACTER SET=utf8 COLLATE=utf8_general_ci

;

-- ----------------------------
-- Records of user
-- ----------------------------
BEGIN;
INSERT INTO `user` VALUES ('1', '1', '1', 'cn', 'cn', 'cn', 'cn', '4900000', '2021-10-28 11:38:54', '昌平'), ('2', '2', '2', '2', '2', '2', '2', '91442', '2021-10-28 15:17:33', '北京昌平支行'), ('65379156', '张三', '123456', '<class \'object\'>', '陕西', '宁夏', 'hi', '566666', '2021-10-28 14:00:16', '北京昌平支行'), ('90394686', '张三', '1', '<class \'object\'>', '纽约省', '华尔街', '003', '10000000', '2021-10-28 15:39:29', '北京昌平支行'), ('96861053', '李四', '8888', '中国', '北京', '昌平区', '18号', '5555555555555', '2021-10-28 15:43:25', '北京昌平支行');
COMMIT;
