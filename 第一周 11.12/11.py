# 算法问题：假设现在是初始状态，下标变量i=0表示头部,下标变量j=height.size()，表示尾部，
# 那么显然此时的容器的装水量取决一个矩形的大小，这个矩形的长度为j-i，
# 高度为height[i]与height[j]的最小值(假设height[i]小于height[j])。
# 接下来考虑是把头部下标i向右移动还是把尾部下标j向左移动呢?
# 如果移动尾部变量j,那么就算height[j]变高了，装水量依然没有变得更大，因为短板在头部变量i。所以应该移动头部变量i。
# 也就是说，每次移动头部变量i和尾部变量j中的一个，哪个变量的高度小，就把这个变量向中心移动。
# 计算此时的装水量并且和最大装水量的当前值做比较。


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start = 0; end = len(height) - 1
        area_max = (end - start) * min(height[start],height[end])
        while start < end :
            s = start
            i = 1
            dis = end - start
            while i < dis:
                if height[start] < height[end]:
                    if height[start + i] > height[start]:
                        start = start + i
                        break
                else:
                    if height[end - i] > height[end]:
                        end = end - i
                        break
                i += 1
            if i >= dis:
                break
            area = (end - start) * min(height[start],height[end])
            area_max = max(area, area_max)

        return area_max


s = Solution()
print (s.maxArea([1,3,2,5,25,24,5]))