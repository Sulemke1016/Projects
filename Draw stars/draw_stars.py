# Import Turtle Module.
import turtle


# Opens the .txt file 
file = open('/home/suryal/Desktop/CS/draw_stars/star_data.txt', 'r')

# Turns the data from the .txt file into a list of strings.
lines_list = file.readlines()

# Creates a variable that is a list.
list_of_stars = []

# Mutates the list to now contain other lists of the x, y, and z values, 
# and the magnitude of each star.
for star in lines_list:
	star = star.split(' ')
	star_list = [star[0], star[1], star[2], star[4]]
	list_of_stars.append(star_list)
	

# Creates a turtle and a turtle screen and sets the BG color to black.
t = turtle.Turtle()
turtle.screensize(500, 500)
turtle.bgcolor('black')
turtle.speed(0)
turtle.tracer(1, 0)

# Creates a function that draws a side of a star.
def draw_side(mag):
	t.fd(mag)
	t.right(90)


# For each star in list)_of_stars the turtle draws the star using this 
# following for loop.

for star in list_of_stars:
	t.color('black')
	t.setx(float(star[0]) * 500)
	t.sety(float(star[1]) * 500)
	t.color('white', 'white')
	
	mag = round(10/(float(star[3]) + 2))
	if mag > 10:
		mag = 10
	elif mag < 1:
		mag = 1
	
	t.begin_fill()
	draw_side(mag)
	draw_side(mag)
	draw_side(mag)
	draw_side(mag)
	t.end_fill()


# Allows for the screen to be closed with a click of the mouse.
turtle.exitonclick()


