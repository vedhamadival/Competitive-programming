#include <iostream>
#include <string>
using namespace std;

string trimWhiteSpaces(const string& str) {
    int n = str.length();
    int start = 0, end = n - 1;

    // Find the index of the first non-space character
    while (start < n && str[start] == ' ') {
        start++;
    }

    // Find the index of the last non-space character
    while (end >= 0 && str[end] == ' ') {
        end--;
    }

    // If the string is entirely spaces, return an empty string
    if (start > end) {
        return "";
    }

    // Extract the substring from start to end
    string result = "";
    for (int i = start; i <= end; i++) {
        result += str[i];
    }

    return result;
}

int main() {
    string input;
    getline(cin, input); // Read the input string with spaces

    string trimmedString = trimWhiteSpaces(input);
    cout << trimmedString << endl;

    return 0;
}
