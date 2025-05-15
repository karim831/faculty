select * from SalesLT.Product p;

-- 1-Write a query to filter records of certain column in a table according to certain confition
select * from SalesLT.Product p  where p.Color = 'Black';


-- 2-Write a query to calculate the average value of a numeric column
select avg(p.ListPrice) from SalesLT.Product p;

-- 3-Write a query to find the maximum value in a numeric column
select max(p.ListPrice)from SalesLT.Product p;

--4-Write a query to find rows where a text column starts with a specific letter.
select * from SalesLT.Product p where p.Color like 'M%';

-- 5-Write a query to select all rows ordered by a column in descending order
select * from SalesLT.Product p order by p.ProductId desc;

-- 6-Write a query to rename a column in the result set using an alias
select p.ProductID  as 'Id' from SalesLT.Product p;

-- 7-Write a query to count rows grouped by a column and show only groups that have more than 2 rows
select p.Color, Count(*) from SalesLT.Product p group by p.Color having count(*) > 2;

 --8-Write a query to find the average of a column for each group.
select p.Color , avg(p.ListPrice) from SalesLT.Product p group by p.Color

-- 9-Write a query to count how many rows exist for each value in a column.
select p.Color, Count(*) from SalesLT.Product p group by p.Color

-- 10- Write a query to join two tables on a common column and select all columns.
select * from SalesLT.Product p inner join SalesLT.ProductCategory pc on p.ProductCategoryID = pc.ProductCategoryID;

-- 11-write a query to select all customers, and any orders they might have
select (c.FirstName + c.LastName) as 'CustomerFullName', soh.SalesOrderID  from SalesLT.SalesOrderHeader soh inner join SalesLT.Customer c on c.CustomerID = soh.CustomerID ;



