class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # create empty dict that holds sorted anagaram as key
        # and anagram sublists as values
        sublist_dict = {}
        # for each str in strs
        for s in strs:
        # sort str and see if its in dict
            sorted_str = "".join(sorted(s))
            if sorted_str in sublist_dict:
            # if so add to corresponding sublist
                sublist_dict[sorted_str].append(s)
            # if not add sorted str to key and str to new sublist
            else:
                sublist_dict[sorted_str] = [s]
        # return dict values (sublists)
        return list(sublist_dict.values())

        # time: O(n) where n is len(strs) for loop over strs
        # size: O(n) where n is len(strs) for sublist dict