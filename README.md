<a id='top'></a>

# Tasks
___

## task 1
[task link](https://github.com/mnv/python-basics)

```
run code: python3 postman_way.py
```
___

## task 2

Develop a game of Reverse Tic-Tac-Toe on a 10 x 10 board with the Five in a Row rule - whoever loses
who got a vertical, horizontal or diagonal row of five of their figures (tic-tac-toe).
The game should work in the "human versus computer" mode.

The game can be console

When developing a game, take into account the principle of DRY (don’t repeat yourself) - “do not repeat yourself”.
That is, to minimize code repetition and increase its reusability through the use of functions.
Functions should have their own area of responsibility.

```
run code: python3 tic-tac-toe.py
```
___

## task 3

Using OOP to design and implement a geometric calculator

for calculations performed on figures. The calculator must support calculations for flat and three-dimensional figures.

Flat figures: circle, square, rectangle, triangle, trapezium, rhombus.
Volumetric figures: sphere, cube, parallelepiped, pyramid, cylinder, cone.

Implement at least one general calculation method for all shapes and at least one specific to certain shapes. For example, area is a general method for all figures, median is a specific method for a number of figures.

It is necessary: ​​to implement a graphical interface for the possibility of user interaction with the program and visualization of figures (taking into account the entered figure parameters).

When implementing, use all kinds of methods: static, class and instance method. 

```
run code: python3 main.py
```
___

## task 4

In the control panel (/admin), the user should be able to enter:
1. list of ingredients for the recipe;
2. add text and recipe name.

In the public part of the site, the user should be able to view the entered recipes with the output of ingredients with the ability to filter by ingredients and recipe name. Keep in mind that one ingredient can be found in several recipes.

You can use the standard Bootstrap templates to design your website.

It is necessary to develop a database schema, describing the appropriate models for the tables. Thus, the database schema must be converted to third normal form (3NF).

When you first start the project, the database should be filled with data due to migration and adding fixtures.

The project must be packaged in Docker (have a Dockerfile and docker-compose.yml).
It is necessary to publish the project on GitHub and issue a Readme.md with a description and instructions for launching.

To develop a project use:
1) PostgreSQL 14 DBMS
2) Django 3.2.8 framework

The DBMS and the web application must run in separate Docker containers.


### How to use

Create an .env file at the root of the repository:
```
cp .env.dist .env
```
Make adjustments to the environment variables as needed.

At the root of the repository, run the command:
```
docker-compose up -d db
```
Make migrations:
```
docker-compose run app python manage.py migrate
```
load data base:
```
docker-compose run app python manage.py loaddata db.json
```
Create super user:
```
docker-compose run app python manage.py createsuperuser
```
Raise container for application:
```
docker-compose up -d app
```
You can stop the database and application containers with the command:
```
docker-compose stop
```
You can stop and remove database and application containers with the command:
```
docker-compose down
```
[recipebook](https://127.0.0.1:8000)




[top](#top)
