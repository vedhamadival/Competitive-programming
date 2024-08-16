class Solution:
  def isPrefixString(self, s, words):
    prefix = []
    for word in words:
      prefix.append(word)
      if ''.join(prefix) == s:
        return True
    return False