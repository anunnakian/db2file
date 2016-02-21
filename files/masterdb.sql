-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               5.6.17 - MySQL Community Server (GPL)
-- Server OS:                    Win32
-- HeidiSQL Version:             9.1.0.4867
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Dumping database structure for masterdb
DROP DATABASE IF EXISTS `masterdb`;
CREATE DATABASE IF NOT EXISTS `masterdb` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `masterdb`;


-- Dumping structure for table masterdb.etudiants
DROP TABLE IF EXISTS `etudiants`;
CREATE TABLE IF NOT EXISTS `etudiants` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(50) NOT NULL,
  `Prenom` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `filier_id` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  KEY `FK_etudiants_filieres` (`filier_id`),
  CONSTRAINT `FK_etudiants_filieres` FOREIGN KEY (`filier_id`) REFERENCES `filieres` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=510 DEFAULT CHARSET=latin1;

-- Dumping data for table masterdb.etudiants: ~103 rows (approximately)
/*!40000 ALTER TABLE `etudiants` DISABLE KEYS */;
INSERT INTO `etudiants` (`ID`, `Nom`, `Prenom`, `Email`, `filier_id`) VALUES
	(383, 'aamer', 'youssef', 'aamer.youssef@gmail.com', 1),
	(384, 'ait abderrahman', 'mohamed', 'ait abderrahman.mohamed@gmail.com', 1),
	(385, 'anajjar', 'chaimaa', 'anajjar.chaimaa@gmail.com', 1),
	(386, 'asghar', 'othmane', 'asghar.othmane@gmail.com', 1),
	(387, 'benachour', 'fatine', 'benachour.fatine@gmail.com', 1),
	(388, 'bendhiba', 'soufiane', 'bendhiba.soufiane@gmail.com', 1),
	(389, 'benomar', 'imane', 'benomar.imane@gmail.com', 1),
	(390, 'bouihi', 'mehdi', 'bouihi.mehdi@gmail.com', 1),
	(391, 'boulahia', 'chaimae', 'boulahia.chaimae@gmail.com', 1),
	(392, 'boutaher', 'nadia', 'boutaher.nadia@gmail.com', 1),
	(393, 'brij', 'yassine', 'brij.yassine@gmail.com', 1),
	(394, 'chatbi', 'abdelhalim', 'chatbi.abdelhalim@gmail.com', 1),
	(395, 'elalami', 'mehdi', 'elalami.mehdi@gmail.com', 1),
	(396, 'el manjaoui', 'zineb', 'el manjaoui.zineb@gmail.com', 1),
	(397, 'gordi', 'hasnaa', 'gordi.hasnaa@gmail.com', 1),
	(398, 'hatim', 'widad', 'hatim.widad@gmail.com', 1),
	(399, 'hemmi', 'sara', 'hemmi.sara@gmail.com', 1),
	(400, 'housni', 'shahrazade', 'housni.shahrazade@gmail.com', 1),
	(401, 'izilli', 'abdelhakim', 'izilli.abdelhakim@gmail.com', 1),
	(402, 'jabal', 'imane', 'jabal.imane@gmail.com', 1),
	(403, 'jidar', 'taha', 'jidar.taha@gmail.com', 1),
	(404, 'kamili', 'rachid', 'kamili.rachid@gmail.com', 1),
	(405, 'lahnine', 'walid', 'lahnine.walid@gmail.com', 1),
	(406, 'motad', 'mohamed amine', 'motad.mohamed amine@gmail.com', 1),
	(407, 'moussalli', 'ali', 'moussalli.ali@gmail.com', 1),
	(408, 'nadafi', 'othmane', 'nadafi.othmane@gmail.com', 1),
	(409, 'niri', 'rania', 'niri.rania@gmail.com', 1),
	(410, 'oabi', 'mohammed', 'oabi.mohammed@gmail.com', 1),
	(411, 'outal', 'wajih', 'outal.wajih@gmail.com', 1),
	(412, 'rebik', 'rachid', 'rebik.rachid@gmail.com', 1),
	(413, 'sahnouni', 'tariq', 'sahnouni.tariq@gmail.com', 1),
	(414, 'tegmousse', 'chaimaa', 'tegmousse.chaimaa@gmail.com', 1),
	(415, 'touymasna', 'houssam', 'touymasna.houssam@gmail.com', 1),
	(416, 'wadif', 'salaheddine', 'wadif.salaheddine@gmail.com', 1),
	(417, 'zaazaa', 'mouad', 'zaazaa.mouad@gmail.com', 1),
	(418, 'aater', 'ayoub', 'aater.ayoub@gmail.com', 2),
	(419, 'abbara', 'ghizlane', 'abbara.ghizlane@gmail.com', 2),
	(420, 'abidar', 'mourad', 'abidar.mourad@gmail.com', 2),
	(421, 'alami taidi', 'zineb', 'alami taidi.zineb@gmail.com', 2),
	(422, 'alami taidi', 'abdelkarim', 'alami taidi.abdelkarim@gmail.com', 2),
	(423, 'amnay', 'meriem', 'amnay.meriem@gmail.com', 2),
	(424, 'azima', 'yassine', 'azima.yassine@gmail.com', 2),
	(425, 'bahiddi', 'sara', 'bahiddi.sara@gmail.com', 2),
	(426, 'belbacha', 'el mehdi', 'belbacha.el mehdi@gmail.com', 2),
	(427, 'bella', 'ghizlane', 'bella.ghizlane@gmail.com', 2),
	(428, 'benyoussef', 'el mehdi', 'benyoussef.el mehdi@gmail.com', 2),
	(429, 'bouchra', 'abdelilah', 'bouchra.abdelilah@gmail.com', 2),
	(430, 'benmoussa', 'soukaina', 'benmoussa.soukaina@gmail.com', 2),
	(431, 'bououhrich', 'fatine', 'bououhrich.fatine@gmail.com', 2),
	(432, 'bouzoubaa', 'yassine', 'bouzoubaa.yassine@gmail.com', 2),
	(433, 'chahir', 'sanae', 'chahir.sanae@gmail.com', 2),
	(434, 'charaa', 'safaa', 'charaa.safaa@gmail.com', 2),
	(435, 'chouaf', 'yasser', 'chouaf.yasser@gmail.com', 2),
	(436, 'hammouch', 'soukaina', 'hammouch.soukaina@gmail.com', 2),
	(437, 'el yamlahi', 'oumayma', 'el yamlahi.oumayma@gmail.com', 2),
	(438, 'errammani', 'mouna', 'errammani.mouna@gmail.com', 2),
	(439, 'haress', 'amal', 'haress.amal@gmail.com', 2),
	(440, 'hrar', 'majdouline', 'hrar.majdouline@gmail.com', 2),
	(441, 'khechou', 'amina', 'khechou.amina@gmail.com', 2),
	(442, 'lagraini', 'amina', 'lagraini.amina@gmail.com', 2),
	(443, 'lahkim', 'mohammed', 'lahkim.mohammed@gmail.com', 2),
	(444, 'lamaizi', 'anas', 'lamaizi.anas@gmail.com', 2),
	(445, 'mahassine', 'abdessamad', 'mahassine.abdessamad@gmail.com', 2),
	(446, 'malki', 'nora', 'malki.nora@gmail.com', 2),
	(447, 'mallouk', 'issam', 'mallouk.issam@gmail.com', 2),
	(448, 'oulkhir', 'ayoub', 'oulkhir.ayoub@gmail.com', 2),
	(449, 'rhoulam', 'ghizlane', 'rhoulam.ghizlane@gmail.com', 2),
	(450, 'sabbar', 'soukaina', 'sabbar.soukaina@gmail.com', 2),
	(451, 'saidi idrissi', 'boutaina', 'saidi idrissi.boutaina@gmail.com', 2),
	(452, 'sidibe', 'samuel', 'sidibe.samuel@gmail.com', 2),
	(453, 'tahiri joutei', 'kamar', 'tahiri joutei.kamar@gmail.com', 2),
	(454, 'thoura', 'oussama', 'thoura.oussama@gmail.com', 2),
	(455, 'bachraoui', 'mouad', 'bachraoui.mouad@gmail.com', 2),
	(456, 'yombouna', 'saa m\'bayo', 'yombouna.saa m\'bayo@gmail.com', 2),
	(457, 'akourbi', 'samira', 'akourbi.samira@gmail.com', 3),
	(458, 'bakhout', 'imane', 'bakhout.imane@gmail.com', 3),
	(459, 'bouraba', 'hamza', 'bouraba.hamza@gmail.com', 3),
	(460, 'bourra', 'abdessadek', 'bourra.abdessadek@gmail.com', 3),
	(461, 'boutlaeb houssaini joutei', 'ismail', 'boutlaeb houssaini joutei.ismail@gmail.com', 3),
	(462, 'chabih', 'oussama', 'chabih.oussama@gmail.com', 3),
	(463, 'choukri', 'ihssane', 'choukri.ihssane@gmail.com', 3),
	(464, 'doulyazal', 'widad', 'doulyazal.widad@gmail.com', 3),
	(465, 'draam', 'salma', 'draam.salma@gmail.com', 3),
	(466, 'el alami', 'omar', 'el alami.omar@gmail.com', 3),
	(467, 'el warrak', 'othmane', 'el warrak.othmane@gmail.com', 3),
	(468, 'elaallouli', 'mahmoud', 'elaallouli.mahmoud@gmail.com', 3),
	(469, 'elbahiji', 'salma', 'elbahiji.salma@gmail.com', 3),
	(470, 'elbrigui', 'hassan', 'elbrigui.hassan@gmail.com', 3),
	(471, 'elkamili', 'sanaa', 'elkamili.sanaa@gmail.com', 3),
	(472, 'erafii', 'hasna', 'erafii.hasna@gmail.com', 3),
	(473, 'essouiri', 'ayoub', 'essouiri.ayoub@gmail.com', 3),
	(474, 'hammioui', 'idriss', 'hammioui.idriss@gmail.com', 3),
	(475, 'hankafi', 'abdelalim', 'hankafi.abdelalim@gmail.com', 3),
	(476, 'iraqi', 'camelia', 'iraqi.camelia@gmail.com', 3),
	(477, 'kissami', 'rim', 'kissami.rim@gmail.com', 3),
	(478, 'lafhili', 'fadwa', 'lafhili.fadwa@gmail.com', 3),
	(479, 'mahi', 'zineb', 'mahi.zineb@gmail.com', 3),
	(480, 'masrour', 'kawtar', 'masrour.kawtar@gmail.com', 3),
	(481, 'nadifi', 'hassnae', 'nadifi.hassnae@gmail.com', 3),
	(482, 'ochfy', 'jihane', 'ochfy.jihane@gmail.com', 3),
	(483, 'ouzaani', 'omar', 'ouzaani.omar@gmail.com', 3),
	(484, 'wahabi', 'hind', 'wahabi.hind@gmail.com', 3),
	(485, 'yousri', 'sara', 'yousri.sara@gmail.com', 3);
