#!/bin/bash

echo -n "Check account balance?"

value=0

while 
[ $value == 0 ]
do 
	read ans
	case $ans in
	yes|YES|y|Y ) echo "I am afraid you are low on balance"
		      echo "Please top up your balance and come back later"
		      echo "Thank you for choosing the teller machine for your automated balance check"
		      echo "Please come back another time and feel most welcome"
		      value=1
		      ;;
	[nN][oO]    ) echo "Thank you for your interaction with me."
		      echo "please come back later"
		      echo "Do you wish to save on money, well look no further. As your automated teller machine, I have a few tips to share with you. Please click on this button to learn more."
		      echo "Have a fruitful day  too."
		      value=1 ;;
	*	    ) echo Yes or No of some form please ;;
	esac
done
