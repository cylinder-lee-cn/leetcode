"""
748. 最短完整词

如果单词列表（words）中的一个单词包含牌照（licensePlate）中所有的字母，那么我们称之为完整词。
在所有完整词中，最短的单词我们称之为最短完整词。

单词在匹配牌照中的字母时不区分大小写，比如牌照中的 "P" 依然可以匹配单词中的 "p" 字母。

我们保证一定存在一个最短完整词。当有多个单词都符合最短完整词的匹配条件时取单词列表中最靠前的一个。
牌照中可能包含多个相同的字符，比如说：对于牌照 "PP"，单词 "pair" 无法匹配，但是 "supper" 可以匹配。

示例 1：
输入：licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
输出："steps"
说明：最短完整词应该包括 "s"、"p"、"s" 以及 "t"。对于 "step" 它只包含一个 "s" 所以它不符合条件。
同时在匹配过程中我们忽略牌照中的大小写。

示例 2：
输入：licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
输出："pest"
说明：有三个单词都符合完整词的定义，但是我们返回最先出现的单词。

注意:
牌照（licensePlate）的长度在区域[1, 7]中。
牌照（licensePlate）将会包含数字、空格、或者字母（大写和小写）。
单词列表（words）长度在区间 [10, 1000] 中。
每一个单词 words[i] 都是小写，并且长度在区间 [1, 15] 中。

"""


class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """

        d = {}
        result = ''
        short = 16
        for l in licensePlate:
            if (l.isalpha()):
                d[l.lower()] = d.get(l.lower(), 0) + 1

        for w in words:
            wl = len(w)
            if all(w.count(k) >= v for k, v in d.items()):
                if (wl < short):
                    short = wl
                    result = w
        return result


s = Solution()
# print(
#     s.shortestCompletingWord("1s3 PSt",
#                              ["step", "steps", "stripe", "stepple"]))
# print(s.shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"]))
print(
    s.shortestCompletingWord("GrC8950", [
        "measure", "other", "every", "base", "according", "level", "meeting",
        "none", "marriage", "rest"
    ]))
"""
此题解法：
* 首先将licensePlate字典化，统计字母（转换成小写）的出现次数。
* 然后遍历words，看看每个单词里是否都包含字典中的字母，并且数量足够，还需记录这个单词的长度
* 如果字母都涵盖了，就看看是否足够短，如果比short的要短，那么就记录

"""