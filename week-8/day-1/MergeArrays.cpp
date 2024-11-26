#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    
    // Input size and elements of the first array
    cin >> n;
    vector<int> array1(n);
    for (int i = 0; i < n; ++i) {
        cin >> array1[i];
    }
    
    // Input size and elements of the second array
    cin >> m;
    vector<int> array2(m);
    for (int i = 0; i < m; ++i) {
        cin >> array2[i];
    }
    
    // Merging the two sorted arrays
    vector<int> mergedArray;
    int i = 0, j = 0;
    
    while (i < n && j < m) {
        if (array1[i] < array2[j]) {
            mergedArray.push_back(array1[i]);
            ++i;
        } else {
            mergedArray.push_back(array2[j]);
            ++j;
        }
    }
    
    // Append remaining elements from the first array
    while (i < n) {
        mergedArray.push_back(array1[i]);
        ++i;
    }
    
    // Append remaining elements from the second array
    while (j < m) {
        mergedArray.push_back(array2[j]);
        ++j;
    }
    
    // Output the merged sorted array
    for (int num : mergedArray) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}
