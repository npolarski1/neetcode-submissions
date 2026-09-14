class Solution:

    delim = "?"

    def encode(self, strs: List[str]) -> str:
        out = []

        # loop over strs
        for s in strs:
            # append len of str and delim to out
            out.append(f"{len(s)}{self.delim}{s}")

        # return out
        return "".join(out)

    def decode(self, s: str) -> List[str]:
        out = []

        # iterate over s
        i = 0
        while i < len(s):
            str_len = []

            # process digits until we reach delim
            while s[i] != self.delim:
                str_len.append(s[i])
                i += 1

            str_len = "".join(str_len)

            # convert that number string to int
            str_len = int(str_len)

            # then skip delim, loop that many times adding each char to string
            i += 1
            added_str = []
            for j in range(str_len):
                added_str.append(s[i])
                i += 1

            # append that string to output list
            out.append("".join(added_str))
        
        return out
