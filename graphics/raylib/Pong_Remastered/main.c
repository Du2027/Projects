#include<stdio.h>
#include<raylib.h>

int main(void){

    const int width = 800;
    const int height = 500;

    InitWindow(width, height, "TEst");
    SetTargetFPS(60);

    while (!WindowShouldClose())
    {
        BeginDrawing();
            ClearBackground(RAYWHITE);
            DrawText("HELLOW!", 190, 200, 20 , LIGHTGRAY);
        EndDrawing();
    }

    CloseWindow();
    return 0;
}
