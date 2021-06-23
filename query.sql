select h.hacker_id, h.name
from submissions as s
join hackers as h
on s.hacker_id = h.hacker_id
join challenges as c
on s.challenge_id = c.challenge_id
join difficulty as d
on c.difficulty_level = d.difficulty_level
where s.score = d.score
group by h.hacker_id, h.name
having count(*) > 1
order by count(*) desc, h.hacker_id


-- we start by selecting the hacker_id and name then join the four tables to gether
-- on line 9 we filter the submissions to find the hacker who got full scores
-- on line 10 to 12 we group the submissions with full score by name and hacker id so that we can output them 
