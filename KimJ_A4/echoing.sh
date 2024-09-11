#!/bin/bash

#Activity 1
#“The time and date are:” and provide the date and time
echo "The time and date are: $(date)"

#“Let’s see who is logged into the system:” and provides us with the users
echo "Let's see who is logged into the system: "
who

#“For <user>, the home directory is <home directory path>”
echo "For $USER, the home directory is $HOME"

#Activity 2
#takes in a positional argument with your name and how much cash you have on you
NAME=$1
MONEY=$2
echo "My name is $NAME and I have \$$MONEY in my wallet."

#Activity 3
#Define 'mathvar1' as 1+5
mathvar1=$[1+5]

#Use 'mathvar1' into calculating 'mathvar2' which we will say 'mathvar2' = 'mathvar1'*20
mathvar2=$[$mathvar1*20]

#Define 'mathvar3' as 10
mathvar3=10

#Calculate 'mathvar4' to be 'mathvar1'*('mathvar2'+'mathvar3')
temp=$[$mathvar2+$mathvar3]
mathvar4=$[$mathvar1*$temp]

#Display “Variable 1 is <'mathvar1'>. Variable 2 is <'mathvar2'>. Using <'mathvar3'> for Variable 3, our final Variable 4 is <'mathvar4'>.”
echo "Variable 1 is $mathvar1."
echo "Variable 2 is $mathvar2."
echo "Using $mathvar3 for Variable 3, our final Variable 4 is $mathvar4."

#Activity 4
#Define a variable 'floating' that is equal to 4.5/1.7
floating=$(echo "scale=3; 4.5/1.7"|bc)
echo "Our floating varaible is $floating"
