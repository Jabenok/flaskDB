-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1
-- Время создания: Апр 22 2025 г., 23:03
-- Версия сервера: 10.4.32-MariaDB
-- Версия PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `universitydb`
--

-- --------------------------------------------------------

--
-- Структура таблицы `changelog`
--

CREATE TABLE `changelog` (
  `ID` int(11) NOT NULL,
  `TableName` varchar(50) DEFAULT NULL,
  `Action` varchar(50) DEFAULT NULL,
  `ChangedData` text DEFAULT NULL,
  `ChangeDate` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `changelog`
--

INSERT INTO `changelog` (`ID`, `TableName`, `Action`, `ChangedData`, `ChangeDate`) VALUES
(1, 'Student', 'UPDATE', 'ID: 1, Full Name: Charlie Brown, Course: 2', '2025-04-17 18:27:34'),
(2, 'Student', 'UPDATE', 'ID: 2, Full Name: Diana Evans, Course: 1', '2025-04-17 18:27:34'),
(3, 'Student', 'UPDATE', 'ID: 3, Full Name: Edward Young, Course: 3', '2025-04-17 18:27:34'),
(4, 'Student', 'UPDATE', 'ID: 4, Full Name: Fiona White, Course: 2', '2025-04-17 18:27:34'),
(5, 'Student', 'UPDATE', 'ID: 5, Full Name: George Black, Course: 4', '2025-04-17 18:27:34'),
(6, 'Student', 'UPDATE', 'ID: 6, Full Name: Hannah Adams, Course: 1', '2025-04-17 18:27:34'),
(7, 'Student', 'INSERT', 'ID: 7, Full Name: John Doe, Course: 2', '2025-04-17 18:32:40'),
(8, 'Student', 'INSERT', 'ID: 8, Full Name: John Doe, Course: 2', '2025-04-17 18:32:58'),
(9, 'Student', 'DELETE', 'ID: 8, Full Name: John Doe, Course: 2', '2025-04-21 16:29:47'),
(10, 'Student', 'DELETE', 'ID: 7, Full Name: John Doe, Course: 2', '2025-04-21 16:30:40'),
(11, 'Student', 'INSERT', 'ID: 9, Full Name: Vlad Korko, Course: 3', '2025-04-21 16:31:34'),
(12, 'Student', 'INSERT', 'ID: 10, Full Name: sdadas, Course: 2', '2025-04-21 16:32:03'),
(13, 'Student', 'UPDATE', 'ID: 1, Full Name: Charlie Brown, Course: 2', '2025-04-21 16:58:47'),
(14, 'Student', 'UPDATE', 'ID: 3, Full Name: Edward Youngaaaaa, Course: 3', '2025-04-22 23:13:11'),
(15, 'Student', 'INSERT', 'ID: 11, Full Name: test, Course: 1', '2025-04-22 23:15:49'),
(16, 'Student', 'DELETE', 'ID: 9, Full Name: Vlad Korko, Course: 3', '2025-04-22 23:16:01'),
(17, 'Student', 'DELETE', 'ID: 11, Full Name: test, Course: 1', '2025-04-22 23:16:07'),
(18, 'Student', 'DELETE', 'ID: 10, Full Name: sdadas, Course: 2', '2025-04-22 23:16:08'),
(19, 'Journal', 'DELETE', 'Discipline ID: 1, Student ID: 1, Teacher ID: 1, Mark: 85', '2025-04-22 23:22:43'),
(20, 'Journal', 'DELETE', 'Discipline ID: 2, Student ID: 2, Teacher ID: 2, Mark: 90', '2025-04-22 23:22:53'),
(21, 'Journal', 'DELETE', 'Discipline ID: 1, Student ID: 3, Teacher ID: 1, Mark: 75', '2025-04-22 23:22:53'),
(22, 'Journal', 'DELETE', 'Discipline ID: 3, Student ID: 4, Teacher ID: 3, Mark: 88', '2025-04-22 23:22:53'),
(23, 'Journal', 'DELETE', 'Discipline ID: 4, Student ID: 5, Teacher ID: 4, Mark: 92', '2025-04-22 23:22:53'),
(24, 'Journal', 'DELETE', 'Discipline ID: 2, Student ID: 6, Teacher ID: 2, Mark: 77', '2025-04-22 23:22:53'),
(25, 'Journal', 'DELETE', 'Discipline ID: 1, Student ID: 1, Teacher ID: 4, Mark: 95', '2025-04-22 23:22:53'),
(26, 'Journal', 'DELETE', 'Discipline ID: 4, Student ID: 3, Teacher ID: 4, Mark: 80', '2025-04-22 23:22:53'),
(27, 'Journal', 'DELETE', 'Discipline ID: 3, Student ID: 5, Teacher ID: 3, Mark: 70', '2025-04-22 23:22:53'),
(28, 'Journal', 'DELETE', 'Discipline ID: 2, Student ID: 6, Teacher ID: 2, Mark: 85', '2025-04-22 23:22:53'),
(29, 'Student', 'DELETE', 'ID: 1, Full Name: Charlie Brown, Course: 2', '2025-04-22 23:22:58'),
(30, 'Student', 'DELETE', 'ID: 2, Full Name: Diana Evans, Course: 1', '2025-04-22 23:22:59'),
(31, 'Student', 'DELETE', 'ID: 3, Full Name: Edward Youngaaaaa, Course: 3', '2025-04-22 23:22:59'),
(32, 'Student', 'INSERT', 'ID: 12, Full Name: test1, Course: 2', '2025-04-22 23:23:34'),
(33, 'Student', 'UPDATE', 'ID: 12, Full Name: test12, Course: 55', '2025-04-22 23:23:44');

-- --------------------------------------------------------

--
-- Структура таблицы `department`
--

CREATE TABLE `department` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `room_number` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `department`
--

INSERT INTO `department` (`id`, `name`, `room_number`) VALUES
(1, 'Computer Science', '101'),
(2, 'Mathematics', '202'),
(3, 'Physics', '303');

--
-- Триггеры `department`
--
DELIMITER $$
CREATE TRIGGER `log_delete_department` AFTER DELETE ON `department` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Department', 'DELETE', CONCAT('ID: ', OLD.id, ', Name: ', OLD.name, ', Room Number: ', OLD.room_number));
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_insert_department` AFTER INSERT ON `department` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Department', 'INSERT', CONCAT('ID: ', NEW.id, ', Name: ', NEW.name, ', Room Number: ', NEW.room_number));
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_update_department` AFTER UPDATE ON `department` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Department', 'UPDATE', CONCAT('ID: ', NEW.id, ', Name: ', NEW.name, ', Room Number: ', NEW.room_number));
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `discipline`
--

CREATE TABLE `discipline` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `discipline`
--

INSERT INTO `discipline` (`id`, `name`) VALUES
(1, 'Databases'),
(2, 'Linear Algebra'),
(3, 'Mechanics'),
(4, 'Algorithms');

--
-- Триггеры `discipline`
--
DELIMITER $$
CREATE TRIGGER `log_delete_discipline` AFTER DELETE ON `discipline` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Discipline', 'DELETE', CONCAT('ID: ', OLD.id, ', Name: ', OLD.name));
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_insert_discipline` AFTER INSERT ON `discipline` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Discipline', 'INSERT', CONCAT('ID: ', NEW.id, ', Name: ', NEW.name));
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_update_discipline` AFTER UPDATE ON `discipline` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Discipline', 'UPDATE', CONCAT('ID: ', NEW.id, ', Name: ', NEW.name));
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `journal`
--

CREATE TABLE `journal` (
  `id` int(11) NOT NULL,
  `discipline_id` int(11) DEFAULT NULL,
  `mark` int(11) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `teacher_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Триггеры `journal`
--
DELIMITER $$
CREATE TRIGGER `log_delete_journal` AFTER DELETE ON `journal` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Journal', 'DELETE', CONCAT('Discipline ID: ', OLD.discipline_id, ', Student ID: ', OLD.student_id, ', Teacher ID: ', OLD.teacher_id, ', Mark: ', OLD.mark));
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_insert_journal` AFTER INSERT ON `journal` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Journal', 'INSERT', CONCAT('Discipline ID: ', NEW.discipline_id, ', Student ID: ', NEW.student_id, ', Teacher ID: ', NEW.teacher_id, ', Mark: ', NEW.mark));
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_update_journal` AFTER UPDATE ON `journal` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Journal', 'UPDATE', CONCAT('Discipline ID: ', NEW.discipline_id, ', Student ID: ', NEW.student_id, ', Teacher ID: ', NEW.teacher_id, ', Mark: ', NEW.mark));
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `course` int(11) DEFAULT NULL,
  `discipline_id` int(11) DEFAULT NULL,
  `phone` varbinary(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `student`
--

INSERT INTO `student` (`id`, `full_name`, `course`, `discipline_id`, `phone`) VALUES
(4, 'Fiona White', 2, 3, 0x6feed5704a31009aa40d02badf334f48),
(5, 'George Black', 4, 4, 0xd8ce1809ca95525a1e511d35021ed454),
(6, 'Hannah Adams', 1, 2, 0x7ffe03bb231a792de656fcb79bf1245e),
(12, 'test12', 55, 2, 0xfad6b5c8b1765c1cde7d52953b29cb9b);

--
-- Триггеры `student`
--
DELIMITER $$
CREATE TRIGGER `check_student_course` BEFORE INSERT ON `student` FOR EACH ROW BEGIN
    -- Проверка, чтобы курс был от 1 до 4
    IF NEW.course < 1 OR NEW.course > 4 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Course must be between 1 and 4';
    END IF;
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_delete_student` AFTER DELETE ON `student` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Student', 'DELETE', CONCAT('ID: ', OLD.id, ', Full Name: ', OLD.full_name, ', Course: ', OLD.course));
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_insert_student` AFTER INSERT ON `student` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Student', 'INSERT', CONCAT('ID: ', NEW.id, ', Full Name: ', NEW.full_name, ', Course: ', NEW.course));
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_update_student` AFTER UPDATE ON `student` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Student', 'UPDATE', CONCAT('ID: ', NEW.id, ', Full Name: ', NEW.full_name, ', Course: ', NEW.course));
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `teacher`
--

CREATE TABLE `teacher` (
  `id` int(11) NOT NULL,
  `full_name` varchar(255) NOT NULL,
  `birth_date` date DEFAULT NULL,
  `department_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `teacher`
--

INSERT INTO `teacher` (`id`, `full_name`, `birth_date`, `department_id`) VALUES
(1, 'Alice Johnson', '1980-05-12', 1),
(2, 'Bob Smith', '1975-09-23', 2),
(3, 'Catherine Green', '1985-03-15', 3),
(4, 'David Brown', '1990-11-30', 1);

--
-- Триггеры `teacher`
--
DELIMITER $$
CREATE TRIGGER `log_delete_teacher` AFTER DELETE ON `teacher` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Teacher', 'DELETE', CONCAT('ID: ', OLD.id, ', Full Name: ', OLD.full_name, ', Department ID: ', OLD.department_id));
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_insert_teacher` AFTER INSERT ON `teacher` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Teacher', 'INSERT', CONCAT('ID: ', NEW.id, ', Full Name: ', NEW.full_name, ', Department ID: ', NEW.department_id));
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `log_update_teacher` AFTER UPDATE ON `teacher` FOR EACH ROW BEGIN
    INSERT INTO ChangeLog (TableName, Action, ChangedData) 
    VALUES ('Teacher', 'UPDATE', CONCAT('ID: ', NEW.id, ', Full Name: ', NEW.full_name, ', Department ID: ', NEW.department_id));
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `login` varchar(255) NOT NULL,
  `password` varbinary(255) NOT NULL,
  `role` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `login`, `password`, `role`) VALUES
(1, '1', 0xfcb47c931c123f8781a4d4fae92ffd19, 'teacher'),
(2, '2', 0xb3800b3a3cb4ece2051a3e80fe373eac, 'teacher'),
(3, 'u', 0xfcb47c931c123f8781a4d4fae92ffd19, 'student');

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `changelog`
--
ALTER TABLE `changelog`
  ADD PRIMARY KEY (`ID`);

--
-- Индексы таблицы `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `discipline`
--
ALTER TABLE `discipline`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `journal`
--
ALTER TABLE `journal`
  ADD PRIMARY KEY (`id`),
  ADD KEY `discipline_id` (`discipline_id`),
  ADD KEY `student_id` (`student_id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- Индексы таблицы `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`),
  ADD KEY `discipline_id` (`discipline_id`);

--
-- Индексы таблицы `teacher`
--
ALTER TABLE `teacher`
  ADD PRIMARY KEY (`id`),
  ADD KEY `department_id` (`department_id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `login` (`login`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `changelog`
--
ALTER TABLE `changelog`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT для таблицы `department`
--
ALTER TABLE `department`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `discipline`
--
ALTER TABLE `discipline`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `journal`
--
ALTER TABLE `journal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT для таблицы `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT для таблицы `teacher`
--
ALTER TABLE `teacher`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `journal`
--
ALTER TABLE `journal`
  ADD CONSTRAINT `journal_ibfk_1` FOREIGN KEY (`discipline_id`) REFERENCES `discipline` (`id`),
  ADD CONSTRAINT `journal_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`),
  ADD CONSTRAINT `journal_ibfk_3` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`);

--
-- Ограничения внешнего ключа таблицы `student`
--
ALTER TABLE `student`
  ADD CONSTRAINT `student_ibfk_1` FOREIGN KEY (`discipline_id`) REFERENCES `discipline` (`id`);

--
-- Ограничения внешнего ключа таблицы `teacher`
--
ALTER TABLE `teacher`
  ADD CONSTRAINT `teacher_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `department` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
