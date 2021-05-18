


SET LANGUAGE ENGLISH


CREATE DATABASE SQL_Types;


USE SQL_Types;





CREATE TABLE Employees
    (Employee_ID INT NOT NULL PRIMARY KEY,
	 Job_Titel VARCHAR(100),
	 Name VARCHAR(100) NOT NULL,
     Age INT NOT NULL)
    ;


INSERT INTO Employees VALUES (1, 'Consultant', 'Klara', 35)
INSERT INTO Employees VALUES (2, 'Consultant', 'Emily', 44)
INSERT INTO Employees VALUES (3, 'Consultant', 'Jessy', 22)
INSERT INTO Employees VALUES (4, 'Consultant', 'Max', 50)
INSERT INTO Employees VALUES (5, 'Consultant', 'Tom', 18)


SELECT * FROM Employees;



UPDATE Employees
    SET Job_Titel = 'Senior Consultant'
    ;

SELECT * FROM Employees;



-- Neu Aufsetzen der Tabelle ....


SELECT * FROM Employees;



BEGIN TRANSACTION Change_Title  
	UPDATE Employees
		SET Job_Titel = 'Senior Consultant'
ROLLBACK TRANSACTION Change_Title  
;





BEGIN TRANSACTION Change_Title  
	UPDATE Employees
		SET Job_Titel = 'Senior Consultant'
		WHERE Age > 40
ROLLBACK TRANSACTION Change_Title  
;


SELECT * FROM Employees;




BEGIN TRANSACTION Change_Title  
	UPDATE Employees
		SET Job_Titel = 'Senior Consultant'
		WHERE Age > 40
COMMIT TRANSACTION Change_Title 
;


SELECT * FROM Employees;








BEGIN TRANSACTION Change_Title_2 

  BEGIN TRY

	UPDATE Employees
		SET Job_Titel = 'Junior Consultant'
		WHERE Age < 25

  END TRY

  BEGIN CATCH

      ROLLBACK TRANSACTION Change_Title_2

  END CATCH  
  ;



SELECT * FROM Employees;



ROLLBACK TRANSACTION Change_Title_2;



SELECT * FROM Employees;




BEGIN TRANSACTION Change_Title_2 

  BEGIN TRY

	UPDATE Employees
		SET Job_Titel = 'Junior Consultant'
		WHERE Age < 25

  END TRY

  BEGIN CATCH

      ROLLBACK TRANSACTION Change_Title_2

  END CATCH  
  ;



SELECT * FROM Employees;


COMMIT TRANSACTION Change_Title_2;


SELECT * FROM Employees;


ROLLBACK TRANSACTION Change_Title_2;






