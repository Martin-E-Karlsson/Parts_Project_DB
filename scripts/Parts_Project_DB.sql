-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: Project_parts_DB
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `cars`
--

USE Project_parts_DB;
DROP TABLE IF EXISTS `cars`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cars` (
  `idCar` int NOT NULL AUTO_INCREMENT,
  `Model` varchar(45) NOT NULL,
  `ModelYear` varchar(4) NOT NULL,
  `Color` varchar(45) NOT NULL,
  `RegNumber` varchar(32) NOT NULL,
  `idSource` int NOT NULL,
  `idCustomer` int NOT NULL,
  PRIMARY KEY (`idCar`),
  KEY `idSource` (`idSource`),
  KEY `idCustomer` (`idCustomer`),
  CONSTRAINT `cars_ibfk_1` FOREIGN KEY (`idSource`) REFERENCES `sources` (`idSource`),
  CONSTRAINT `cars_ibfk_2` FOREIGN KEY (`idCustomer`) REFERENCES `customers` (`idCustomer`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cars`
--

LOCK TABLES `cars` WRITE;
/*!40000 ALTER TABLE `cars` DISABLE KEYS */;
INSERT INTO `cars` VALUES (1,'Volvo V70','1997','grå','abc 123',1,1),(2,'Volvo V70','2000','grå','cad 123',1,1),(3,'Volvo S60','2008','vit med en bild på liam neeson','bmw 163',1,2),(4,'Saab 29 Tunnan','1963','grå','fly 483',2,3),(5,'Saab 39 Gripen','2011','röd','gar 111',2,4),(7,'911 Turbo','2003','Red','TVR646',3,1);
/*!40000 ALTER TABLE `cars` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `companies` (
  `idCompany` int NOT NULL AUTO_INCREMENT,
  `CompanyName` varchar(45) NOT NULL,
  PRIMARY KEY (`idCompany`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
INSERT INTO `companies` VALUES (1,'Volvo Cars'),(2,'SAAB');
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacts` (
  `idContact` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `PhoneNumber` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `idCompany` int DEFAULT NULL,
  PRIMARY KEY (`idContact`),
  KEY `idCompany` (`idCompany`),
  CONSTRAINT `contacts_ibfk_1` FOREIGN KEY (`idCompany`) REFERENCES `companies` (`idCompany`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts`
--

LOCK TABLES `contacts` WRITE;
/*!40000 ALTER TABLE `contacts` DISABLE KEYS */;
INSERT INTO `contacts` VALUES (1,'Martin','555-555555555','Martin@mail.com',NULL),(2,'Henrik','555-112223344','Henrik@mail.com',2),(3,'Luis','123123123','luis@volvo.com',1),(4,'sayed','070-0707070707','sayed@email.com',1);
/*!40000 ALTER TABLE `contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `idCustomer` int NOT NULL AUTO_INCREMENT,
  `Address` varchar(45) NOT NULL,
  `idContact` int NOT NULL,
  PRIMARY KEY (`idCustomer`),
  KEY `idContact` (`idContact`),
  CONSTRAINT `customers_ibfk_1` FOREIGN KEY (`idContact`) REFERENCES `contacts` (`idContact`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'Hemmvägen 37',1),(2,'satangatan 66',2),(3,'Andragatan',2),(4,'galgevägen 4',3);
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employees`
--

DROP TABLE IF EXISTS `employees`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employees` (
  `idEmployee` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `PhoneNumber` varchar(100) NOT NULL,
  `idStore` int NOT NULL,
  PRIMARY KEY (`idEmployee`),
  KEY `idStore` (`idStore`),
  CONSTRAINT `employees_ibfk_1` FOREIGN KEY (`idStore`) REFERENCES `stores` (`idStore`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employees`
--

LOCK TABLES `employees` WRITE;
/*!40000 ALTER TABLE `employees` DISABLE KEYS */;
INSERT INTO `employees` VALUES (1,'Light','2738493822228','Light@carparts.se',1),(2,'Wily','073619574448','Wily@carparts.se',1),(3,'Proto Man','123234345','ProtoMan@carparts.se',2),(4,'Mega man','123765345789','Megaman@carparts.se',3);
/*!40000 ALTER TABLE `employees` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manufacturers`
--

DROP TABLE IF EXISTS `manufacturers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `manufacturers` (
  `idManufacturer` int NOT NULL AUTO_INCREMENT,
  `HQAdress` varchar(45) NOT NULL,
  `HQPhoneNumber` varchar(45) NOT NULL,
  `ManufacturerName` varchar(155) NOT NULL,
  PRIMARY KEY (`idManufacturer`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manufacturers`
--

LOCK TABLES `manufacturers` WRITE;
/*!40000 ALTER TABLE `manufacturers` DISABLE KEYS */;
INSERT INTO `manufacturers` VALUES (1,'Personalvägen 21, 418 78 Göteborg','031-59 33 00','Volvo Cars'),(2,'Bröderna Ugglas gata 58254 LINKÖPING','08-463 00 00','SAAB AB'),(7,'Schmetterlingstraße','34280394832','Porsche');
/*!40000 ALTER TABLE `manufacturers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orderdetails`
--

DROP TABLE IF EXISTS `orderdetails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orderdetails` (
  `ProductQuantity` int NOT NULL,
  `PurchaseDate` datetime NOT NULL,
  `idOrder` int NOT NULL,
  `idProduct` int NOT NULL,
  `idEmployee` int NOT NULL,
  PRIMARY KEY (`idOrder`,`idProduct`),
  KEY `idProduct` (`idProduct`),
  KEY `idEmployee` (`idEmployee`),
  CONSTRAINT `orderdetails_ibfk_1` FOREIGN KEY (`idOrder`) REFERENCES `orders` (`idOrder`),
  CONSTRAINT `orderdetails_ibfk_2` FOREIGN KEY (`idProduct`) REFERENCES `products` (`idProduct`),
  CONSTRAINT `orderdetails_ibfk_3` FOREIGN KEY (`idEmployee`) REFERENCES `employees` (`idEmployee`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orderdetails`
--

LOCK TABLES `orderdetails` WRITE;
/*!40000 ALTER TABLE `orderdetails` DISABLE KEYS */;
INSERT INTO `orderdetails` VALUES (5,'2020-01-01 04:40:10',1,1,1),(5,'2020-11-22 23:45:55',1,2,1),(15,'2020-11-13 22:45:14',1,3,2),(6,'2020-11-22 12:45:35',2,1,3),(75,'2020-11-11 05:45:10',2,4,2),(55,'2020-11-16 09:23:10',3,5,3),(9,'2020-11-17 19:45:10',4,4,4),(33,'2020-11-23 10:45:00',4,5,1);
/*!40000 ALTER TABLE `orderdetails` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orders` (
  `idOrder` int NOT NULL AUTO_INCREMENT,
  `idCustomer` int DEFAULT NULL,
  PRIMARY KEY (`idOrder`),
  KEY `idCustomer` (`idCustomer`),
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`idCustomer`) REFERENCES `customers` (`idCustomer`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (1,1),(2,2),(3,3),(4,4);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `product_catalogs`
--

DROP TABLE IF EXISTS `product_catalogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product_catalogs` (
  `idProduct` int NOT NULL,
  `idRetailer` int NOT NULL,
  PRIMARY KEY (`idProduct`,`idRetailer`),
  KEY `idRetailer` (`idRetailer`),
  CONSTRAINT `product_catalogs_ibfk_1` FOREIGN KEY (`idProduct`) REFERENCES `products` (`idProduct`),
  CONSTRAINT `product_catalogs_ibfk_2` FOREIGN KEY (`idRetailer`) REFERENCES `retailers` (`idRetailer`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product_catalogs`
--

LOCK TABLES `product_catalogs` WRITE;
/*!40000 ALTER TABLE `product_catalogs` DISABLE KEYS */;
INSERT INTO `product_catalogs` VALUES (1,1),(2,1),(3,1),(4,1),(5,1),(1,2),(2,2),(3,2),(5,2);
/*!40000 ALTER TABLE `product_catalogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `idProduct` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Retailer` varchar(45) NOT NULL,
  `Description` varchar(45) NOT NULL,
  `PurchaseCost` int NOT NULL,
  `SellPrice` int NOT NULL,
  `idSource` int NOT NULL,
  `idWarehouse` int NOT NULL,
  PRIMARY KEY (`idProduct`),
  KEY `idSource` (`idSource`),
  KEY `idWarehouse` (`idWarehouse`),
  CONSTRAINT `products_ibfk_1` FOREIGN KEY (`idSource`) REFERENCES `sources` (`idSource`),
  CONSTRAINT `products_ibfk_2` FOREIGN KEY (`idWarehouse`) REFERENCES `warehouses` (`idWarehouse`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'VARTA E11','batterionline.se','12V 74Ah (Bilbatteri)',1100,1249,1,1),(2,'VARTA H3','batterionline.se','12V 100Ah (Bilbatteri)',1200,1569,1,2),(3,'RIDEX Bromsbeläggssats skivbroms','bildelaronline24.se','Bakaxel, exkl. bromsoksskruvar',1100,1249,1,3),(4,'Muflare','Volvo Cars','Volvo muflare',110,1249,1,4),(5,'Blinkar vätska','storeOnline.web','Funkar inte till BMW',100,1490,2,5);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `retailers`
--

DROP TABLE IF EXISTS `retailers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `retailers` (
  `idRetailer` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `Address` varchar(45) NOT NULL,
  `idContact` int DEFAULT NULL,
  `idManufacturer` int DEFAULT NULL,
  PRIMARY KEY (`idRetailer`),
  KEY `idContact` (`idContact`),
  KEY `idManufacturer` (`idManufacturer`),
  CONSTRAINT `retailers_ibfk_1` FOREIGN KEY (`idContact`) REFERENCES `contacts` (`idContact`),
  CONSTRAINT `retailers_ibfk_2` FOREIGN KEY (`idManufacturer`) REFERENCES `manufacturers` (`idManufacturer`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `retailers`
--

LOCK TABLES `retailers` WRITE;
/*!40000 ALTER TABLE `retailers` DISABLE KEYS */;
INSERT INTO `retailers` VALUES (1,'Volvoparts','volvoshem',4,1),(2,'inte saab bilar','volvoshem',2,1);
/*!40000 ALTER TABLE `retailers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sources`
--

DROP TABLE IF EXISTS `sources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sources` (
  `idSource` int NOT NULL AUTO_INCREMENT,
  `idManufacturer` int NOT NULL,
  PRIMARY KEY (`idSource`),
  KEY `idManufacturer` (`idManufacturer`),
  CONSTRAINT `sources_ibfk_1` FOREIGN KEY (`idManufacturer`) REFERENCES `manufacturers` (`idManufacturer`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sources`
--

LOCK TABLES `sources` WRITE;
/*!40000 ALTER TABLE `sources` DISABLE KEYS */;
INSERT INTO `sources` VALUES (1,1),(2,2),(3,7);
/*!40000 ALTER TABLE `sources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `storeinventorys`
--

DROP TABLE IF EXISTS `storeinventorys`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storeinventorys` (
  `idProduct` int NOT NULL,
  `idStore` int NOT NULL,
  PRIMARY KEY (`idProduct`,`idStore`),
  KEY `idStore` (`idStore`),
  CONSTRAINT `storeinventorys_ibfk_1` FOREIGN KEY (`idProduct`) REFERENCES `products` (`idProduct`),
  CONSTRAINT `storeinventorys_ibfk_2` FOREIGN KEY (`idStore`) REFERENCES `stores` (`idStore`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storeinventorys`
--

LOCK TABLES `storeinventorys` WRITE;
/*!40000 ALTER TABLE `storeinventorys` DISABLE KEYS */;
INSERT INTO `storeinventorys` VALUES (1,1),(2,1),(3,1),(4,1),(5,1),(1,2),(2,2),(4,2),(1,3),(2,3),(3,3);
/*!40000 ALTER TABLE `storeinventorys` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stores`
--

DROP TABLE IF EXISTS `stores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stores` (
  `idStore` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(100) NOT NULL,
  `StoreType` varchar(100) NOT NULL,
  PRIMARY KEY (`idStore`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stores`
--

LOCK TABLES `stores` WRITE;
/*!40000 ALTER TABLE `stores` DISABLE KEYS */;
INSERT INTO `stores` VALUES (1,'carparts gbg','fysisk butik'),(2,'carparts utanför gbg','fysisk butik'),(3,'carparts.se','online butik');
/*!40000 ALTER TABLE `stores` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `warehouses`
--

DROP TABLE IF EXISTS `warehouses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `warehouses` (
  `idWarehouse` int NOT NULL AUTO_INCREMENT,
  `ProductInStorage` int NOT NULL,
  `MinimalAmountInStorage` int NOT NULL,
  `AmountToBeDelivered` int NOT NULL,
  `ProductDeliveryDate` date DEFAULT NULL,
  PRIMARY KEY (`idWarehouse`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `warehouses`
--

LOCK TABLES `warehouses` WRITE;
/*!40000 ALTER TABLE `warehouses` DISABLE KEYS */;
INSERT INTO `warehouses` VALUES (1,12,5,4,'2020-11-20'),(2,15,7,4,'2020-11-23'),(3,19,1,4,'2020-11-26'),(4,23,16,10,'2020-11-23'),(5,13,11,10,NULL);
/*!40000 ALTER TABLE `warehouses` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-12-02 10:26:33
