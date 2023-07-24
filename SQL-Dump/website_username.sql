-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: website
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `username`
--

DROP TABLE IF EXISTS `username`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `username` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `phone` varchar(45) DEFAULT NULL,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='b';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `username`
--

LOCK TABLES `username` WRITE;
/*!40000 ALTER TABLE `username` DISABLE KEYS */;
INSERT INTO `username` VALUES (1,'daskal','2b1cad3cf9de535731cbe0ab020deaf9ee8893111c35daa9196d8ef581cad6e014ab1c39913c992a7658d362e05ef9ca9ed4467ea78d5289df16c51e6d20c342d08beedd3320f66afccba99e07eeaa6fc5af05cc3f98a5541d76d1783c8cfc1c','israel@daskal.co.il','0987654321','israel','daskal'),(2,'test12','751cfd8b95f7e753fefc460f34d0e7b2a1b5e141804f8b0400f42ea55cb3ae30daa9942ff3fd4e4fb6f9bbbbad0042b5962c860315f2b6933be512e18eaa97e52d4959f9dea346c08fff7bdb91c89607732c7c36ba2c5ffc65280f64952702b6','t@e','1234567890','test','test'),(3,'test13','fe3299bb96c250eb1ee10581b3854c132027af18e15b4c13bced7be7cd56e2d01c5a9cf90a3bfacd82a636cfacad62cba88f878dd681b3f200c3bd41cd1a3e2fdde85dd27de926c0fb52926ce6d9fa21f8141ec7c35e1934a11f234578cfa872','e@d','1234567890','firstName','lastName'),(4,'qqqqqqq','bcab5644132ab9b96a91bd98c15ae30c13d7ff618f3f819ee8cf8433c9c82e1ebedb1ab73fb6173ac7f20c2b532d4af00503182e7772fd117f70ae9b80ed326f75aa4c16bc5d4b094bb31561c3fb85b95172fdc2cf490da665bdbb67223fbf46','qq@qq','0987654321','qqq','qqq'),(5,'test1','26a621b763ce361aadbbafcdd00887fb5589bff7fc14fa6502d22ce72a7759bdab71af30945eaee4505e589f406d9f76f47ea7052a3254e6de221361f99e4a938a7c13ffb31e0a6a59aca6491938e24bc44a0d26635285cf7e3a8dd02372654d','test@test','0987654321','test','test1'),(6,'shmuel','6f13480699c63f67dcc79d35385a1fa2afbf3fbec07224485731f76bcaa57baeea5b9c5e9b725f6af379e4a9b323b739d8138a8bf413fb5983044ef54638f4a972b412ba0f4340fa2df35eafecec0d8b95b88e9680ce0f64a07a12deb2f7f420','morshmuel7@gamil.com','123456789','mor','shmuel'),(7,'test321','7c6256b33b419c2a72cd82068a9098eed39218595a6ededfbf8568e54bc569a4c060e8ebb040534767a3c34617d017cd89a74782ae2fcceb548e2611dab05103a88aeb007f5014775334612b7715d47f36d2cf61d12b79559df8d0eb635d1be9','test@test.com','1234567890','test','test12'),(8,'test14','f123d1f7e0862ed098de0d5d8a95502dc227b78fc2f399dc30cb9e5a33536cbc24bd688a7e3a21f82e08c26ce323da014e6c19c1557c180b79557ad03c0152f810172145055eeb03f7544f161ee399abc816a9f9a7e8854a8169751726d90c9a','test12@test.com','1234567890','test23','test14'),(9,'test18','931deb10a56a39bb51663f07456a0d4c16261cc90ac0ba12e62ec9f8377bfeee1f1b450d14bbd8f7b06c923055176f0612d774c59963a9689ac09721bab7ea4a9de0196f9d60fa1df59e8d258e1634a46feec5aa6f659647dfdd72ffa3f6cac3','test18@t.com','1234567890','test18','test18'),(10,'morshu','79571a2dcfc0bc9c3dfd7bcc31903c9b76db22708e6bc0610f9219888e5ab2f40b1f38a6c3f3c4dfcb690fc928e601c561dd424064dcb66d61b98806c227b88fa2cc9f72724cb8c319edfd4d9a2b8ec1f4c1a064d1766455eaaec3cc7d0945ad','mor105001@walla.com','0528236612','mor','cohen'),(11,'test3456','c318f0b14eedf8a13cf8f7e6496455d84af90a61e737ee9d2d70529e161d1af80abc532c0e8367dd1737d8c6ab1148172d8765038d20c674d406ed7f8f2cae38775d6f412bf7a9750da1929f0638e54cc6d2a911ee35b5fca05278a8d08b1f54','test@test','1234567890','test','test');
/*!40000 ALTER TABLE `username` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-30  0:17:22
