class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create empty dict that holds char count dicts as keys
        # anagram sublists as values
        counts_dict = defaultdict(list)

        # for each str in strs
        for s in strs:
            # loop over str chars and create count array where c_count[0]
            # is 'a' count, c_count[1] is 'b' count, ...
            c_count = [0] * 26

            for c in s:
                c_count[ord(c) - ord('a')] += 1

            # add str to sublist
            # convert c_count to tuple since tuples are hashable
            counts_dict[tuple(c_count)].append(s)
        
        # return dict values (sublists)
        return list(counts_dict.values())

        # size: O(n)
        # time: O(n * m)