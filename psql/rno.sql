-- 1 task
SELECT ocurance FROM wordform LIMIT 10;

-- 2 task
select plaintext from wordform where plaintext like 'a%';

-- 3 task
select title, genretype from work where genretype = 'p';

-- 4 task
select avg(totalparagraphs) as avg from work where genretype = 't';

-- 5 task
select avg(totalwords) as avg from work;
select title from work where totalwords > 20563;

-- 9 task
select charname, speechcount from character where speechcount >= 15 and speechcount <= 30;

-- 10 task
select title, year from work where year >= 1601 and year <= 1701;

-- 11 task
select longtitle from work where longtitle like '%the%';