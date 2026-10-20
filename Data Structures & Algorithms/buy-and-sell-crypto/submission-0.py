class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p, min_p = prices[0], prices[0]
        profit = 0;
        for i in range(1, len(prices)):
            if prices[i] < min_p:
                min_p = prices[i]
                max_p = prices[i]
            if prices[i] > max_p:
                max_p = prices[i]

            if profit < max_p - min_p:
                profit = max_p - min_p

        return profit