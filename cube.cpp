#include <iostream>
#include <vector>
#include <cmath>
#include <windows.h> 

const int WIDTH = 40; // Smaller width to fit screen better
const int HEIGHT = 20;
char buffer[WIDTH * HEIGHT];

struct Point3D { float x, y, z; };

std::vector<Point3D> vertices = {
    {-1, -1, -1}, {1, -1, -1}, {1, 1, -1}, {-1, 1, -1},
    {-1, -1, 1},  {1, -1, 1},  {1, 1, 1},  {-1, 1, 1}
};

std::vector<std::pair<int, int>> edges = {
    {0,1}, {1,2}, {2,3}, {3,0},
    {4,5}, {5,6}, {6,7}, {7,4},
    {0,4}, {1,5}, {2,6}, {3,7}
};

void drawLine(int x1, int y1, int x2, int y2) {
    float dx = x2 - x1;
    float dy = y2 - y1;
    float steps = std::max(abs(dx), abs(dy));
    if(steps == 0) return;

    float xInc = dx / steps;
    float yInc = dy / steps;
    float x = x1, y = y1;
    
    for (int i = 0; i <= steps; i++) {
        if (x >= 0 && x < WIDTH && y >= 0 && y < HEIGHT) {
            buffer[(int)y * WIDTH + (int)x] = '#';
        }
        x += xInc; y += yInc;
    }
}

int main() {
    float angle = 0.0f;
    while (true) {
        // 1. Fill buffer with DOTS so we can see the empty space
        for(int i=0; i<WIDTH*HEIGHT; i++) buffer[i] = '.'; 

        angle += 0.1f;
        std::vector<std::pair<int, int>> projPoints;

        for (auto& v : vertices) {
            float x = v.x, y = v.y, z = v.z;
            float rx = x * cos(angle) - z * sin(angle);
            float rz = x * sin(angle) + z * cos(angle);
            float dist = 4.0f;
            float scale = 15.0f;
            float projX = (rx * scale * 2) / (dist + rz); 
            float projY = (y * scale) / (dist + rz); 
            projPoints.push_back({ (int)(projX + WIDTH / 2), (int)(projY + HEIGHT / 2) });
        }

        for (auto& edge : edges) {
            drawLine(projPoints[edge.first].first, projPoints[edge.first].second,
                     projPoints[edge.second].first, projPoints[edge.second].second);
        }

        // Print a separator line
        std::cout << "\n--- FRAME ---\n";
        for (int i = 0; i < WIDTH * HEIGHT; i++) {
            if (i > 0 && i % WIDTH == 0) std::cout << "\n";
            std::cout << buffer[i];
        }
        Sleep(500); // Slow speed
    }
    return 0;
}