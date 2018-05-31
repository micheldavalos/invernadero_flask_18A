CREATE TABLE dueno(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    apellido VARCHAR(50) NOT NULL
);

CREATE TABLE invernadero(
    id INT PRIMARY KEY AUTO_INCREMENT,
    ubicacion VARCHAR(50) NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    id_dueno INT NOT NULL,
    FOREIGN KEY (id_dueno)
    REFERENCES dueno(id)
);

CREATE TABLE planta(
    id INT PRIMARY KEY AUTO_INCREMENT,
    cultivo VARCHAR(30) NOT NULL,
    fecha DATE NOT NULL,
    id_invernadero INT NOT NULL,
    FOREIGN KEY (id_invernadero)
    REFERENCES invernadero(id)
);

CREATE TABLE registro(
    id INT PRIMARY KEY AUTO_INCREMENT,
    fecha DATE NOT NULL,
    co2 FLOAT,
    humedad FLOAT,
    luz FLOAT,
    ph FLOAT,
    id_planta INT NOT NULL,
    FOREIGN KEY (id_planta)
    REFERENCES planta(id)
);

CREATE TABLE tipo(
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(15) NOT NULL
);

CREATE TABLE usuario(
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(15) NOT NULL,
    id_tipo INT NOT NULL,
    FOREIGN KEY (id_tipo)
    REFERENCES tipo(id)
);

CREATE TABLE usuario_invernadero(
    id_usuario INT NOT NULL,
    id_invernadero INT NOT NULL,
    FOREIGN KEY (id_usuario)
    REFERENCES usuario(id),
    FOREIGN KEY (id_invernadero)
    REFERENCES invernadero(id)
);



