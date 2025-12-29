# 3D and 2D Cube Visualization with Turtle Graphics

This project demonstrates how to use Python's `turtle` graphics module to visualize 2D and 3D cubes. It includes three scripts:

1. `cube2d.py` - A rotating 2D square.
2. `cube3d.py` - A rotating 3D cube.
3. `move.py` - A 3D cube with interactive camera movement.

## Files Overview

### `cube2d.py`
This script visualizes a 2D square that rotates around its center. Key features:
- **Vertices and Edges**: Defines the 4 corners of the square and the edges connecting them.
- **2D Rotation**: Uses trigonometric formulas to rotate the square around the origin.
- **Drawing**: Projects the rotated points directly onto the screen (no perspective needed).

### `cube3d.py`
This script visualizes a 3D cube that rotates around the Y-axis. Key features:
- **Vertices and Edges**: Defines the 8 corners of the cube and the edges connecting them.
- **3D Rotation**: Uses trigonometric formulas to rotate the cube around the Y-axis.
- **Projection**: Applies a perspective projection to simulate depth, making the cube appear 3D.

### `move.py`
This script extends the 3D cube visualization by adding interactive camera movement. Key features:
- **Camera Controls**: Use the following keys to move the camera:
  - `W`: Move forward (into the screen).
  - `S`: Move backward (away from the screen).
  - `Up Arrow`: Move up (jump).
  - `Down Arrow`: Move down (crouch).
- **Dynamic Camera Transformation**: Adjusts the cube's position relative to the camera.
- **Auto-Rotation**: The cube rotates continuously around the X and Y axes.

## How to Run
1. Make sure Python is installed on your system.
2. Run any of the scripts using the following command:
   ```bash
   python <script_name>.py