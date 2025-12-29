import turtle
import math

# --- SETUP ---
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0) 

pen = turtle.Turtle()
pen.hideturtle()
pen.color("lime")
pen.width(3)

# --- THE DATA (8 corners of a cube) ---
vertices = [
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1],  [1, -1, 1],  [1, 1, 1],  [-1, 1, 1]
]

# Lines connecting the corners
edges = [
    (0,1), (1,2), (2,3), (3,0), # Back Face
    (4,5), (5,6), (6,7), (7,4), # Front Face
    (0,4), (1,5), (2,6), (3,7)  # Connecting Lines
]

angle = 0

def draw_one_frame():
    global angle
    pen.clear()
    angle += 0.05  # Speed of rotation
    
    projected_points = []
    
    # --- THE MATH LOOP ---
    for v in vertices:
        x, y, z = v[0], v[1], v[2]
        
        # 1. ROTATION MATH (Trigonometry)
        # Rotate around Y-axis
        # New X depends on old X and Z
        # New Z depends on old X and Z
        rotated_x = x * math.cos(angle) - z * math.sin(angle)
        rotated_z = x * math.sin(angle) + z * math.cos(angle)
        rotated_y = y # Y doesn't change when spinning left/right
        
        # 2. PROJECTION MATH (Perspective Divide)
        distance = 4
        fov = 400
        # The further away (z), the smaller the scale
        scale = fov / (distance + rotated_z)
        
        x_2d = rotated_x * scale
        y_2d = rotated_y * scale
        
        projected_points.append((x_2d, y_2d))
            
    # --- DRAWING LINES ---
    for edge in edges:
        p1 = projected_points[edge[0]]
        p2 = projected_points[edge[1]]
        pen.penup()
        pen.goto(p1)
        pen.pendown()
        pen.goto(p2)

    screen.update()
    screen.ontimer(draw_one_frame, 30)

draw_one_frame()
turtle.done()