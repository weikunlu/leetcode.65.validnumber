
class Solution(object):

    INVALID=0
    SIGN=1
    POINT=2
    EXPONENT=3
    DIGIT=4

    def get_char_type(self, char):
        if char in '+-':
            return Solution.SIGN
        if char == '.':
            return Solution.POINT
        if char in 'Ee':
            return Solution.EXPONENT
        if char in '0123456789':
            return Solution.DIGIT
        return Solution.INVALID

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # clean data
        s = s.strip()

        # print '=====test string:%r'%(s)

        # boundary check
        if len(s)==1:
            char_type = self.get_char_type(s)
            return char_type == Solution.DIGIT
        elif len(s)==0:
            return False

        # iterate string for checking valid number 
        state = 0
        for i in range(0, len(s)):
            char_type = self.get_char_type(s[i])
            
            if char_type == Solution.INVALID:
                return False

            # print 'b: [%s] state: %04x %r'%(s[i], state, char_type)

            if state == 0: # initial
                if char_type == Solution.SIGN:
                    state = 0x0001
                elif char_type == Solution.POINT:
                    state = 0x0002
                elif char_type == Solution.DIGIT:
                    state = 0x0013
                else:
                    return False
            elif (state&0x0004) == 0x0004: # exponent mode

                if char_type == Solution.SIGN:
                    state = 0x0001 | (state&0x0ff0)
                elif char_type == Solution.DIGIT:

                    state = 0x0013 | (state&0x0ff0)
                else:
                    return False
            elif (state&0x0003) == 0x0003: # is number

                if char_type == Solution.POINT:
                    if (state&0x0120)>0:
                        return False
                    state = 0x0002 | (state&0x0ff0)
                elif char_type == Solution.EXPONENT:

                    if (state&0x0100)>0:
                        return False
                    state = 0x0104 | (state&0x0120)
                elif char_type == Solution.DIGIT:
                    state = 0x0013 | (state&0x0ff0)
                else:
                    return False
            elif (state&0x0002) == 0x0002: # is point

                if char_type == Solution.DIGIT:
                    state = 0x0033
                elif char_type == Solution.EXPONENT:
                    if state == 0x0002:
                        return False
                    state = 0x0124 | (state&0x0f00)
                else:
                    return False
            elif (state&0x0001) == 0x0001: # is sign

                if char_type == Solution.POINT:
                    state = 0x0002
                elif char_type == Solution.DIGIT:
                    state = 0x0013 | (state&0x0f20)
                else:
                    return False

            state |= (state&0x0ff0)
            # print 'a: state: %04x'%(state)

        return (state&0x0003)==0x0003 or (state&0x0010)>0
