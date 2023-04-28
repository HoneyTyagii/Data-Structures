# 839. Similar String Groups

# Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

# We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

 

# Example 1:

# Input: strs = ["tars","rats","arts","star"]
# Output: 2
# Example 2:

# Input: strs = ["omv","ovm"]
# Output: 1
 

# Constraints:

# 1 <= strs.length <= 300
# 1 <= strs[i].length <= 300
# strs[i] consists of lowercase letters only.
# All words in strs have the same length and are anagrams of each other.

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        #dedupe input
        strs=list(set(strs))

        parents=list(range(len(strs)))
        size=[1]*len(strs)

        wordlen=len(strs[0])

        def similar(word1,word2):
            diff=i=0
            while i<wordlen and diff<=2:
                if word1[i]!=word2[i]:
                    diff+=1

                i+=1

            return diff<=2

        def find(a):
            if parents[a]!=a:
                #path compression
                parents[a]=parents[parents[a]]
                a=parents[a]

            return parents[a]

        def union(a,b):
            a,b=find(a),find(b)
            if a==b:
                return 
            #swap so a is larger, as we will make a parent
            if size[a]<size[b]:
                a,b=b,a

            size[a]+=size[b]
            parents[b]=a


        for i in range(len(strs)):
            for j in range(i+1,len(strs)):
                if similar(strs[i],strs[j]):
                    union(i,j)

        #count parents who are roots(their own parent)
        return sum([1 for i,e in enumerate(parents) if i==e])                