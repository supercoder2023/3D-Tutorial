# 3D and 2D Cube Visualization

This project demonstrates how to visualize 2D and 3D cubes using both Python and C++. It includes scripts for rotating cubes, interactive camera movement, and perspective projection.

## Files Overview

### Python Files

#### `cube2d.py`
This script visualizes a 2D square that rotates around its center. Key features:
- **Vertices and Edges**: Defines the 4 corners of the square and the edges connecting them.
- **2D Rotation**: Uses trigonometric formulas to rotate the square around the origin.
- **Drawing**: Projects the rotated points directly onto the screen (no perspective needed).

#### `cube3d.py`
This script visualizes a 3D cube that rotates around the Y-axis. Key features:
- **Vertices and Edges**: Defines the 8 corners of the cube and the edges connecting them.
- **3D Rotation**: Uses trigonometric formulas to rotate the cube around the Y-axis.
- **Projection**: Applies a perspective projection to simulate depth, making the cube appear 3D.

#### `move.py`
This script extends the 3D cube visualization by adding interactive camera movement. Key features:
- **Camera Controls**: Use the following keys to move the camera:
  - `W`: Move forward (into the screen).
  - `S`: Move backward (away from the screen).
  - `Up Arrow`: Move up (jump).
  - `Down Arrow`: Move down (crouch).
- **Dynamic Camera Transformation**: Adjusts the cube's position relative to the camera.
- **Auto-Rotation**: The cube rotates continuously around the X and Y axes.

### C++ Files

#### `cube.cpp`
This script visualizes a rotating 3D cube in the console using ASCII characters. Key features:
- **Vertices and Edges**: Defines the 8 corners of the cube and the edges connecting them.
- **3D Rotation**: Rotates the cube around the Y-axis using trigonometric functions.
- **Projection**: Applies a perspective projection to simulate depth.
- **ASCII Rendering**: Renders the cube in the console using a buffer of characters.

#### `cube_safe.cpp`
This is a safer version of `cube.cpp` with additional checks and improvements. Key features:
- **Improved Line Drawing**: Ensures no infinite loops during line drawing.
- **Static Frame**: Renders a single frame of the cube with a fixed rotation angle.
- **Console Output**: Displays the cube in the console with a larger resolution.

## How to Run

### Python Scripts
1. Make sure Python is installed on your system.
2. Run any of the scripts using the following command:
   ```bash
   python <script_name>.py