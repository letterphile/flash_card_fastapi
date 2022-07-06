from platform import node


def recall_from_any_node_query (node_query):
    query = (f"SELECT\
`mybrain\`.`m`.`know_id` AS `id`,\
    MAX(`mybrain`.`m`.`question`) AS `front`,\
    MAX(`mybrain`.`m`.`answer`) AS `back`,\
    SUM(\
        IF((`r`.`recall_verdict` = 1),\
        1,\
        0)\
    ) AS `score`,\
    (\
        SUM(\
            IF((`r`.`recall_verdict` = 1),\
            1,\
            0)\
        ) / COUNT(0)\
    ) AS `success_ratio`\
FROM\
    (\
        (\
        WITH\
            recursive `category_path`(\
                `know_id`,\
                `question`,\
                `answer`,\
                `parent_id`,\
                `lvl`\
            ) AS(\
            SELECT\
                `mybrain`.`knowledge`.`know_id` AS `know_id`,\
                `mybrain`.`knowledge`.`question` AS `question`,\
                `mybrain`.`knowledge`.`answer` AS `answer`,\
                `mybrain`.`knowledge`.`parent_id` AS `parent_id`,\
                0 AS `lvl`\
            FROM\
                `mybrain`.`knowledge`\
            WHERE\
                (\
                    `mybrain`.`knowledge`.`parent_id` {node_query}\
                )\
            UNION ALL\
        SELECT\
            `c`.`know_id` AS `know_id`,\
            `c`.`question` AS `question`,\
            `c`.`answer` AS `answer`,\
            `c`.`parent_id` AS `parent_id`,\
            (`cp`.`lvl` + 1) AS `cp.lvl + 1`\
        FROM\
            (\
                `category_path` `cp`\
            JOIN `mybrain`.`knowledge` `c`\
            ON\
                ((`cp`.`know_id` = `c`.`parent_id`))\
            )\
        )\
    SELECT\
        `category_path`.`know_id` AS `know_id`,\
        `category_path`.`question` AS `question`,\
        `category_path`.`answer` AS `answer`,\
        `category_path`.`parent_id` AS `parent_id`,\
        `category_path`.`lvl` AS `lvl`\
    FROM\
        `category_path`\
    ORDER BY\
        `category_path`.`lvl`\
    ) `m`\
LEFT JOIN `mybrain`.`recall` `r`\
ON\
    (\
        (\
            `r`.`memory_id` = `mybrain`.`m`.`know_id`\
        )\
    )\
    )\
WHERE\
    (`mybrain`.`m`.`answer` IS NOT NULL)\
GROUP BY\
    `mybrain`.`m`.`know_id`\
ORDER BY\
    `score`,\
    `success_ratio`")

    return query