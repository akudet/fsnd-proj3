-- view stat of a path
-- only successful views (status is 200) and using GET are counted
create view view_stat as
select path, count(*) as view_cnt
from log
where status = '200 OK' and method = 'GET'
group by path
