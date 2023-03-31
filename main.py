# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

#PART 1
#1 - Variables
scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'
goal_0 = 32
goal_1 = 54

#2 - Who scored when
scorers = F"{scorer_1} {goal_0}, {scorer_2} {goal_1}"
print(scorers)

#2 - f string

report = f"{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute"
print(report)

#PART 2
#1 first name
player = 'Berry van Aerle'
space = player.find(" ")
print(space)
first_name = player[0:space]
print(first_name)

#2 last name
last_name = player[space+1:]
last_name_len = len(last_name)
print(last_name)
print(last_name_len)

#3 name short
initial = player[0]
name_short = initial + ". " + last_name
print(name_short)

#4 chant
first_name_chant = first_name + '! '
chant = (first_name_chant) * len(first_name)
chant = chant[:-1]
print(chant)

#5 good chant
good_chant = chant[-1] != ' '
print(good_chant)
