/*
Enter your query below.
Please append a semicolon ";" at the end of the query

There is a table with daily weather data over the last 6 months of 2020, including the maximum, minimum, and average temperatures.
Write a query that gives month, monthly maximum, monthly minimum, and monthly average temperatures for the six months.

Note: Round the average to the nearest integer.

NAME OF THE TABLE: temperature_records
COLUMNS: record_date, data_type, data_value
Types: record_date (varchar(10)), data_type (varchar(3)), data_value (int)
Description: record_date is data of the record, data_type is the type of data (max, min, avg), and data_value is the value of the data.

record_date is in the format 'YYYY-MM-DD'.

output columns: month, max, min, avg
Example: 7 100 67 79
*/

SELECT 
    MONTH(record_date) AS month,
    MAX(CASE WHEN data_type = 'max' THEN data_value END) AS max,
    MIN(CASE WHEN data_type = 'min' THEN data_value END) AS min,
    ROUND(AVG(CASE WHEN data_type = 'avg' THEN data_value END)) AS avg
FROM temperature_records
GROUP BY month;