class Solution {
public:
    vector<int> replaceElements(vector<int>& arr) {
         int n = arr.size();
    int maxFromRight = -1;
    
    // Traverse the array from right to left
    for (int i = n - 1; i >= 0; --i) {
        int current = arr[i];
        arr[i] = maxFromRight;
        maxFromRight = std::max(maxFromRight, current);
    }
    
    return arr;
    }
};