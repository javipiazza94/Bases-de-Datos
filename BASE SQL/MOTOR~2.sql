

--CREATE SEQUENCE SEQ_TRABAJADOR;
--CREATE SEQUENCE SEQ_COLABORACION;
--CREATE SEQUENCE SEQ_COMPOSICION;
--CREATE SEQUENCE SEQ_PIEZA;
--CREATE SEQUENCE SEQ_ENCARGO;
--CREATE SEQUENCE SEQ_SECCION;
--CREATE SEQUENCE SEQ_FAENA;
--CREATE SEQUENCE SEQ_MOTOR;


INSERT INTO SECCION (id_seccion, nombre)VALUES(SEQ_SECCION.nextval, 'AERODINAMICA');
INSERT INTO MOTOR (id_motor, codigo, potencia)VALUES(SEQ_MOTOR.nextval, 'U738H', 120);
INSERT INTO PIEZA (id_pieza, descripcion, precio)VALUES(2334, 'bujia', 145);
INSERT INTO TRABAJADOR (id_trabajador, nombre, apellido_a, apellido_b, dni, alta, id_seccion)VALUES(SEQ_TRABAJADOR.nextval, 'PEPE', 'GARCIA', 'DOMINGUEZ', 77835283, '23/6/2014', 78434);
INSERT INTO TRABAJADOR (id_trabajador, nombre, apellido_a, apellido_b, dni, alta, id_seccion)VALUES(SEQ_TRABAJADOR.nextval, 'RODOLFO', 'LANGOSTINO', 'MORENO', 45835283, '23/8/2017', 78434);
INSERT INTO TRABAJADOR (id_trabajador, nombre, apellido_a, apellido_b, dni, alta, id_seccion)VALUES(SEQ_TRABAJADOR.nextval, 'DOMIN', 'CALBO', 'BRAZZERS', 93465837, '25/2/2019', 78434);
INSERT INTO ENCARGO (id_encargo, tarea, entrega, id_motor)VALUES(SEQ_ENCARGO.nextval, '12/12/2020', '12/12/2022', 97868);
INSERT INTO FAENA (id_faena, horas, id_trabajador, id_encargo)VALUES(SEQ_FAENA.nextval, 234, 45835283, 78348894);
INSERT INTO COLABORACION (id_colaboracion, maximo, id_motor, id_seccion)VALUES(SEQ_COLABORACION.nextval, 123, SEQ_MOTOR.nextval, SEQ_SECCION.nextval);






 