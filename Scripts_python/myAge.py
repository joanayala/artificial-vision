#Developer: Joan C. Ayala
'''
What does this script do?:
This script show your name and your age.
'''

'''
How config git in my computer?
1st. git config --global user.name "myusername"
2nd. git config --global user.email "mygitemail"


How make a tracking/staging to GitHub or GitLab

1st. git add . / git add --all / git add file_name
2nd. git commit -m "Your message"
3rd. git push origin master
'''

myName = 'Joan C. Ayala'
myDate = 1985
year = 2020

age = year - myDate

print ("Your name is: ", myName, "and you are ", age, "years old")
