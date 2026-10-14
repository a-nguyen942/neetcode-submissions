class Solution:
    def buildLetterList(self, word):
        letter_list = [0] * 26
        for j in range(len(word)):
            letter_index = ord(word[j]) - ord('a')
            letter_list[letter_index] += 1
        return tuple(letter_list)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution_dict = dict()
        for i in range(len(strs)):
            if not solution_dict:
                a = self.buildLetterList(strs[i])
                solution_dict[a] = [strs[i]]
                continue
            a = self.buildLetterList(strs[i])
            if a in solution_dict:
                solution_dict[a].append(strs[i])
            else:
                solution_dict[a] = [strs[i]]
            
            
        return list(solution_dict.values())