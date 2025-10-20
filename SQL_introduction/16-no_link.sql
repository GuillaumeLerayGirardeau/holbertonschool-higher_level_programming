-- This script lists all record in the table "second_table" in a MySQL server

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;