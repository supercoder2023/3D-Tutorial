#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm> // For std::max

// Define screen size
const int WIDTH = 60;
const int HEIGHT = 30;
char buffer[WIDTH * HEIGHT];

struct Point3D { float x, y, z; };

// 8 corners of a cube
std::vector<Point3D> vertices = {
    {-1, -1, -1}, {1, -1, -1}, {1, 1, -1}, {-1, 1, -1},
    {-1, -1, 1},  {1, -1, 1},  {1, 1, 1},  {-1, 1, 1}
};

// Connections
std::vector<std::pair<int, int>> edges = {
    {0,1}, {1,2}, {2,3}, {3,0},
    {4,5}, {5,6}, {6,7}, {7,4},
    {0,4}, {1,5}, {2,6}, {3,7}
};

// Safer Line Drawing (No infinite while-loop)
void drawLine(int x1, int y1, int x2, int y2) {
    float dx = (float)(x2 - x1);
    float dy = (float)(y2 - y1);
    float steps = std::max(std::abs(dx), std::abs(dy));

    if (steps == 0) return;

    float xInc = dx / steps;
    float yInc = dy / steps;

    float x = (float)x1;
    float y = (float)y1;

    for (int i = 0; i <= steps; i++) {
        // Only draw if inside screen boundaries
        if (x >= 0 && x < WIDTH && y >= 0 && y < HEIGHT) {
            buffer[(int)y * WIDTH + (int)x] = '#';
        }
        x += xInc;
        y += yInc;
    }
}

int main() {
    std::cout << "1. Initializing..." << std::endl;

    // Fill background with dots
    for (int i = 0; i < WIDTH * HEIGHT; i++) buffer[i] = '.';

    std::cout << "2. Calculating Math..." << std::endl;
    
    // Rotate slightly (Angle = 0.5 radians)
    float angle = 0.5f; 
    std::vector<std::pair<int, int>> projectedPoints;

    for (auto& v : vertices) {
        float x = v.x, y = v.y, z = v.z;

        // Rotation
        float rx = x * cos(angle) - z * sin(angle);
        float rz = x * sin(angle) + z * cos(angle);

        // Projection
        float dist = 4.0f;
        float scale = 20.0f;
        
        float projX = (rx * scale * 2) / (dist + rz);
        float projY = (y * scale) / (dist + rz);

        // Center on screen
        projectedPoints.push_back({
            (int)(projX + WIDTH / 2),
            (int)(projY + HEIGHT / 2)
        });
    }

    std::cout << "3. Drawing Lines..." << std::endl;
    for (auto& edge : edges) {
        drawLine(projectedPoints[edge.first].first, projectedPoints[edge.first].second,
                 projectedPoints[edge.second].first, projectedPoints[edge.second].second);
    }

    std::cout << "4. RENDERING OUTPUT:" << std::endl;
    std::cout << "---------------------------------" << std::endl;

    // Print buffer
    for (int i = 0; i < WIDTH * HEIGHT; i++) {
        if (i > 0 && i % WIDTH == 0) std::cout << "\n";
        std::cout << buffer[i];
    }
    
    std::cout << "\n---------------------------------" << std::endl;
    std::cout << "Done." << std::endl;

    return 0;
}