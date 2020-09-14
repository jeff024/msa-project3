# msa-project3

## Table of contents
* [OverView](#OverView)
* [Teck-Stack](#Teck-Stack)
* [How To Run](#How-To-Run)
* [OutComes](#Outcomes)
* [Project Demo](#Project-Demo)
* [Issues](#Issues)

## OverView
This project is a Web App that was designed to be a personal web-version study notebook. It can let user to post, edit, delete a post. All posts will be stored in a database and any changes to the posts will be commited.

## Teck-Stack
- Flask

## How To Run
Running this project on a local machine is simple: 

`python3 app.py` or `flask run`

## Outcomes
1. This web app can successfully communicate with Azure SQL Database.
2. This web app can run perfectly on local machines (Please see Demo part Below)

## Project Demo
1. Home Page
    - This is the home page of the web app
    - This page will display the most recent 3 posts in the database
    - It has a navigation bar on the top
    - All links in the page works

    <img src="https://github.com/jeff024/msa-project3/blob/master/imgs/home.PNG" width="500">
2. All Posts Page
    - This is the All Posts page of the web app
    - This page will display all the posts in the database
    - It has a navigation bar on the top
    - All links in the page works

    <img src="https://github.com/jeff024/msa-project3/blob/master/imgs/all.PNG" width="500">

3. Post Detail Page
    - After Clicking Read More Button in home page or all  posts page, this page will pop up
    - The user can edit or delete a post in this page

    <img src="https://github.com/jeff024/msa-project3/blob/master/imgs/detail.PNG" width="500">

4. AboutMe Page
    - This page is static and will display some personal information about myself

    <img src="https://github.com/jeff024/msa-project3/blob/master/imgs/aboutme.PNG" width="500">

## Issues
Although this web app works perfectly on local machine, I cannot put it in Azure Web Service Since there will be Application Error