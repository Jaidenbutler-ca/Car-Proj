DECLARE @make AS VARCHAR(100)='%'
DECLARE @model AS VARCHAR(100)='%'
DECLARE @year AS varchar(4)='2024'
Select * from info
where make like @make and name like @model and year like @year