The repository was created for recruitment purposes. This application is my first application written in Python so this is why the code is messy and really needs refactoring. This code is the result of coding by 2 months from August to September in 2016. The purpose was to learn basics of Python. I also have familiarized with Selenium module.

# Description
## Overview
The main goal of this application was to automate playing the browser game Tentlan. The application also provides sending messages about game status to facebook account and receiving commands from facebook messages. Unfortunately changes in implementation crushed this feature so I had to switch it off.

The code was written in Python 2. Application is based on Selenium module.

## Some Features
The main features provides possibility to continuously collecting goods and defending strategic villages from enemies.

To collect goods, player firstly needs to make the order for production of specific good, then choose production time. The longer time production takes, the less efficient production is. So the most efficient decision is to choose the least time of production. So the application iterate trough all villages and makes orders for production of all goods that takes the least time. This loop is endless until something gets crushed.

One of game rules allows attacking 5 barbarian villages once a day. The barbarians villages have its level and troops. The higher level of the village, the higher benefit of attacking it. The greater distance between the attacker and barbarian village, the greater costs of sending troops. So application provides the feature that collects information about nearest map area, search all barbarians villages that can be defeated without losses and providing optimal benefits, compute distances between the attacker and barbarian village and chooses 5 nearest villages that meet previous requirements. Of course, this function is performed once a day.

Another feature provides defending system against other players. One way to defend without losses is to send somewhere all troops and goods in the village. The goal is to not keep these things in the village while the village is under attack. Every time another player is attacking us we can see the time when enemy troops will arrive. So the application gets this time and calculate timings that must be meet up to avoid losses and sends all troops and goods to another place. After attack troops come back to the village.

## Author
Mateusz Krogul