/*!40000 ALTER TABLE `etudiants` ENABLE KEYS */;


-- Dumping structure for table masterdb.filieres
DROP TABLE IF EXISTS `filieres`;
CREATE TABLE IF NOT EXISTS `filieres` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

-- Dumping data for table masterdb.filieres: ~3 rows (approximately)
/*!40000 ALTER TABLE `filieres` DISABLE KEYS */;
INSERT INTO `filieres` (`ID`, `Nom`) VALUES
	(1, 'bd2c'),
	(2, 'iostl'),
	(3, '3i');
/*!40000 ALTER TABLE `filieres` ENABLE KEYS */;


-- Dumping structure for table masterdb.filieres_modules
DROP TABLE IF EXISTS `filieres_modules`;
CREATE TABLE IF NOT EXISTS `filieres_modules` (
  `id_filiere` int(11) NOT NULL,
  `id_module` int(11) NOT NULL,
  PRIMARY KEY (`id_filiere`,`id_module`),
  KEY `FK__modules` (`id_module`),
  CONSTRAINT `FK__filieres` FOREIGN KEY (`id_filiere`) REFERENCES `filieres` (`ID`),
  CONSTRAINT `FK__modules` FOREIGN KEY (`id_module`) REFERENCES `modules` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Dumping data for table masterdb.filieres_modules: ~0 rows (approximately)
/*!40000 ALTER TABLE `filieres_modules` DISABLE KEYS */;
INSERT INTO `filieres_modules` (`id_filiere`, `id_module`) VALUES
	(1, 1),
	(1, 2),
	(3, 2),
	(1, 3),
	(3, 3),
	(1, 4),
	(1, 5),
	(2, 5),
	(1, 6),
	(2, 6),
	(2, 7),
	(2, 8),
	(2, 9),
	(2, 10),
	(3, 10),
	(2, 11),
	(3, 11),
	(2, 12),
	(2, 13),
	(3, 14),
	(3, 15),
	(3, 16);
/*!40000 ALTER TABLE `filieres_modules` ENABLE KEYS */;


-- Dumping structure for table masterdb.modules
DROP TABLE IF EXISTS `modules`;
CREATE TABLE IF NOT EXISTS `modules` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Nom` varchar(50) NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;

-- Dumping data for table masterdb.modules: ~6 rows (approximately)
/*!40000 ALTER TABLE `modules` DISABLE KEYS */;
INSERT INTO `modules` (`ID`, `Nom`) VALUES
	(1, 'Anglais'),
	(2, 'Web Sémantique'),
	(3, 'Bases de Données Avancées'),
	(4, 'Intelligence Artificielle'),
	(5, 'Statistique Inférencielle'),
	(6, 'Programmation Python'),
	(7, 'xml'),
	(8, 'Programmation lineaire avancée'),
	(9, 'Théorie des graphes'),
	(10, 'JEE'),
	(11, 'ASP.net'),
	(12, 'buisness intelligence'),
	(13, 'communication'),
	(14, 'IDM'),
	(15, 'algorithmiques'),
	(16, 'cryptographie');
/*!40000 ALTER TABLE `modules` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
