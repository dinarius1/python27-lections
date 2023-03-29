-- 1 task
SELECT ocurance FROM wordform LIMIT 10;

-- 2 task
select plaintext from wordform where plaintext like 'a%';

-- 3 task
select title, genretype from work where genretype = 'p';
