class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        longest = ''
        for e in s:
            tmp_len = 0
            if e in longest:
                longest = e
                tmp_len = 1
            else:
                longest += e
                tmp_len = len(longest)    
            
            length = length if length > tmp_len else tmp_len
        
        return length

def stringToString(input):
    return input[1:-1].decode('string_escape')

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToString(line)
            
            ret = Solution().lengthOfLongestSubstring(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
