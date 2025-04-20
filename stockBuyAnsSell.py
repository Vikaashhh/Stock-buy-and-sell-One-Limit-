class Solution:
    def maximumProfit(self, prices):

        # Edge case: Agar prices list empty hai ya usme sirf ek price hai
        if len(prices) < 2:
            return 0

        # Minimum price ko initially infinite set karte hain
        min_price = float('inf')        
        
        max_profit = 0            # Max profit initially 0

        # Har din ke price par iterate karo
        for price in prices:
        
            # Sabse kam price update karo agar naya price chhota hai
            min_price = min(min_price, price)
        
            # Aaj bechne par kya profit milega
            profit_today = price - min_price
        
            # Max profit update karo agar aaj ka profit zyada hai
            max_profit = max(max_profit, profit_today)

        return max_profit


# ------- Driver Code --------
if __name__ == "__main__":
    prices = list(map(int, input("Enter stock prices separated by space: ").split()))
    obj = Solution()
    result = obj.maximumProfit(prices)
    print("Maximum Profit:", result)