class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create empty dict that holds char count dicts as keys
        # anagram sublists as values
        counts_dict = {}

        # for each str in strs
        for s in strs:
            # loop over str chars and create count array where c_count[0]
            # is 'a' count, c_count[1] is 'b' count, ...
            c_count = [0] * 26

            for c in s:
                # get index of count by converting a -> 0, b -> 1, ...
                i = ord(c) - ord('a')

                # increment the counter
                c_count[i] += 1

            # convert to string since list isn't hashable
            c_count = str(c_count)

            # if already in counts dict then add str to sublist
            # if not create new sublist and add str
            if c_count in counts_dict:
                counts_dict[c_count].append(s)
            else:
                counts_dict[c_count] = [s]
        
        # return dict values (sublists)
        return list(counts_dict.values())

        # size: O(n)
        # time: O(n * m)