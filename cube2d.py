import turtle
import math

# --- SETUP ---
screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0) 

pen = turtle.Turtle()
pen.hideturtle()
pen.color("yellow")
pen.width(3)

# --- THE DATA (4 corners of a square) ---
# No Z coordinate, just X and Y
vertices = [
    [-100, -100], 
    [ 100, -100], 
    [ 100,  100], 
    [-100,  100]
]

# Connect 0->1->2->3->0
edges = [(0,1), (1,2), (2,3), (3,0)]

angle = 0

def draw_2d_frame():
    global angle
    pen.clear()
    angle += 0.05  # Speed
    
    rotated_points = []
    
    # --- THE MATH ---
    for v in vertices:
        x = v[0]
        y = v[1]
        
        # 2D ROTATION FORMULA
        # We rotate X and Y around the center (0,0)
        new_x = x * math.cos(angle) - y * math.sin(angle)
        new_y = x * math.sin(angle) + y * math.cos(angle)
        
        # No "Project" step needed because it's already 2D!
        rotated_points.append((new_x, new_y))
            
    # --- DRAWING ---
    for edge in edges:
        p1 = rotated_points[edge[0]]
        p2 = rotated_points[edge[1]]
        pen.penup()
        pen.goto(p1)
        pen.pendown()
        pen.goto(p2)

    screen.update()
    screen.ontimer(draw_2d_frame, 30)

draw_2d_frame()
turtle.done()