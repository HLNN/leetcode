# LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.
#
# You are given a list of strings keyName and keyTime where [keyName[i], keyTime[i]] corresponds to a person's name and the time when their key-card was used in a single day.
#
# Access times are given in the 24-hour time format "HH:MM", such as "23:51" and "09:49".
#
# Return a list of unique worker names who received an alert for frequent keycard use. Sort the names in ascending order alphabetically.
#
# Notice that "10:00" - "11:00" is considered to be within a one-hour period, while "22:51" - "23:52" is not considered to be within a one-hour period.
#
#  
# Example 1:
#
#
# Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
# Output: ["daniel"]
# Explanation: "daniel" used the keycard 3 times in a one-hour period ("10:00","10:40", "11:00").
#
#
# Example 2:
#
#
# Input: keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
# Output: ["bob"]
# Explanation: "bob" used the keycard 3 times in a one-hour period ("21:00","21:20", "21:30").
#
#
#  
# Constraints:
#
#
# 	1 <= keyName.length, keyTime.length <= 105
# 	keyName.length == keyTime.length
# 	keyTime[i] is in the format "HH:MM".
# 	[keyName[i], keyTime[i]] is unique.
# 	1 <= keyName[i].length <= 10
# 	keyName[i] contains only lowercase English letters.
#
#


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def time2int(t):
            h, m = t.split(':')
            return 60 * int(h) + int(m)
        
#         res = set()
#         dd = defaultdict(lambda: [-inf, -inf])
#         for t, n in sorted(zip(keyTime, keyName)):
#             dd[n].append(time2int(t))
#             if dd[n][-3] < dd[n][-1] <= dd[n][-3] + 60:
#                 res.add(n)
        
#         return sorted(res)
    
        res = []
        dd = defaultdict(list)
        for n, t in zip(keyName, keyTime):
            dd[n].append(time2int(t))
        for n, t in dd.items():
            t.sort()
            for i in range(2, len(t)):
                if t[i] <= t[i - 2] + 60:
                    res.append(n)
                    break
        return sorted(res)
