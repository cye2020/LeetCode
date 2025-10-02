SELECT
    ID
FROM
    WEATHER AS w1
WHERE 1 = 1
    AND TEMPERATURE > (
        SELECT
            w2.TEMPERATURE
        FROM
            WEATHER AS w2
        WHERE 1 = 1
            AND w2.RECORDDATE = w1.RECORDDATE - INTERVAL 1 DAY
    )
;