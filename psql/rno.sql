-- 1 task
SELECT ocurance FROM wordform LIMIT 10;

-- 2 task
select plaintext from wordform where plaintext like 'a%';

-- 3 task
select title, genretype from work where genretype = 'p';

-- 4 task
select avg(totalparagraphs) as avg from work where genretype = 't';
