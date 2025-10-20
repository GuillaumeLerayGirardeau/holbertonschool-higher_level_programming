-- This script lists all record in the table "second_table" with the same score in a MySQL server

SELECT score, COUNT(*) AS "number"
FROM second_table
GROUP BY score
ORDER BY score DESC;
