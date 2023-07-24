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
-- Table structure for table `history_password`
--

DROP TABLE IF EXISTS `history_password`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `history_password` (
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(200) DEFAULT NULL,
  `date` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `history_password`
--

LOCK TABLES `history_password` WRITE;
/*!40000 ALTER TABLE `history_password` DISABLE KEYS */;
INSERT INTO `history_password` VALUES ('test12','316f30c50d8d3b914370eb7cee204568e97f3f2c6a80bc4a15176e1f0edfb5933ed71585d6a0da3945c90a0d84ab7036ae7f188c0f8ab55b66a1d11bb2606177023ae4a2336d5ceb2525ad5d9b184734c3a14404088da87f9453773ebd989465',1637789573),('test12','0416dcfa0150f5fa8131184e336119a7ab8457ded66164035f2f6ab563298e47045da275e9db18ba8d0c7a3fbe6a6d4a8db7ccb461a89492cf09993036d6d3b3098895799f770c9d83323a32ce89e41b64851cf79bc83ecf983ffdf873f82ecc',1637789687),('test12','8b5520e25b4f9cf74b4014fe9973fe52e92a8a730bee4c0ad1cb1eb6baff9811cdf1f36879489e3c0e9b7ee2d03e154413317dafce1137360187b2ab603aa540ab0226a7fe9e181c0be2b8f986d542834965d0e15f89d5b05a3f434c702d3991',1637789796),('test12','52f4d4c79501a3b4f2e8f3e040af5b135e1515841dc2c120d706b1048b3089b558d66d0f06bea69f0c8dfb8d7a77d38640458a55ab208a9e7e1bfed586bc40d63c02a70e6d71493daad517305f48947234dfeedec0990538b6a580bc93135f3a',1637789904),('test12','98bc1a1a3907b56ade8c392e162c5aecb2c2c6c291385b0df6548f28d671a0d85781492a7d55f9fde0691d395309928131594f3292677395ce27d78a6513e0d00903cb0b244ab8d1b863d5f39ec895ff7bef9f3c305f75666cd8ab731af0613d',1637789936),('test12','c8e0d774a6f8e6552d3234dbb608f2352dc91fb36ff85e2702d4d90a14cf980186874942b36d6599e1eba0d84790c01594206c9d06fc73687392a98805e9d496d04ee9a2b2495bc4e4e80b86e7cb9f31aba4338a137c927e8d0fb979250b117b',1637791618),('daskal','8104d18fa2273708f020e070b8675e75082719761ba56e089e3032ae65c74e9436be492cbca1a1b4aa0ef259f431904667d95279d5c8a96bfe327bc169720ff024e0dc36ef61df4e30f32a531f8ec0f7ea409eba75d24b49a91b2ddf26f0bbff',1637792290),('daskal','b327a78ba0a972af162fc9f3755515dd5d03f86abfe75f04321e73081502493cf53ae654885de9161c4769d8c19e551264b1f9e32497433a5024942c84591216a03dfc631229ccf3ca0d358fa230769026fb23b40625bbaf1a8d80bf8fc17d88',1637792297),('test12','00349cc0d3fe51a1b9a9178b1d044e7245f3c1735adb1bb20f6d65b5d3598503be4dfd468b29f51cbcfb5f2be56bb1c3bf18c94ad87f2799585fa92ee57c3e04067ed4d39e707eb94d3bfef6d0b3ce159e3e4105e25d5b39caf4b44747567e19',1637793526),('daskal','598e3f70a8e1019f698d5ac096beff4b8aaf0e6483f4dc88cc3703438b9f236ece2a027eee87c715d0bdcf193e07ff871649b56c400e15eb694fe2a2fe19dd5ebeb1fa69c77ac6a885472320096c8f68d6faac70ed0f46bd3245132da0dce186',1637794311),('daskal','57445a7a3fa2099d0e7539d550941d6e93b29834d424a53a775fe849fd443b975c7f32e2c93aa7f8f4028222a7da4c02289c3f01bde9d0b9cc80a09c6870759df28966c9f557583e7f079a96d96063282cecb0dcee752169cfa3de6baae5ed08',1637931958),('daskal','f5fbc940be16b5019a255c6a5c544121184703d238a12b599ddf172f6dd14ec6bbcd12afce38277bc198c73e8cfbbf0dc83a5b0de5d0f867968a5b6cc815366639a06ab2cc87014e81f2779c10f9c1df56b559fcae305b085bcf2f3f7bb2377b',1637933018),('daskal','6a2e930b1886aac8a42a2f8c34103ce138b892f4281fd98ebb0ac8940aedf39ac1aa586d23d87c7319dc063fcb09e154e6b9d2ac0b223b1402f4f3bdb678b2ef0524e6d203625fb72934556aa1599c668695a1d4fb3b6946c975594e86ad67c0',1638091922),('qqqqqqq','f0ce47792bd63720a8ac3e49d82e9651adc9c5e1a1520b4f0f62653c474a8f8f253dfe3df83c690355fc5063064ee978ff54c470550e502577e5a1acb694fdbbdd19f8228c315f45c02bed451e2d67c89be6454c9e221f1ee8ccbfc669d4233e',1638136572),('test1','3dc8ebb5c618a7729575cb2b03226965a60333a1acef82d1e117649b20ab32598ed85c3b2cdcf528ee1c52bf63e152e1b7c87dd7500e91f3e5ae49bd63ab007aec98e6a0f2b1b463ded986b2c7fd0540ac0c3c388754fa4ed4a1f716ebdac99b',1638192683),('daskal','44885f177a0f9bc3f04e2786e80ee74a5b3be9770b910dae6ded94f671a5ac54a703307623c28700e7fbe25a8d787785c8dd56249e7c5a99ff3d24b071ab057edcb39ff3ad995060bd59b4f89fa3b1d2cbfe7adc73921236bd7631ba4db82153',1638193899),('shmuel','cf634b11fc8d357a6a6898711eddd2a04d93e20929e6fd4be7521653a1af65c6f8e345b39426708cc847accf0df283e189d232a9d58b8bcf5c71e39b5c01ad83ddcd87d56c53d1a72cc1953bdea50cb4403d2f3013914e65ddc5d95f30ee5eaf',1638270558),('daskal','8104a0fbbab95d226c5fec21b0cb2ee5ebf90d7f4dea9503e0f636182225128c6a131fea3c359018e15d7aa946e1b2b5345366288ace27856a13a9838b3c67a7a27827cfa01ce36563cd733428cb3631c3976001ab2ab4491d20d3987cd83b2a',1638282851),('test321','9165832c9af8ebd589ce3a9196453294794de6b536778de8f60db32abb3b5e357655bb18ce49c7457e4635a0f95fa4746f91b43eacc8e31a68b07aa5b3d588a199748c0ef57a0e6290863ec2f8d020b787fa55bb8233c71439da766bdd65e229',1638286633),('test14','284012f369a57935d37afd06d933b9924f999a324c115d9c2758be8bc7358fa5f2c5742e28b3a9b973da5cdd301340330d7a7657fdbb6246006107d1161d95013202e891ef2341dfc2953b20beec34cd6cd7c8e0c7c6473385b3f904b5ccbc0c',1638287435),('test18','7999f81674edb8432f8c99083c70fd8555edb3b5abd482560548c0c19620c8b55a261b3c41c4c6701ba0a5b8a29195777fa7fffea5cefa20aec9878c2be506599b718c32cd218f98cb8013c7d31d49c52a6e48caaac499cfce5e40acc2212704',1638290661),('daskal','76a31c89829887751ce935d7b5368f7349ba7b433f93445cace134c0c566a83cf2b28bc64f4ffdf07ec3fa4f29ddf200fa1e820a982963f9791f0e4b5f7cb9dea6f7cf4d75a670539e598356649a40718b1135428a1255ec077188c91496578c',1638291102),('daskal','877915e52ee9245e88f1d262b9273598f24b00b8bdf5c1378556316ea8beb08cdc3d1d77c520e215f471b603da62a6acd052e40fb6342ed84428f3151ecec87d9ab80a7447a163f33bc5ad8682fbd25c04758e6c62f1a3fe33fd49d4c755a1b2',1638377021),('dsakal','a61e3a3a03178d022a8d577ef014e8634efa0f76d10c53d40f0a74b116c609e93e1a5f47a75c7ff72c884a532b08026f85a43f9209fff62c382d34e40b7f76224a9fb971261287ed801fe9979085aaa8f4b19751aac92ce4fc1c90652b91fd4d',1640878676),('daskal','e623ca67e18a5dcf54df25fb3b27d48772b9c1ce7e84811db666c8b6ee8c694a160e2056e220d990506b7204f3d78d30ea451286c54beb1890338fb36089e1735328646a49f5e1cc2c03cf0c14d22ccacbe56a0f193214d3f2affc42175e4e7b',1640879018),('daskal','19b312420c3bac184c0c5b4743e378dd718bc66dd53de7d8e0065cacdbfad72704d2dd430777050f51cc0e1a6e2f779f75f518f86b442f25ed9f1be228a45db2882a5f3fbac0eefebe95067dcc6fb4afe86e307f80398d967c718f7b8b5ec44b',1641712037),('morshu','0d24e54eeca3fe64e59b212b01b7c2ec2b3a83b9dc19e685e5fc606b3f72be0316c610b6bb698ec386f93ea08073e86fb1842de87b398a4e4d3891789b654c4ec11c114cc413136ff2e65bfca3a92c2613cd82bbc68720b2c9cc9a8fbd7714ce',1641745621),('daskal','54a9a99fde794602de8571cbb2341dfb3eda8d6eae5472a1226a97243eae2b471446e5455c044f33f1e598191f86e5d10a602f105e28b3e0f8c6796b20141a89c096f6d638e039f62390dafee149335e256be83904a78ded08ca53bed93ac6a3',1641795871),('daskal','fcf67c2c506f9cf5eaad1e96a9006029e86ec28cbe025b9d33fa863bceeec6cb8a26f89cfdc5624c7cf1a2caaa1ef6d4a9dd3c199098859f59500a4c2fa92f5494b8431ed12770eade947fd21f85be99b91196c712347eb31df158963e47809c',1641796096),('test3456','958cef85758c9b8c27a1da62a18f71ebf43f588176aab00032fe0db9155406b88a3db3ea14dd7906663ac5afb6fd176585f40fc7c9964d1a561ce2f7c5a606e81db5afcebf95dafa72da18f69250627e2d8c11b413be3f4760d8d47bbc809f57',1641796491),('daskal','81ef165a99681d2b45f0b37fdf4f78023b0bb3b4f21a18f2f7712b29f64a1e2f25c6b92c1ef318319d6451b6455d3101fb31fe7ba5441c0ef1275e0614e63f49aa32a3ee5ee67bf1018288f3a84397842f21b85dac6d32d19f03a25272a8a538',1642001097),('daskal','38aef9cf5639866de7d60ae18dcf203793f6cdf01915907fb2ce137df2f25044805223142b6a846fab5f15e4e5f6af71aeb2ed256634c9ae9c85300d6bafa7f6e2e0438c63fbb012ffb3ef5bb9cd1a1a12d3064364bd688653d3b44bdd152bc4',1670944043);
/*!40000 ALTER TABLE `history_password` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-30  0:17:21