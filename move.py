import turtle
import math

# --- SETUP ---
screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Press 'W' to Walk Forward, 'S' to Walk Back")
screen.tracer(0) 

pen = turtle.Turtle()
pen.hideturtle()
pen.color("cyan")
pen.width(3)

# --- VARIABLES ---
vertices = [
    [-1, -1, -1], [1, -1, -1], [1, 1, -1], [-1, 1, -1],
    [-1, -1, 1],  [1, -1, 1],  [1, 1, 1],  [-1, 1, 1]
]
edges = [
    (0,1), (1,2), (2,3), (3,0),
    (4,5), (5,6), (6,7), (7,4),
    (0,4), (1,5), (2,6), (3,7)
]

angle_x = 0
angle_y = 0

# NEW: Camera Position
camera_z = 0 
camera_y = 0

# --- CONTROLS ---
def move_forward():
    global camera_z
    camera_z += 0.5  # Move camera into the screen

def move_backward():
    global camera_z
    camera_z -= 0.5  # Move camera away

def move_up():
    global camera_y
    camera_y += 0.5 # Move camera up (jump)

def move_down():
    global camera_y
    camera_y -= 0.5 # Move camera down (crouch)

# Listen for keyboard input
screen.listen()
screen.onkeypress(move_forward, "w")
screen.onkeypress(move_backward, "s")
screen.onkeypress(move_up, "Up")     # Arrow Up
screen.onkeypress(move_down, "Down") # Arrow Down

# --- MAIN LOOP ---
def draw_frame():
    global angle_x, angle_y
    pen.clear()
    
    # Auto-rotate the cube so it looks cool
    angle_x += 0.02
    angle_y += 0.03
    
    projected_points = []
    
    for v in vertices:
        x, y, z = v[0], v[1], v[2]
        
        # 1. ROTATE (Spin the object)
        ry = y
        rx = x * math.cos(angle_y) - z * math.sin(angle_y)
        rz = x * math.sin(angle_y) + z * math.cos(angle_y)
        
        rx2 = rx
        ry2 = ry * math.cos(angle_x) - rz * math.sin(angle_x)
        rz2 = ry * math.sin(angle_x) + rz * math.cos(angle_x)
        
        # 2. CAMERA TRANSFORM (The New Math!)
        # We move the object relative to the camera
        # To simplify, we push the object 5 units away so it starts in front of us
        final_x = rx2
        final_y = ry2 - camera_y  # Subtract Camera Y
        final_z = rz2 + 5 - camera_z # Subtract Camera Z (Offset by 5)
        
        # 3. PROJECTION
        fov = 400
        
        # Safety: Avoid dividing by zero if camera hits the object
        if final_z < 0.1: 
            final_z = 0.1
            
        scale = fov / final_z
        
        x_2d = final_x * scale
        y_2d = final_y * scale
        
        projected_points.append((x_2d, y_2d))
            
    # Draw Lines
    for edge in edges:
        p1 = projected_points[edge[0]]
        p2 = projected_points[edge[1]]
        pen.penup()
        pen.goto(p1)
        pen.pendown()
        pen.goto(p2)

    # Display Instructions
    pen.penup()
    pen.goto(-350, 260)
    pen.write(f"Camera Z: {camera_z:.1f} (Press W/S)", font=("Arial", 16, "normal"))
    
    screen.update()
    screen.ontimer(draw_frame, 30)

draw_frame()
turtle.done()