# some-random-vibecoding-shi
# just for the sake of participating in the event
#include <iostream>
#include <cmath>
#include <limits>

using namespace std;

void clearInput() {
    cin.clear();
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
}

double getNumber() {
    double number;

    while (true) {
        if (cin >> number) {
            return number;
        }

        cout << "Invalid input. Enter a number: ";
        clearInput();
    }
}

void basicCalculator() {
    double a, b;
    char op;

    cout << "\nEnter first number: ";
    a = getNumber();

    cout << "Enter operator (+, -, *, /, %): ";
    cin >> op;

    cout << "Enter second number: ";
    b = getNumber();

    switch (op) {
        case '+':
            cout << "Result: " << a + b << endl;
            break;

        case '-':
            cout << "Result: " << a - b << endl;
            break;

        case '*':
            cout << "Result: " << a * b << endl;
            break;

        case '/':
            if (b == 0) {
                cout << "Error: division by zero." << endl;
            } else {
                cout << "Result: " << a / b << endl;
            }
            break;

        case '%':
            if (b == 0) {
                cout << "Error: division by zero." << endl;
            } else {
                cout << "Result: " << fmod(a, b) << endl;
            }
            break;

        default:
            cout << "Error: invalid operator." << endl;
    }
}

void powerCalculator() {
    double base, exponent;

    cout << "\nEnter base: ";
    base = getNumber();

    cout << "Enter exponent: ";
    exponent = getNumber();

    cout << "Result: " << pow(base, exponent) << endl;
}

void squareRootCalculator() {
    double number;

    cout << "\nEnter number: ";
    number = getNumber();

    if (number < 0) {
        cout << "Error: cannot calculate square root of a negative number." << endl;
    } else {
        cout << "Result: " << sqrt(number) << endl;
    }
}

void percentageCalculator() {
    double number, percent;

    cout << "\nEnter number: ";
    number = getNumber();

    cout << "Enter percentage: ";
    percent = getNumber();

    cout << "Result: " << number * percent / 100 << endl;
}

void factorialCalculator() {
    int number;

    cout << "\nEnter a non-negative integer: ";

    while (!(cin >> number) || number < 0) {
        cout << "Invalid input. Enter a non-negative integer: ";
        clearInput();
    }

    if (number > 20) {
        cout << "Error: number is too large." << endl;
        return;
    }

    unsigned long long result = 1;

    for (int i = 1; i <= number; i++) {
        result *= i;
    }

    cout << "Result: " << result << endl;
}

void calculatorMenu() {
    int choice;

    while (true) {
        cout << "\n========== CALCULATOR ==========\n";
        cout << "1. Basic calculator\n";
        cout << "2. Power\n";
        cout << "3. Square root\n";
        cout << "4. Percentage\n";
        cout << "5. Factorial\n";
        cout << "0. Exit\n";
        cout << "===============================\n";
        cout << "Choose an option: ";

        if (!(cin >> choice)) {
            cout << "Error: invalid menu choice." << endl;
            clearInput();
            continue;
        }

        switch (choice) {
            case 1:
                basicCalculator();
                break;

            case 2:
                powerCalculator();
                break;

            case 3:
                squareRootCalculator();
                break;

            case 4:
                percentageCalculator();
                break;

            case 5:
                factorialCalculator();
                break;

            case 0:
                cout << "Goodbye!" << endl;
                return;

            default:
                cout << "Error: choose a number from 0 to 5." << endl;
        }
    }
}

int main() {
    calculatorMenu();
    return 0;
}
