-- The Perfect Arrangement
-- Write a query to print the id, first_name and last_name. 
-- To filter the names, concatenate the first and last names to create a combined name. 
-- Return the names of customers whose combined names are less than 12 letters long. 
-- Sort the results by their combined name lengths, then alphabetically, case insensitive, by combined name, then by id. All sorts are ascending.

-- Input Format
-- CUSTOMER
-- Name          Type    Description
-- ID            Integer unique id, primary key.
-- FIRST_NAME    String  
-- LAST_NAME     String  
-- COUNTRY       String  
-- CREDIT_LIMIT  Float  

-- Output Format
-- CUSTOMER.ID CUSTOMER.FIRST_NAME CUSTOMER.LAST_NAME


-- Explanation
-- AlexWhite is 9 letters long, so it is included in the results. JordanFernandez is 15 letters long, so it is excluded from the results. The last 3 names are the same length, so they are sorted alphabetically by name.

-- MorganThomas 12
-- PeytonHarris 12
-- EllisGutierrez 14
-- JordanFernandez 15
-- SpencerJohnston 15

SELECT ID, FIRST_NAME, LAST_NAME
FROM CUSTOMER
WHERE LENGTH(FIRST_NAME) + LENGTH(LAST_NAME) < 12
ORDER BY LENGTH(FIRST_NAME) + LENGTH(LAST_NAME), CONCAT(FIRST_NAME, LAST_NAME), ID;

