Select * from players
WHERE Player_ID 
NOT IN
(select distinct Player_ID from gamelogs)