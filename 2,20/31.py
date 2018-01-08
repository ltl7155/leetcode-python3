# 思路：1）由于下一个数比上一个数大，因此需要从后往前扫描，找到递增的位置设为元素i,j(i小于j)
# 2）由于下一个数虽然大于上一个数，且最接近上一个数，因此找到元素i，在i元素后面找到最接近i且大于i的元素k。由于i后面的元素都是降序排列的，只需要从后往前扫描找到第一个比i大的元素即可
# 3）找到将i和k交换位置，然后将k后面的元素递增排序
# 4）找不到，则将全部元素递增排序

class Solution:

    def nextPermutation(self, num):
        lenth = len(num) - 1
        while lenth > 0:
            if num[lenth - 1] < num[lenth]:
                break
            lenth -= 1
        if lenth == 0:
            num.reverse()
        k = len(num) - 1
        while k >= lenth:
            if num[k] > num[lenth - 1]:
                break
            k -= 1
        num[k], num[lenth - 1] = num[lenth - 1], num[k]
        newnum = num[lenth:]
        newnum.sort()
        num[lenth:] = newnum
