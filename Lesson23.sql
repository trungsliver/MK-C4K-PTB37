-- Khởi tạo database 
CREATE DATABASE school_management_db;

-- Xóa database
DROP DATABASE school_management_db;

-- Dùng db để làm việc 
USE school_management_db;

-- Tạo bảng lớp học
CREATE TABLE classes (
	class_id INT auto_increment PRIMARY KEY,
    class_name VARCHAR(50) NOT NULL
); 

-- Tạo bảng giáo viên
CREATE TABLE teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    teacher_name VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    phone VARCHAR(20)
);

-- Tạo bảng học sinh
CREATE TABLE students (
	student_id INT AUTO_INCREMENT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    dob DATE,
    gender VARCHAR(10),
    email VARCHAR(100),
    phone VARCHAR(20),
    class_id INT,
    
    FOREIGN KEY (class_id) REFERENCES classes(class_id)
);
 
 -- Tạo bảng subjects
 CREATE TABLE subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    subject_name VARCHAR(100) NOT NULL
);

-- Tạo bảng điểm
CREATE TABLE scores (
    score_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT NOT NULL,
    subject_id INT NOT NULL,
    score DECIMAL(4,2),

    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);

-- ================================ THÊM DỮ LIỆU CHO BẢNG =======================================
INSERT INTO classes (class_name)
VALUES ('9B1'), ('9B2'), ('9B3'), ('9B4'), ('9B5');

SELECT * FROM classes;
-- -----------------------------------------------------
INSERT INTO teachers (teacher_name, email, phone)
VALUES
    ('Nguyễn Văn An', 'an@gmail.com', '0901234567'),
    ('Trần Thị Bình', 'binh@gmail.com', '0902345678'),
    ('Lê Văn Nam', 'nam@gmail.com', '0903456789');
    
-- ---------------------------------------------------
INSERT INTO students
    (student_name, date_of_birth, gender, email, phone, class_id)
VALUES
    ('Nguyễn Minh Anh', '2010-05-12', 'Nữ','minhanh@gmail.com', '0901111111', 1),
    ('Trần Văn Bình', '2010-08-20', 'Nam','binh@gmail.com', '0902222222', 1),
    ('Lê Hoàng Nam', '2009-03-15', 'Nam','nam@gmail.com', '0903333333', 2),
    ('Phạm Thu Hà', '2009-11-02', 'Nữ','ha@gmail.com', '0904444444', 2),
    ('Đỗ Minh Đức', '2008-07-25', 'Nam','duc@gmail.com', '0905555555', 3);
-- ---------------------------------------------------
INSERT INTO subjects (subject_name)
VALUES
('Toán'),
('Ngữ Văn'),
('Tiếng Anh'),
('Tin học'),
('Vật lý');
-- --------------------------------------------------
INSERT INTO scores
    (student_id, subject_id, score)
VALUES
    (1, 1, 8.5),
    (1, 2, 7.5),
    (1, 3, 9.0),

    (2, 1, 7.0),
    (2, 2, 8.0),
    (2, 3, 8.5),

    (3, 1, 9.0),
    (3, 2, 8.5),
    (3, 4, 9.5),

    (4, 1, 6.5),
    (4, 2, 7.0),

    (5, 1, 8.0),
    (5, 4, 9.0);
