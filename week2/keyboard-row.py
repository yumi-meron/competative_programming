class Solution:
    def findWords(self, words: List[str]) -> List[str]:
      set1 = set(['q','w','e','r','t','y','u','i','o','p'])
      set2 = set(['a','s','d','f','g','h','j','k','l'])
      set3 = set(['z','x','c','v','b','n','m'])

      #define a function to check if the letters are found in one of the sets
      def subset(word,set1,set2,set3):
        return set(word).issubset(set1) or set(word).issubset(set2) or set(word).issubset(set3)

      ans = []
      for word in words:
        #temp is temporary string that holds the word in lowercase
        temp = word.lower()
        if subset(temp,set1,set2,set3):
          #if our function returns true we will append the word to our answer
          ans.append(word)
      return ans
          


        