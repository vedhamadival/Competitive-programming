#include <iostream>
#include <string>
using namespace std;

// Function to remove the last occurrence of a word
string removeLastOccurrence(string str, string word) {
    int str_len = str.length();
    int word_len = word.length();
    
    int pos = -1;  // Position of the last occurrence of the word

    // Traverse from the end of the string to find the last occurrence of the word
    for (int i = str_len - word_len; i >= 0; i--) {
        bool match = true;
        
        // Check if the substring matches the word
        for (int j = 0; j < word_len; j++) {
            if (str[i + j] != word[j]) {
                match = false;
                break;
            }
        }
        
        // If a match is found, record the position and stop
        if (match) {
            pos = i;
            break;
        }
    }

    // If no occurrence is found, return the original string
    if (pos == -1) {
        return str;
    }

    // Build the result string by excluding the word from the last occurrence
    string result = str.substr(0, pos) + str.substr(pos + word_len);

    return result;
}

int main() {
    string str, word;
    getline(cin, str);  // Read the input string
    getline(cin, word); // Read the word to remove
    
    string modifiedString = removeLastOccurrence(str, word);
    cout << modifiedString << endl; // Output the modified string
    
    return 0;
}
