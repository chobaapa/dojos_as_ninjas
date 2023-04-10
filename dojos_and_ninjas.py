
USE dojos_and_ninjas;

INSERT INTO dojos(name)
VALUES ("Chicago"), ("Seattle"), ("Online");

SET SQL_SAFE_UPDATES = 0;
DELETE FROM dojos;

INSERT INTO ninjas (first_name, Last_name, age, dojo_id)
VALUES( "JEFF", "STONE", 23, 1), ("CHRIS", "CLETUS", 35, 1), ("FEMI", "OLA", 40,1);

INSERT INTO ninjas (first_name, Last_name, age, dojo_id)
VALUES( "PRISCA", "WAUVER", 33, 2), ("CHRISTOPHER", "DAN", 65, 2), ("FEMU", "ODLA", 20,2);

INSERT INTO ninjas (first_name, Last_name, age, dojo_id)
VALUES( "HAWA", "DIAW", 23, 3), ("KESSO", "NELSON", 25, 3), ("GODWIN", "TUTU", 18,3);

SELECT* FROM dojos
LEFT JOIN ninjas_id ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 4;

SELECT* FROM dojos
LEFT JOIN ninjas_id ON dojos.id = ninjas.dojo_id
WHERE dojos.id = 6;


SELECT*FROM dojos
where dojos.id = (SELECT dojo_id FROM ninjas ORDER BY dojo_id DESC LIMIT 1);