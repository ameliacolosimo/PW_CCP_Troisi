-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Creato il: Nov 11, 2020 alle 19:03
-- Versione del server: 10.4.14-MariaDB
-- Versione PHP: 7.3.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `acme_energia`
--

-- --------------------------------------------------------

--
-- Struttura della tabella `bollette_emesse`
--

CREATE TABLE `bollette_emesse` (
  `id_bolletta_emessa` int(11) NOT NULL,
  `id_utente` int(11) DEFAULT NULL,
  `quantita` int(20) DEFAULT NULL,
  `id_contratto` int(11) DEFAULT NULL,
  `tariffa` double(13,3) DEFAULT NULL,
  `importo` double(13,3) DEFAULT NULL,
  `periodo_riferimento` varchar(50) DEFAULT NULL,
  `data_emissione` date DEFAULT NULL,
  `data_scadenza` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `bollette_emesse`
--

INSERT INTO `bollette_emesse` (`id_bolletta_emessa`, `id_utente`, `quantita`, `id_contratto`, `tariffa`, `importo`, `periodo_riferimento`, `data_emissione`, `data_scadenza`) VALUES
(1, 1, 1253, 1, 0.200, 250.600, '\"Maggio-Luglio\"', '2020-07-10', '2020-07-25'),
(2, 2, 1111, 2, 0.200, 222.200, '\"Gemmaio-Marzo\"', '2020-03-02', '2020-03-17'),
(3, 3, 20140, 3, 0.200, 4914.160, '\"Marzo-Maggio\"', '2020-05-10', '2020-05-25'),
(4, 4, 134, 4, 0.200, 26.800, '\"Luglio-Settembre\"', '2020-09-03', '2020-09-18'),
(5, 5, 8556, 5, 0.200, 2087.664, '\"Settembre-Novembre\"', '2020-11-05', '2020-11-20'),
(6, 6, 109, 6, 0.200, 21.800, '\"Marzo-Maggio\"', '2020-05-10', '2020-05-25'),
(7, 7, 52512, 7, 0.200, 12812.928, '\"Marzo-Maggio\"', '2020-05-04', '2020-05-19'),
(8, 8, 35102, 8, 0.200, 8564.888, '\"Luglio-Settembre\"', '2020-09-01', '2020-09-16'),
(9, 9, 117, 9, 0.200, 23.400, '\"Settembre-Novembre\"', '2020-11-04', '2020-11-15'),
(10, 10, 13645, 10, 0.200, 3329.380, '\"Marzo-Maggio\"', '2020-05-20', '2020-06-04'),
(11, 11, 20209, 11, 0.200, 4930.996, '\"Gennaio-Marzo\"', '2020-03-03', '2020-03-18'),
(12, 12, 111, 12, 0.200, 22.200, '\"GennaiO-Marzo\"', '2020-03-15', '2020-03-30'),
(13, 13, 201, 13, 0.200, 40.200, '\"Marzo-Maggio\"', '2020-05-11', '2020-05-26'),
(14, 14, 22167, 14, 0.200, 5408.748, '\"Luglio-Settembre\"', '2020-09-05', '2020-09-20'),
(15, 15, 90, 15, 0.200, 18.000, '\"Luglio-Settembre\"', '2020-09-15', '2020-09-30'),
(16, 2, 153, 2, 0.200, 30.600, '\"Marzo-Maggio\"', '2020-05-15', '2020-05-30'),
(17, 4, 222, 4, 0.200, 44.400, '\"Marzo-Maggio\"', '2020-05-15', '2020-05-30'),
(18, 6, 309, 6, 0.200, 61.800, '\"Marzo-Maggio\"', '2020-05-07', '2020-05-22'),
(19, 8, 21981, 8, 0.200, 5363.364, '\"Gennaio-Marzo\"', '2020-03-05', '2020-03-20'),
(20, 10, 22261, 10, 0.200, 5431.684, '\"Settembre-Novembre\"', '2020-09-05', '2020-09-20');

-- --------------------------------------------------------

--
-- Struttura della tabella `bollette_pagate`
--

CREATE TABLE `bollette_pagate` (
  `id_bolletta_pagata` int(11) NOT NULL,
  `id_bolletta_emessa` int(11) DEFAULT NULL,
  `data_pagamento` date DEFAULT NULL,
  `id_istituto` int(11) DEFAULT NULL,
  `id_utente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `bollette_pagate`
--

INSERT INTO `bollette_pagate` (`id_bolletta_pagata`, `id_bolletta_emessa`, `data_pagamento`, `id_istituto`, `id_utente`) VALUES
(1, 1, '2020-07-15', 1, 1),
(2, 2, '2020-03-10', 2, 2),
(3, 3, '2020-05-11', 3, 3),
(4, 4, '2020-09-09', 4, 4),
(5, 5, '2020-11-17', 5, 5),
(6, 7, '2020-05-18', 7, 7),
(7, 8, '2020-09-14', 8, 8),
(8, 9, '2020-11-12', 9, 9),
(9, 10, '2020-05-25', 10, 10),
(10, 12, '2020-03-16', 12, 12),
(11, 15, '2020-09-25', 15, 15),
(12, 16, '2020-05-20', 2, 2),
(13, 17, '2020-05-20', 4, 4),
(14, 19, '2020-03-10', 8, 8),
(15, 20, '2020-09-10', 10, 10);

-- --------------------------------------------------------

--
-- Struttura della tabella `contatori`
--

CREATE TABLE `contatori` (
  `id_contatore` int(11) NOT NULL,
  `id_utente` int(11) DEFAULT NULL,
  `quantità_totale` double(13,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `contatori`
--

INSERT INTO `contatori` (`id_contatore`, `id_utente`, `quantità_totale`) VALUES
(1, 1, 367897834.000),
(2, 2, 3432566435.000),
(3, 2, 455661356.000),
(4, 1, 667465778.000),
(5, 6, 1000239656.000),
(6, 3, 448245632.000),
(7, 4, 9812007539.000),
(8, 5, 1134227539.000),
(9, 7, 3302846541.000),
(10, 8, 210093214.000),
(11, 9, 4533997412.000),
(12, 10, 812740954.000),
(13, 3, 112878541.000),
(14, 2, 672195951.000),
(15, 10, 20065498.000),
(16, 11, 485295545.000),
(17, 12, 894516541.000),
(18, 13, 646565416.000),
(19, 15, 654665656.000),
(20, 14, 516146562.000);

-- --------------------------------------------------------

--
-- Struttura della tabella `contratti`
--

CREATE TABLE `contratti` (
  `id_contratto` int(11) NOT NULL,
  `cod_contratto` varchar(10) DEFAULT NULL,
  `descrizione` varchar(50) DEFAULT NULL,
  `id_utente` int(11) DEFAULT NULL,
  `status_contratti` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `contratti`
--

INSERT INTO `contratti` (`id_contratto`, `cod_contratto`, `descrizione`, `id_utente`, `status_contratti`) VALUES
(1, 'A12', 'GAS', 1, 'attivo'),
(2, 'B23', 'ACQUA', 2, 'attivo'),
(3, 'A34', 'LUCE', 3, 'attivo'),
(4, 'C34', 'ACQUA', 4, 'attivo'),
(5, 'A23', 'LUCE', 5, 'attivo'),
(6, 'D34', 'GAS', 6, 'sospeso'),
(7, 'A45', 'GAS', 7, 'attivo'),
(8, 'E45', 'LUCE', 8, 'attivo'),
(9, 'A67', 'ACQUA', 9, 'attivo'),
(10, 'E98', 'GAS', 10, 'attivo'),
(11, 'E34', 'LUCE', 11, 'attivo'),
(12, 'E87', 'ACQUA', 12, 'attivo'),
(13, 'A56', 'GAS', 13, 'sospeso'),
(14, 'G56', 'LUCE', 14, 'sospeso'),
(15, 'E98', 'GAS', 15, 'attivo');

-- --------------------------------------------------------

--
-- Struttura della tabella `dw_bolletta`
--

CREATE TABLE `dw_bolletta` (
  `ID_bolletta` int(11) NOT NULL,
  `cod_bolletta` int(11) DEFAULT NULL,
  `tariffa` double(13,3) DEFAULT NULL,
  `cod_contratto` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `dw_bolletta`
--

INSERT INTO `dw_bolletta` (`ID_bolletta`, `cod_bolletta`, `tariffa`, `cod_contratto`) VALUES
(1, 1, 0.200, 1),
(2, 2, 0.200, 2),
(3, 3, 0.200, 3),
(4, 4, 0.200, 4),
(5, 5, 0.200, 5),
(6, 6, 0.200, 6),
(7, 7, 0.200, 7),
(8, 8, 0.200, 8),
(9, 9, 0.200, 9),
(10, 10, 0.200, 10),
(11, 11, 0.200, 11),
(12, 12, 0.200, 12),
(13, 13, 0.200, 13),
(14, 14, 0.200, 14),
(15, 15, 0.200, 15),
(16, 16, 0.200, 2),
(17, 17, 0.200, 4),
(18, 18, 0.200, 6),
(19, 19, 0.200, 8),
(20, 20, 0.200, 10);

-- --------------------------------------------------------

--
-- Struttura della tabella `dw_citta`
--

CREATE TABLE `dw_citta` (
  `ID_citta` int(11) NOT NULL,
  `citta_utente` int(11) DEFAULT NULL,
  `citta` varchar(50) DEFAULT NULL,
  `CAP` char(5) DEFAULT NULL,
  `provincia` char(2) DEFAULT NULL,
  `regione` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `dw_citta`
--

INSERT INTO `dw_citta` (`ID_citta`, `citta_utente`, `citta`, `CAP`, `provincia`, `regione`) VALUES
(1, 1, 'Pizzo', '89812', 'VV', 'Calabria'),
(2, 2, 'Napoli', '65478', 'NA', 'Campania'),
(3, 3, 'Roma', '00181', 'RM', 'Lazio'),
(4, 4, 'Roma', '00456', 'RM', 'Lazio'),
(5, 5, 'Milano', '56789', 'MI', 'Lombardia'),
(6, 6, 'Bologna', '56789', 'BO', 'Emilia-Romagna'),
(7, 7, 'Maierato', '45679', 'VV', 'Calabria'),
(8, 8, 'Venezia', '53492', 'VE', 'Veneto'),
(9, 9, 'Torino', '45678', 'TO', 'Veneto'),
(10, 10, 'Firenze', '56788', 'FI', 'Toscana'),
(11, 11, 'Milano', '56789', 'MI', 'Lombardia'),
(12, 12, 'Milano', '67899', 'MI', 'Lombardia'),
(13, 13, 'Roma', '45678', 'RM', 'Lazio'),
(14, 14, 'Torino', '67487', 'TO', 'Piemonte'),
(15, 15, 'Bologna', '56787', 'B0', 'Emilia-Romagna');

-- --------------------------------------------------------

--
-- Struttura della tabella `dw_contratti`
--

CREATE TABLE `dw_contratti` (
  `ID_Contratto` int(11) NOT NULL,
  `cpd_contratto` int(11) DEFAULT NULL,
  `periodo` int(11) DEFAULT NULL,
  `status_contratto` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `dw_contratti`
--

INSERT INTO `dw_contratti` (`ID_Contratto`, `cpd_contratto`, `periodo`, `status_contratto`) VALUES
(1, 1, NULL, 'attivo'),
(2, 2, NULL, 'attivo'),
(3, 3, NULL, 'attivo'),
(4, 4, NULL, 'attivo'),
(5, 5, NULL, 'attivo'),
(6, 6, NULL, 'sospeso'),
(7, 7, NULL, 'attivo'),
(8, 8, NULL, 'attivo'),
(9, 9, NULL, 'attivo'),
(10, 10, NULL, 'attivo'),
(11, 11, NULL, 'attivo'),
(12, 12, NULL, 'attivo'),
(13, 13, NULL, 'sospeso'),
(14, 14, NULL, 'sospeso'),
(15, 15, NULL, 'attivo');

-- --------------------------------------------------------

--
-- Struttura della tabella `dw_data`
--

CREATE TABLE `dw_data` (
  `ID_data` int(11) NOT NULL,
  `cod_data` int(11) DEFAULT NULL,
  `data_t0` date DEFAULT NULL,
  `data_t1` date DEFAULT NULL,
  `mese_t0` int(2) DEFAULT NULL,
  `mese_t1` int(2) DEFAULT NULL,
  `anno_t0` int(4) DEFAULT NULL,
  `anno_t1` int(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `dw_data`
--

INSERT INTO `dw_data` (`ID_data`, `cod_data`, `data_t0`, `data_t1`, `mese_t0`, `mese_t1`, `anno_t0`, `anno_t1`) VALUES
(1, 1, '2020-05-10', '2020-07-07', 5, 7, 2020, 2020),
(2, 2, '2020-01-01', '2020-02-28', 1, 2, 2020, 2020),
(3, 3, '0020-03-25', '2020-05-02', 3, 5, 20, 2020),
(4, 4, '2020-07-18', '2020-09-01', 7, 9, 2020, 2020),
(5, 5, '2020-09-10', '2020-10-30', 9, 10, 2020, 2020),
(6, 6, '2020-03-10', '2020-05-01', 3, 5, 2020, 2020),
(7, 7, '2020-03-04', '2020-04-30', 3, 4, 2020, 2020),
(8, 8, '2020-07-01', '2020-08-15', 7, 8, 2020, 2020),
(9, 9, '2020-09-04', '2020-10-27', 9, 10, 2020, 2020),
(10, 10, '2020-03-20', '2020-05-02', 3, 5, 2020, 2020),
(11, 11, '2020-01-01', '2020-02-28', 1, 2, 2020, 2020),
(12, 12, '2020-01-15', '2020-03-01', 1, 3, 2020, 2020),
(13, 13, '2020-03-11', '2020-05-05', 3, 5, 2020, 2020),
(14, 14, '2020-07-05', '2020-09-01', 7, 9, 2020, 2020),
(15, 15, '2020-07-15', '2020-09-04', 7, 9, 2020, 2020),
(16, 16, '2020-03-10', '2020-05-01', 3, 5, 2020, 2020),
(17, 17, '2020-03-04', '2020-04-30', 3, 4, 2020, 2020),
(18, 18, '2020-03-20', '2020-05-02', 3, 5, 2020, 2020),
(19, 19, '2020-01-01', '2020-02-28', 1, 2, 2020, 2020),
(20, 20, '2020-07-18', '2020-09-01', 7, 9, 2020, 2020);

-- --------------------------------------------------------

--
-- Struttura della tabella `dw_utente`
--

CREATE TABLE `dw_utente` (
  `ID_utente` int(11) NOT NULL,
  `cod_utente` int(11) DEFAULT NULL,
  `solvibilita` varchar(30) DEFAULT NULL,
  `tipologia` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `dw_utente`
--

INSERT INTO `dw_utente` (`ID_utente`, `cod_utente`, `solvibilita`, `tipologia`) VALUES
(1, 1, 'in regola', 'privato'),
(2, 2, 'in regola', 'privato'),
(3, 3, 'moroso', 'azienda'),
(4, 4, 'in regola', 'privato'),
(5, 5, 'in regola', 'azienda'),
(6, 6, 'moroso grave', 'privato'),
(7, 7, 'in regola', 'azienda'),
(8, 8, 'in regola', 'azienda'),
(9, 9, 'in regola', 'privato'),
(10, 10, 'in regola', 'azienda'),
(11, 11, 'moroso', 'azienda'),
(12, 12, 'in regola', 'privato'),
(13, 13, 'moroso grave', 'privato'),
(14, 14, 'moroso grave', 'azienda'),
(15, 15, 'in regola', 'privato');

-- --------------------------------------------------------

--
-- Struttura della tabella `fatto_consumi`
--

CREATE TABLE `fatto_consumi` (
  `ID_bolletta` int(11) DEFAULT NULL,
  `ID_citta` int(11) DEFAULT NULL,
  `ID_utente` int(11) DEFAULT NULL,
  `ID_data` int(11) DEFAULT NULL,
  `num_utenti` int(11) DEFAULT NULL,
  `importo_tot` double(13,3) DEFAULT NULL,
  `qta_kW_tot` double(13,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `fatto_consumi`
--

INSERT INTO `fatto_consumi` (`ID_bolletta`, `ID_citta`, `ID_utente`, `ID_data`, `num_utenti`, `importo_tot`, `qta_kW_tot`) VALUES
(1, 1, 1, 1, NULL, 250.600, 1253.000),
(2, 2, 2, 2, NULL, 222.200, 1111.000),
(16, 2, 2, 16, NULL, 30.600, 1111.000),
(3, 3, 3, 3, NULL, 4914.160, 109.000),
(4, 4, 4, 4, NULL, 26.800, 52512.000),
(17, 4, 4, 17, NULL, 44.400, 52512.000),
(5, 5, 5, 5, NULL, 2087.664, 35102.000),
(6, 6, 6, 6, NULL, 21.800, 8556.000),
(18, 6, 6, 18, NULL, 61.800, 8556.000),
(7, 7, 7, 7, NULL, 12812.928, 117.000),
(8, 8, 8, 8, NULL, 8564.888, 13745.000),
(19, 8, 8, 19, NULL, 5363.364, 13745.000),
(9, 9, 9, 9, NULL, 23.400, 20209.000),
(10, 10, 10, 10, NULL, 3329.380, 111.000),
(20, 10, 10, 20, NULL, 5431.684, 111.000),
(11, 11, 11, 11, NULL, 4930.996, 153.000),
(12, 12, 12, 12, NULL, 22.200, 222.000),
(13, 13, 13, 13, NULL, 40.200, 309.000),
(14, 14, 14, 14, NULL, 5408.748, 22261.000),
(15, 15, 15, 15, NULL, 18.000, 21981.000);

-- --------------------------------------------------------

--
-- Struttura della tabella `fatto_vendite`
--

CREATE TABLE `fatto_vendite` (
  `ID_utente` int(11) DEFAULT NULL,
  `ID_Contratto` int(11) DEFAULT NULL,
  `tot_spesa` double(13,3) DEFAULT NULL,
  `tot_quantita` double(13,3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `fatto_vendite`
--

INSERT INTO `fatto_vendite` (`ID_utente`, `ID_Contratto`, `tot_spesa`, `tot_quantita`) VALUES
(1, 1, 250.600, 1253.000),
(2, 2, 252.800, 1264.000),
(3, 3, 4914.160, 20140.000),
(4, 4, 71.200, 356.000),
(5, 5, 2087.664, 8556.000),
(6, 6, 83.600, 418.000),
(7, 7, 12812.928, 52512.000),
(8, 8, 13928.252, 57083.000),
(9, 9, 23.400, 117.000),
(10, 10, 8761.064, 35906.000),
(11, 11, 4930.996, 20209.000),
(12, 12, 22.200, 111.000),
(13, 13, 40.200, 201.000),
(14, 14, 5408.748, 22167.000),
(15, 15, 18.000, 90.000);

-- --------------------------------------------------------

--
-- Struttura della tabella `guasti`
--

CREATE TABLE `guasti` (
  `id_guasto` int(11) NOT NULL,
  `id_contatore` int(11) DEFAULT NULL,
  `data_inizio` date DEFAULT NULL,
  `data_fine` date DEFAULT NULL,
  `ora_inizio` time DEFAULT NULL,
  `ora_fine` time DEFAULT NULL,
  `descrizione` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `guasti`
--

INSERT INTO `guasti` (`id_guasto`, `id_contatore`, `data_inizio`, `data_fine`, `ora_inizio`, `ora_fine`, `descrizione`) VALUES
(1, 1, '2020-07-10', '2020-07-10', '09:00:00', '10:00:00', 'guasti al contatore'),
(2, 2, '2020-10-07', '2020-10-07', '12:00:00', '00:00:00', 'pericolo relativo al contatore o alla rete esterna'),
(3, 3, '2020-11-09', '2020-11-09', '06:00:00', '23:00:00', 'interruzioni di corrente elettrica'),
(4, 4, '2020-12-15', '2020-12-15', '12:00:00', '03:00:00', 'anomalie sulla rete esterna'),
(5, 5, '2020-01-31', '2020-02-01', '23:50:00', '00:05:00', 'guasti al contatore'),
(6, 6, '2020-11-11', '2020-11-11', '16:00:00', '16:50:00', 'interruzioni di corrente elettrica'),
(7, 7, '2020-01-04', '2020-01-04', '15:00:00', '19:00:00', 'anomalie sulla rete esterna'),
(8, 8, '2020-03-12', '2020-03-12', '22:00:00', '23:50:00', 'pericolo relativo al contatore o alla rete esterna'),
(9, 9, '2020-04-08', '2020-04-08', '20:50:00', '23:50:00', 'pericolo relativo al contatore o alla rete esterna'),
(10, 10, '2020-05-04', '2020-05-04', '15:35:00', '19:22:00', 'anomalie sulla rete esterna'),
(11, 11, '2020-09-11', '2020-09-11', '08:00:00', '16:50:00', 'interruzioni di corrente elettrica'),
(12, 12, '2020-07-10', '2020-08-10', '09:00:00', '10:00:00', 'guasti al contatore'),
(13, 13, '2020-06-13', '2020-06-13', '10:40:00', '11:50:00', 'interruzioni di corrente elettrica'),
(14, 14, '2020-02-02', '2020-02-02', '17:35:00', '23:46:00', 'anomalie sulla rete esterna'),
(15, 15, '2020-08-31', '2020-09-01', '23:50:00', '00:05:00', 'guasti al contatore'),
(16, 16, '2020-12-11', '2020-12-11', '14:00:00', '16:50:00', 'anomalie sulla rete esterna'),
(17, 17, '2020-02-04', '2020-02-04', '13:00:00', '15:00:00', 'interruzioni di corrente elettrica'),
(18, 18, '2020-03-15', '2020-03-15', '21:00:00', '23:48:00', 'pericolo relativo al contatore o alla rete esterna'),
(19, 19, '2020-06-08', '2020-06-08', '12:50:00', '14:50:00', 'guasti al contatore'),
(20, 20, '2020-05-14', '2020-05-14', '16:35:00', '19:22:00', 'anomalie sulla rete esterna');

-- --------------------------------------------------------

--
-- Struttura della tabella `istituti_di_pagamento`
--

CREATE TABLE `istituti_di_pagamento` (
  `id_istituto` int(11) NOT NULL,
  `tipologia_istituto` varchar(10) DEFAULT NULL,
  `indirizzo` varchar(50) DEFAULT NULL,
  `citta` varchar(50) DEFAULT NULL,
  `provincia` char(2) DEFAULT NULL,
  `CAP` char(5) DEFAULT NULL,
  `id_utente` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `istituti_di_pagamento`
--

INSERT INTO `istituti_di_pagamento` (`id_istituto`, `tipologia_istituto`, `indirizzo`, `citta`, `provincia`, `CAP`, `id_utente`) VALUES
(1, 'BANCA', 'Via Colpu', 'Pizzo', 'VV', '89812', 1),
(2, 'POSTA', 'Via Pignatta', 'Napoli', 'NA', '65478', 2),
(3, 'POSTA', 'Via Appia Nuova', 'Roma', 'RM', '00181', 3),
(4, 'BANCA', 'Via Torlonia', 'Roma', 'RM', '00456', 4),
(5, 'BANCA', 'Via Giunco', 'Milano', 'MI', '56789', 5),
(6, 'POSTA', 'Via Siracusa', 'Bologna', 'BO', '56789', 6),
(7, 'POSTA', 'Via Sant Antonio', 'Maierato', 'VV', '45679', 7),
(8, 'BANCA', 'Via Unità D Italia', 'Venezia', 'VE', '53492', 8),
(9, 'POSTA', 'Via Sant Antonio', 'Maierato', 'VV', '45679', 9),
(10, 'BANCA', 'Via Simone', 'Firenze', 'FI', '56788', 10),
(11, 'POSTA', 'Viale Silco', 'Milano', 'MI', '56789', 11),
(12, 'POSTA', 'Via Frico', 'Milano', 'MI', '67899', 12),
(13, 'BANCA', 'Via Giuncolo', 'Roma', 'RM', '45678', 13),
(14, 'BANCA', 'Via Ara', 'Torino', 'TO', '67487', 14),
(15, 'POSTA', 'Via Fruci', 'Bologna', 'B0', '56787', 15);

-- --------------------------------------------------------

--
-- Struttura della tabella `lettura_consumi`
--

CREATE TABLE `lettura_consumi` (
  `id_lettura` int(11) NOT NULL,
  `id_contatore` int(11) DEFAULT NULL,
  `id_utente` int(11) DEFAULT NULL,
  `livello_soglia` varchar(30) DEFAULT NULL,
  `lettura1` double(13,3) DEFAULT NULL,
  `lettura2` double(13,3) DEFAULT NULL,
  `quantita` int(20) DEFAULT NULL,
  `data_lettura1` datetime DEFAULT NULL,
  `data_lettura2` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `lettura_consumi`
--

INSERT INTO `lettura_consumi` (`id_lettura`, `id_contatore`, `id_utente`, `livello_soglia`, `lettura1`, `lettura2`, `quantita`, `data_lettura1`, `data_lettura2`) VALUES
(1, 1, 1, 'basso', 1092.000, 2345.000, 1253, '2020-05-10 00:00:00', '2020-07-07 00:00:00'),
(2, 2, 2, 'alto', 2345.000, 3456.000, 1111, '2020-01-01 00:00:00', '2020-02-28 00:00:00'),
(3, 3, 3, 'alto', 23445.000, 43585.000, 20140, '0020-03-25 00:00:00', '2020-05-02 00:00:00'),
(4, 4, 4, 'basso', 100.000, 234.000, 134, '2020-07-18 00:00:00', '2020-09-01 00:00:00'),
(5, 5, 5, 'basso', 56789.000, 65345.000, 8556, '2020-09-10 00:00:00', '2020-10-30 00:00:00'),
(6, 6, 6, 'basso', 123.000, 232.000, 109, '2020-03-10 00:00:00', '2020-05-01 00:00:00'),
(7, 7, 7, 'alto', 12113.000, 64625.000, 52512, '2020-03-04 00:00:00', '2020-04-30 00:00:00'),
(8, 8, 8, 'alto', 1224.000, 36326.000, 35102, '2020-07-01 00:00:00', '2020-08-15 00:00:00'),
(9, 9, 9, 'basso', 235.000, 352.000, 117, '2020-09-04 00:00:00', '2020-10-27 00:00:00'),
(10, 10, 10, 'alto', 45778.000, 59323.000, 13745, '2020-03-20 00:00:00', '2020-05-02 00:00:00'),
(11, 11, 11, 'basso', 12345.000, 32554.000, 20209, '2020-01-01 00:00:00', '2020-02-28 00:00:00'),
(12, 12, 12, 'basso', 234.000, 345.000, 111, '2020-01-15 00:00:00', '2020-03-01 00:00:00'),
(13, 13, 13, 'alto', 345.000, 546.000, 201, '2020-03-11 00:00:00', '2020-05-05 00:00:00'),
(14, 14, 14, 'basso', 34567.000, 56734.000, 22167, '2020-07-05 00:00:00', '2020-09-01 00:00:00'),
(15, 15, 15, 'alto', 345.000, 435.000, 90, '2020-07-15 00:00:00', '2020-09-04 00:00:00'),
(16, 16, 2, 'basso', 234.000, 387.000, 153, '2020-03-10 00:00:00', '2020-05-01 00:00:00'),
(17, 17, 4, 'alto', 123.000, 345.000, 222, '2020-03-04 00:00:00', '2020-04-30 00:00:00'),
(18, 18, 6, 'alto', 345.000, 654.000, 309, '2020-03-20 00:00:00', '2020-05-02 00:00:00'),
(19, 19, 8, 'alto', 45673.000, 67654.000, 21981, '2020-01-01 00:00:00', '2020-02-28 00:00:00'),
(20, 20, 14, 'basso', 34523.000, 56784.000, 22261, '2020-07-18 00:00:00', '2020-09-01 00:00:00');

-- --------------------------------------------------------

--
-- Struttura della tabella `utenti`
--

CREATE TABLE `utenti` (
  `id_utente` int(11) NOT NULL,
  `nome` varchar(50) DEFAULT NULL,
  `cognome` varchar(50) DEFAULT NULL,
  `indirizzo` varchar(50) DEFAULT NULL,
  `citta` varchar(50) DEFAULT NULL,
  `provincia` char(2) DEFAULT NULL,
  `CAP` char(5) DEFAULT NULL,
  `regime_fiscale` varchar(30) DEFAULT NULL,
  `solvibilita` varchar(30) DEFAULT NULL,
  `tipologia_cliente` varchar(30) DEFAULT NULL,
  `regione` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dump dei dati per la tabella `utenti`
--

INSERT INTO `utenti` (`id_utente`, `nome`, `cognome`, `indirizzo`, `citta`, `provincia`, `CAP`, `regime_fiscale`, `solvibilita`, `tipologia_cliente`, `regione`) VALUES
(1, 'Mario', 'Rossi', 'Via Nazionale', 'Pizzo', 'VV', '89812', 'soggetto a IVA', 'in regola', 'privato', 'Calabria'),
(2, 'Marica', 'Marchese', 'Via Pignatta', 'Napoli', 'NA', '65478', 'soggetto a IVA', 'in regola', 'privato', 'Campania'),
(3, 'Luca', 'Gammo', 'Via Appia Nuova', 'Roma', 'RM', '00181', 'esente IVA', 'moroso', 'azienda', 'Lazio'),
(4, 'Rocco', 'Stillitani', 'Via XXV Aprile', 'Roma', 'RM', '00456', 'soggetto a IVA', 'in regola', 'privato', 'Lazio'),
(5, 'Rossana', 'Gallo', 'Viale Arcala', 'Milano', 'MI', '56789', 'esente IVA', 'in regola', 'azienda', 'Lombardia'),
(6, 'Federica', 'Galfo', 'Via Siracusa', 'Bologna', 'BO', '56789', 'soggetto a IVA', 'moroso grave', 'privato', 'Emilia-Romagna'),
(7, 'Carmela', 'Cortese', 'Via Sant Antonio', 'Maierato', 'VV', '45679', 'esente IVA', 'in regola', 'azienda', 'Calabria'),
(8, 'Filippo', 'Callipo', 'Via Milino', 'Venezia', 'VE', '53492', 'esente IVA', 'in regola', 'azienda', 'Veneto'),
(9, 'Miriam', 'Cugliari', 'Via Ripa', 'Torino', 'TO', '45678', 'soggetto a IVA', 'in regola', 'privato', 'Veneto'),
(10, 'Francesca', 'De Pasquale', 'Via Torli', 'Firenze', 'FI', '56788', 'esente IVA', 'in regola', 'azienda', 'Toscana'),
(11, 'Giuseppe', 'Calfapietra', 'Viale Silco', 'Milano', 'MI', '56789', 'esente IVA', 'moroso', 'azienda', 'Lombardia'),
(12, 'Lucia', 'Conti', 'Via Frico', 'Milano', 'MI', '67899', 'soggetto a IVA', 'in regola', 'privato', 'Lombardia'),
(13, 'Marco', 'Porcella', 'Viale Fiorito', 'Roma', 'RM', '45678', 'soggetto a IVA', 'moroso grave', 'privato', 'Lazio'),
(14, 'Andrea', 'Lepanto', 'Via Po', 'Torino', 'TO', '67487', 'esente IVA', 'moroso grave', 'azienda', 'Piemonte'),
(15, 'Sara', 'Giuliani', 'Via Fruci', 'Bologna', 'B0', '56787', 'soggetto a IVA', 'in regola', 'privato', 'Emilia-Romagna');

--
-- Indici per le tabelle scaricate
--

--
-- Indici per le tabelle `bollette_emesse`
--
ALTER TABLE `bollette_emesse`
  ADD PRIMARY KEY (`id_bolletta_emessa`);

--
-- Indici per le tabelle `bollette_pagate`
--
ALTER TABLE `bollette_pagate`
  ADD PRIMARY KEY (`id_bolletta_pagata`);

--
-- Indici per le tabelle `contatori`
--
ALTER TABLE `contatori`
  ADD PRIMARY KEY (`id_contatore`);

--
-- Indici per le tabelle `contratti`
--
ALTER TABLE `contratti`
  ADD PRIMARY KEY (`id_contratto`);

--
-- Indici per le tabelle `dw_bolletta`
--
ALTER TABLE `dw_bolletta`
  ADD PRIMARY KEY (`ID_bolletta`);

--
-- Indici per le tabelle `dw_citta`
--
ALTER TABLE `dw_citta`
  ADD PRIMARY KEY (`ID_citta`);

--
-- Indici per le tabelle `dw_contratti`
--
ALTER TABLE `dw_contratti`
  ADD PRIMARY KEY (`ID_Contratto`);

--
-- Indici per le tabelle `dw_data`
--
ALTER TABLE `dw_data`
  ADD PRIMARY KEY (`ID_data`);

--
-- Indici per le tabelle `dw_utente`
--
ALTER TABLE `dw_utente`
  ADD PRIMARY KEY (`ID_utente`);

--
-- Indici per le tabelle `guasti`
--
ALTER TABLE `guasti`
  ADD PRIMARY KEY (`id_guasto`);

--
-- Indici per le tabelle `istituti_di_pagamento`
--
ALTER TABLE `istituti_di_pagamento`
  ADD PRIMARY KEY (`id_istituto`);

--
-- Indici per le tabelle `lettura_consumi`
--
ALTER TABLE `lettura_consumi`
  ADD PRIMARY KEY (`id_lettura`);

--
-- Indici per le tabelle `utenti`
--
ALTER TABLE `utenti`
  ADD PRIMARY KEY (`id_utente`);

--
-- AUTO_INCREMENT per le tabelle scaricate
--

--
-- AUTO_INCREMENT per la tabella `bollette_emesse`
--
ALTER TABLE `bollette_emesse`
  MODIFY `id_bolletta_emessa` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT per la tabella `bollette_pagate`
--
ALTER TABLE `bollette_pagate`
  MODIFY `id_bolletta_pagata` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=99;

--
-- AUTO_INCREMENT per la tabella `contatori`
--
ALTER TABLE `contatori`
  MODIFY `id_contatore` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT per la tabella `contratti`
--
ALTER TABLE `contratti`
  MODIFY `id_contratto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT per la tabella `dw_bolletta`
--
ALTER TABLE `dw_bolletta`
  MODIFY `ID_bolletta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT per la tabella `dw_citta`
--
ALTER TABLE `dw_citta`
  MODIFY `ID_citta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT per la tabella `dw_contratti`
--
ALTER TABLE `dw_contratti`
  MODIFY `ID_Contratto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT per la tabella `dw_data`
--
ALTER TABLE `dw_data`
  MODIFY `ID_data` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT per la tabella `dw_utente`
--
ALTER TABLE `dw_utente`
  MODIFY `ID_utente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT per la tabella `guasti`
--
ALTER TABLE `guasti`
  MODIFY `id_guasto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT per la tabella `istituti_di_pagamento`
--
ALTER TABLE `istituti_di_pagamento`
  MODIFY `id_istituto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT per la tabella `lettura_consumi`
--
ALTER TABLE `lettura_consumi`
  MODIFY `id_lettura` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT per la tabella `utenti`
--
ALTER TABLE `utenti`
  MODIFY `id_utente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
