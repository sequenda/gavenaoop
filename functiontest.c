#include <stdio.h>
#include <math.h>

int circleArea(int radius) {
    float pi = 3.14;
    return pi * radius * radius;

}

float unnecessary_function() {
    float x = pow(3.0, 2.0);
    printf("%f\n", x);
    
    int y = 5 << 1;
    printf("%d", y);
}

void main() {
    int myRadius = 3;
    int myCircleArea = circleArea(myRadius);
    printf("Circle radius: %d\nCircle area: %d\n", myRadius, myCircleArea);

    unnecessary_function();

}

