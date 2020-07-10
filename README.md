# 🗄 Website-Server
Database and Server For My Personal Website

## 🧗🏻 Introduction
Every great website needs a good backend to host its content and my website shall be no different. While my website will be designed in react via JS, I wanted to push myself to step outside my comfort zone to try and build a server from scratch as well. Because my coding background mostly originates around Swift, initially I thought it would be fun to try and learn some server side swift using frameworks like Vapor to drive my server forward. However, as I said, this project is all about pushing myself so push I shall. Likewise my goal with this server is to build it from the ground up with a very easy to use framework called Flask using python. In addition I will attach a database to it via sqlalchemy and use it to store all of my data.

For Hosting and Deployment I really want to step out of my comfort zone. So my goal is to learn about and deploy a docker image on AWS using something like elastic-beanstalk. To really tie everything together nicely I would love to sync my github repo with my docker repo so that any change on master causes docker to recreate the docker-image. After this I would finally love to have docker alert the elastic beanstalk server via webhook and cause the server to update and reinstall every time a change is pushed up to it. This is definitely a reach goal but something I am striving to accomplish.

## 🧐 If this is your actual backend then why is it public?
Great question. While the goal is to make this my actual backend, I really think the code here not only displays my ability to code in languages other than Swift (the main language I've used on my github), but I also hope to make it an easy how-to-guide for anyone looking to learn about backend servers or designing websites from scratch. And hopefully it does just that :)

## 🧮 Current Status of Project
- [x] Initialize Github Repo
- [x] Setup Flask
- [x] Setup Sql-Alchemy
- [x] Setup User authentication route
- [ ] Setup Article Post routes
- [ ] Add Support for sending and storing photos
- [ ] Setup up for production deployment
- [ ] Configure with docker for speedy updates
- [ ] Setup and deploy on AWS

## Dependencies Used in the Making of this Server ...
Originally I was using
  - Flask
  - Marshmallow
  - SQLAlchemy  
  
However I found a very thorough guide from Flask that talks about building and deploying production-level Flask applications and have sinced been building my server that way. Now I am Using:
  - Flask
  - SQLite3
  - Werkzeug Security
  - Flask Blueprints for routing
