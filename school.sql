-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: school
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course` (
  `name` varchar(40) NOT NULL,
  `description` varchar(50) DEFAULT NULL,
  `study` varchar(50) NOT NULL,
  `teacher` varchar(40) NOT NULL,
  `credits` int(2) NOT NULL,
  PRIMARY KEY (`name`,`study`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` (`name`, `description`, `study`, `teacher`, `credits`) VALUES ('Controlsystems','how to control things','PrecisionEngineering','de Wit',2),('Datamodelleren','inleiding tot datamodelleren','BusinessICT','Noether',2),('DifferentialEquations','for smart students','MathematicalEngineering','Eddington',4),('Drawing','drawing with software','Architecture','Mondriaan',2),('ICT','intro to ict','Building information Modeling','Eddington',2),('Mechanics','F=ma and all that','Planedesign','Planck',3),('Optics','lenzen en prismas','PrecisionEngineering','de Wit',3),('Precalculus','introduction to math','MathematicalEngineering','Planck',3);
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exam`
--

DROP TABLE IF EXISTS `exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam` (
  `Course` varchar(50) NOT NULL,
  `Room` varchar(4) NOT NULL,
  `Resit` enum('Y','N') NOT NULL,
  `date` date NOT NULL,
  `time` varchar(20) NOT NULL,
  PRIMARY KEY (`Room`,`time`,`date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam`
--

LOCK TABLES `exam` WRITE;
/*!40000 ALTER TABLE `exam` DISABLE KEYS */;
INSERT INTO `exam` (`Course`, `Room`, `Resit`, `date`, `time`) VALUES ('Optics','A34','N','2017-12-17','10:00-12:00'),('Datamodelleren','A34','N','2017-12-13','14:00-15:30'),('ICT','A34','N','2017-04-01','9:00-11:00'),('ICT','A34','Y','2017-06-01','9:00-11:00'),('DifferentialEquations','A45','N','2017-08-02','14:00-15:30'),('Precalculus','A8','N','2018-05-12','14:00-15:30'),('Drawing','B12','N','2017-08-02','11:00-13:00'),('Optics','B12','Y','2017-03-03','13:00-15:00'),('Mechanics','B13','Y','2018-09-20','19:00-20:30'),('Mechanics','B13','N','2017-04-01','9:00-11:00'),('Controlsystems','B88','N','2017-06-06','16:00-17:30');
/*!40000 ALTER TABLE `exam` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `result`
--

DROP TABLE IF EXISTS `result`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `result` (
  `grade` int(2) DEFAULT NULL,
  `exam` varchar(40) NOT NULL,
  `date` date NOT NULL,
  `weight` float NOT NULL,
  `student` varchar(40) NOT NULL,
  `passed` enum('Y','N') DEFAULT NULL,
  PRIMARY KEY (`exam`,`student`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `result`
--

LOCK TABLES `result` WRITE;
/*!40000 ALTER TABLE `result` DISABLE KEYS */;
INSERT INTO `result` (`grade`, `exam`, `date`, `weight`, `student`, `passed`) VALUES (4,'Controlsystems','2017-06-06',1,'Brandse','N'),(5,'Controlsystems','2017-06-06',1,'Snel','N'),(4,'Controlsystems','2017-06-06',1,'Vidal','N'),(6,'DifferentialEquation','2017-08-02',1,'Udang','Y'),(8,'DifferentialEquations','2017-08-02',1,'Hanzo','Y'),(8,'DifferentialEquations','2017-08-02',1,'Udang','Y'),(10,'Drawing','2017-02-08',1,'Pietersma','Y'),(8,'ICT','2017-04-01',1,'Henriquez','Y'),(3,'ICT','2017-04-01',1,'Penning','N'),(6,'Mechanics','2017-04-01',1,'Bush','Y'),(2,'Mechanics','2017-04-04',1,'Williamson','N'),(3,'Optics','2017-12-17',1,'Brandse','N'),(5,'Optics','2017-12-17',1,'Vidal','N'),(7,'Precalculus','2018-05-12',1,'Hanzo','Y'),(4,'Precalculus','2018-05-12',1,'Tjaikovski','N'),(7,'Precalculus','2018-05-12',1,'Udang','Y'),(6,'resit ICT','2017-06-01',1,'Penning','Y'),(5,'resit Mechanics','2017-09-20',1,'Williamson','N'),(9,'resit Optics','2018-03-03',1,'Brandse','Y'),(6,'resit Optics','2018-03-03',1,'Vidal','Y');
/*!40000 ALTER TABLE `result` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `studentnumber` int(10) NOT NULL,
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(30) NOT NULL,
  `dateofbirth` date NOT NULL,
  `nationality` varchar(30) NOT NULL,
  `gender` enum('M','F') NOT NULL,
  `street` varchar(40) NOT NULL,
  `streetnumber` varchar(6) NOT NULL,
  `postalcode` varchar(10) NOT NULL,
  `city` varchar(35) NOT NULL,
  `phonenumber` varchar(15) NOT NULL,
  `email` varchar(50) NOT NULL,
  `study` varchar(50) NOT NULL,
  `startyear` int(4) NOT NULL,
  `studycounselor` varchar(50) NOT NULL,
  `schoolemail` varchar(50) NOT NULL DEFAULT '',
  `password` varchar(255) NOT NULL DEFAULT '',
  PRIMARY KEY (`studentnumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` (`studentnumber`, `firstname`, `lastname`, `dateofbirth`, `nationality`, `gender`, `street`, `streetnumber`, `postalcode`, `city`, `phonenumber`, `email`, `study`, `startyear`, `studycounselor`, `schoolemail`, `password`) VALUES (1,'Ben','Williamson','1984-06-02','American','M','Van Baerlestraat','102','1071 BC','Amsterdam','0657892638','benwilliamson@gmail.com','Planedesign',2016,'de Wit','',''),(2,'Akimira','Hanzo','1998-04-06','Japanese','F','Leylandstraat','18','2014 JN','Haarlem','0678905621','kira@gmail.com','MathematicalEngineering',2018,'Mondriaan','',''),(3,'Estrella','Henriquez','1995-12-04','Spanish','F','Professor Dondersstraat','21','1221 HM','Hilversum','0682856135','estrella.henriquez@gmail.com','BusinessICT',2017,'Planck','',''),(4,'Artur','Vidal','1997-11-27','Portuguese','M','Dirkhartogstraat','375','4812 GE','Breda','0683956121','arturvidal@gmail.com','PrecisionEngineering',2019,'Mondriaan','',''),(5,'Jan-Willem','Pietersma','1995-02-26','Dutch','M','Dubbeldamseweg Zuid','84','3314 JC','Dordrecht','0631121451','pietersma@gmail.com','Architecture',2018,'Mondriaan','',''),(16153,'Margje','Penning','2001-02-20','Dutch','F','Bergwijkdreef','632','1112 XD','Diemen','0695270512','margjepenning@gmail.com','Building information Modeling',2016,'de Wit','',''),(16500,'Frank','Brandse','1999-01-19','Dutch','M','Oosterdokskade','88','1011 DL','Amsterdam','0643898705','frankb@gmail.com','PrecisionEngineering',2016,'Planck','',''),(16504,'Willibrord','Snel','1980-02-22','Dutch','M','Edith Piafstraat','4','1311 HJ','Almere','0699775533','snelbrord@gmail.com','PrecisionEngineering',2016,'de Wit','',''),(17502,'Johann','Bach','1934-03-01','Dutch','M','Singel','89','1015AD','Amsterdam','656657588','johannbach@gmail.com','BusinessICT',2017,'Planck','',''),(17605,'Kate','Bush','1967-03-31','English','F','Markenstraat','34','6131 BP','Sittard','0685342188','thekatebush@gmail.com','Planedesign',2017,'Planck','',''),(17606,'Pjotr','Tjaikovsky','1922-10-10','Russian','M','De Wittenkade','45','1052AC','Amsterdam','0645453798','tjaikovsky@gmail.com','MathematicalEngineering',2017,'Planck','',''),(18501,'Hetty','Udang','1999-09-09','Indonesian','F','Hugo de Grootsingel','33','1277 CM','Almere','0683421765','hetty.udang@gmail.com','MathematicalEngineering',2018,'Mondriaan','','');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `study`
--

DROP TABLE IF EXISTS `study`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `study` (
  `name` varchar(40) NOT NULL,
  `parttime` enum('Y','N') DEFAULT 'N',
  `description` varchar(50) DEFAULT NULL,
  `language` enum('Dutch','English') NOT NULL,
  `no_of_years` int(2) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `study`
--

LOCK TABLES `study` WRITE;
/*!40000 ALTER TABLE `study` DISABLE KEYS */;
INSERT INTO `study` (`name`, `parttime`, `description`, `language`, `no_of_years`) VALUES ('Architecture','N','designing buildings','Dutch',4),('Building information Modeling','Y','management of digital representations of physical ','Dutch',4),('BusinessICT','N','for management studies','Dutch',3),('MathematicalEngineering','N','a mathematical approach to engineering','Dutch',4),('Planedesign','N','for aeronautical engineers','English',4),('PrecisionEngineering','N','study of very small things','Dutch',4);
/*!40000 ALTER TABLE `study` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `firstname` varchar(30) NOT NULL,
  `lastname` varchar(30) NOT NULL,
  `dateofbirth` date NOT NULL,
  `nationality` varchar(30) NOT NULL,
  `gender` enum('M','F') NOT NULL,
  `street` varchar(40) NOT NULL,
  `streetnumber` varchar(6) NOT NULL,
  `postalcode` varchar(10) NOT NULL,
  `city` varchar(35) NOT NULL,
  `phonenumber` varchar(15) NOT NULL,
  `salary` int(15) NOT NULL,
  `studycounselor` char(1) NOT NULL,
  `email` varchar(40) NOT NULL DEFAULT '',
  `workemail` varchar(50) NOT NULL DEFAULT '',
  `Password` varchar(50) NOT NULL DEFAULT '',
  `teachernumber` int(10) NOT NULL,
  PRIMARY KEY (`teachernumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` (`firstname`, `lastname`, `dateofbirth`, `nationality`, `gender`, `street`, `streetnumber`, `postalcode`, `city`, `phonenumber`, `salary`, `studycounselor`, `email`, `workemail`, `Password`, `teachernumber`) VALUES ('Emmy','Noether','1945-04-04','German','F','Eemnesserweg','105','1221 CW','Hilversum','0622357181',5877,'N','noether@gmail.com','','',372252),('Arthur','Eddington','1933-12-23','English','M','Van Alkemadelaan','980','2597 BH','Den Haag','0689472536',4986,'N','arthureddington@gmail.com','','',941661),('Bert','de Wit','1955-01-09','Dutch','M','Buiksloterneerstraat','1','1135 JP','Edam','0698576267',4350,'Y','bert.dewit@gmail.com','','',952754),('Max','Planck','1905-12-12','German','M','Rechtboomsloot','28','1011 CS','Amsterdam','0687125530',6489,'Y','mplanck@gmail.com','','',962560),('Pieter','Mondriaan','1907-01-31','Dutch','M','Burgwal','17','2011 BA','Haarlem','0678361523',3172,'Y','Mondrilaan.piet@gmail.com','','',983650);
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'school'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-04 16:51:47
