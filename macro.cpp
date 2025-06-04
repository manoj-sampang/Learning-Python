#include <iostream>
#define SQUARE(x) ((x) * (x))
using namespace std;

int main() {
    int a = 5;
    cout << "Square of " << a << " is " << SQUARE(a) << endl;
    return 0;
}