create database taskmanagementsystem;
use taskmanagementsystem;
select * from tasks;
CREATE TABLE tasks(TASKID INT PRIMARY KEY, TASK_NAME VARCHAR(200), TASK_DESCRIPTION VARCHAR(500), TASK_DUEDATE date, TASK_STATUS VARCHAR(50));
