# Write your MySQL query statement below
SELECT FirstName, LastName, City, State
FROM Person Left Outer Join Address ON Person.PersonId = Address.PersonId
