//Maximum Number of Words Found in Sentences

class Solution {
 public:
  int mostWordsFound(vector<string>& sentences) {
    long maxSpaceCount = 0;

    for (const string& s : sentences)
      maxSpaceCount = max(maxSpaceCount, ranges::count(s, ' '));

    return maxSpaceCount + 1;
  }
};