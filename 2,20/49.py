# 要注意现将每一个字符串转化成列表再排序，还有后面的.join方法
# 仔细看看字典、数组、字符串、列表的操作

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        result = []
        ss = []
        res = {}
        for i in strs:
            temp = list(i)
            temp.sort()
            ss.append("".join(temp))
        for i in range(len(strs)):
            if ss[i] not in res:
                res[ss[i]] = []
            res[ss[i]].append(strs[i])
        for key in res:
            result.append(res[key])
        return result
