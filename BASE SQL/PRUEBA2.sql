
Error que empieza en la línea: 49 del comando :
CREATE TABLA  COMPOSICION (ID_COMPOSICION NUMBER (9)
                          ,CANTIDAD NUMBER (9)
                          ,ID_MOTOR NUMBER (9)
                          ,ID_PIEZA NUMBER (9)
                          ,CONSTRAINT PK_COMPOSICION PRIMARY KEY (ID_COMPOSICION)
                          ,CONSTRAINT FK_MOTOR FOREIGN KEY (ID_MOTOR) REFERENCES MOTOR(ID_MOTOR)
                          ,CONSTRAINT FK_PIEZA FOREIGN KEY (ID_PIEZA) REFERENCES PIEZA(ID_PIEZA)
Informe de error -
ORA-00901: comando CREATE no válido
00901. 00000 -  "invalid CREATE command"
*Cause:    
*Action:

Error que empieza en la línea: 49 del comando :
CREATE TABLE COMPOSICION (ID_COMPOSICION NUMBER (9)
                          ,CANTIDAD NUMBER (9)
                          ,ID_MOTOR NUMBER (9)
                          ,ID_PIEZA NUMBER (9)
                          ,CONSTRAINT PK_COMPOSICION PRIMARY KEY (ID_COMPOSICION)
                          ,CONSTRAINT FK_MOTOR FOREIGN KEY (ID_MOTOR) REFERENCES MOTOR(ID_MOTOR)
                          ,CONSTRAINT FK_PIEZA FOREIGN KEY (ID_PIEZA) REFERENCES PIEZA(ID_PIEZA)
Informe de error -
ORA-00907: falta el paréntesis derecho
00907. 00000 -  "missing right parenthesis"
*Cause:    
*Action:

Error que empieza en la línea: 49 del comando :
CREATE TABLE COMPOSICION (ID_COMPOSICION NUMBER (9)
                          ,CANTIDAD NUMBER (9)
                          ,ID_MOTOR NUMBER (9)
                          ,ID_PIEZA NUMBER (9)
                          ,CONSTRAINT PK_COMPOSICION PRIMARY KEY (ID_COMPOSICION)
                          ,CONSTRAINT FK_MOTOR FOREIGN KEY (ID_MOTOR) REFERENCES MOTOR(ID_MOTOR)
                          ,CONSTRAINT FK_PIEZA FOREIGN KEY (ID_PIEZA) REFERENCES PIEZA(ID_PIEZA))
Informe de error -
ORA-00942: la tabla o vista no existe
00942. 00000 -  "table or view does not exist"
*Cause:    
*Action:

Error que empieza en la línea: 49 del comando :
CREATE TABLE COMPOSICION (ID_COMPOSICION NUMBER (9)
                          ,CANTIDAD NUMBER (9)
                          ,ID_MOTOR NUMBER (9)
                          ,ID_PIEZA NUMBER (9)
                          ,CONSTRAINT PK_COMPOSICION PRIMARY KEY (ID_COMPOSICION)
                          ,CONSTRAINT FK_MOTOR FOREIGN KEY (ID_MOTOR) REFERENCES MOTOR(ID_MOTOR)
                          ,CONSTRAINT FK_PIEZA FOREIGN KEY (ID_PIEZA) REFERENCES PIEZA(ID_PIEZA))
Informe de error -
ORA-00942: la tabla o vista no existe
00942. 00000 -  "table or view does not exist"
*Cause:    
*Action:
