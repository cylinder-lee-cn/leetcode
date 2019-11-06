"""
93. 复原IP地址

给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:
输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        sLen = len(s)
        if sLen < 4 or sLen > 12:
            return []

        result = []

        ipLens = {
            4: [(1, 1, 1, 1)],
            5: [(1, 1, 1, 2), (1, 1, 2, 1), (1, 2, 1, 1), (2, 1, 1, 1)],
            6: [(1, 1, 1, 3), (1, 1, 2, 2), (1, 1, 3, 1), (1, 2, 1, 2),
                (1, 2, 2, 1), (1, 3, 1, 1), (2, 1, 1, 2), (2, 1, 2, 1),
                (2, 2, 1, 1), (3, 1, 1, 1)],
            7: [(1, 1, 2, 3), (1, 1, 3, 2), (1, 2, 1, 3), (1, 2, 2, 2),
                (1, 2, 3, 1), (1, 3, 1, 2), (1, 3, 2, 1), (2, 1, 1, 3),
                (2, 1, 2, 2), (2, 1, 3, 1), (2, 2, 1, 2), (2, 2, 2, 1),
                (2, 3, 1, 1), (3, 1, 1, 2), (3, 1, 2, 1), (3, 2, 1, 1)],
            8: [(1, 1, 3, 3), (1, 2, 2, 3), (1, 2, 3, 2), (1, 3, 1, 3),
                (1, 3, 2, 2), (1, 3, 3, 1), (2, 1, 2, 3), (2, 1, 3, 2),
                (2, 2, 1, 3), (2, 2, 2, 2), (2, 2, 3, 1), (2, 3, 1, 2),
                (2, 3, 2, 1), (3, 1, 1, 3), (3, 1, 2, 2), (3, 1, 3, 1),
                (3, 2, 1, 2), (3, 2, 2, 1), (3, 3, 1, 1)],
            9: [(1, 2, 3, 3), (1, 3, 2, 3), (1, 3, 3, 2), (2, 1, 3, 3),
                (2, 2, 2, 3), (2, 2, 3, 2), (2, 3, 1, 3), (2, 3, 2, 2),
                (2, 3, 3, 1), (3, 1, 2, 3), (3, 1, 3, 2), (3, 2, 1, 3),
                (3, 2, 2, 2), (3, 2, 3, 1), (3, 3, 1, 2), (3, 3, 2, 1)],
            10: [(1, 3, 3, 3), (2, 2, 3, 3), (2, 3, 2, 3), (2, 3, 3, 2),
                 (3, 1, 3, 3), (3, 2, 2, 3), (3, 2, 3, 2), (3, 3, 1, 3),
                 (3, 3, 2, 2), (3, 3, 3, 1)],
            11: [(2, 3, 3, 3), (3, 2, 3, 3), (3, 3, 2, 3), (3, 3, 3, 2)],
            12: [(3, 3, 3, 3)]
        }

        ipPatten = ipLens[sLen]

        print(ipPatten)

        def vaildIP(n):
            if len(n) > 1 and n[0] == '0':
                return False
            elif int(n) > 255:
                return False
            else:
                return True

        for p in ipPatten:
            l1, l2, l3, l4 = p
            ip1 = s[0:l1]
            ip2 = s[l1:(l1 + l2)]
            ip3 = s[(l1 + l2):(l1 + l2 + l3)]
            ip4 = s[(l1 + l2 + l3):]
            ip = [ip1, ip2, ip3, ip4]
            if all([vaildIP(x) for x in ip]):
                result.append('.'.join(ip))

        print(result)
        return result


s = Solution()
# s.restoreIpAddresses('25525511135')
s.restoreIpAddresses('01101')
s.restoreIpAddresses('')
"""
此题解法：
* 首先要确定s的长度，然后根据长度进行分组，最长12位，最短4位
* 数字长度的组合有限，可以预先制表，用于查询，这样可以大幅度减少可能性，尽在有限的范围内进行核实
* IP首位数字不能为0，每段数字都在0-255
"""
