# 💹 Day-8: Stock Buy and Sell (With One Transaction)

This repository provides an efficient Python solution for the classic **Stock Buy and Sell** problem (with the constraint of only **one transaction**). The implementation is designed using a greedy approach and runs in **O(n)** time with **O(1)** space.

---

## 📌 Problem Statement

Given an array of stock prices, where `prices[i]` is the price of a given stock on the `i-th` day, determine the **maximum profit** you can achieve **from a single buy-sell transaction**.  
You must **buy before you sell**.

---

## 🧠 Approach & Intuition

To maximize profit:

- You want to **buy at the lowest price** observed so far.
- You want to **sell at the current price** if it gives a better profit than before.
- We track `min_price` (lowest seen so far) and `max_profit` (best difference observed).

This is a **greedy linear pass**, updating both values as we iterate.

---

## 🔄 Algorithm Steps

1. Edge case: If the list has less than 2 elements, return 0.
2. Initialize `min_price` as ∞ and `max_profit` as 0.
3. Loop through each day's price:
   - Update `min_price` if the current price is lower.
   - Calculate today's profit: `price - min_price`.
   - Update `max_profit` if today's profit is higher.
4. Return the `max_profit`.

---

## ▶️ Sample Input/Output
Input: 
```
Enter stock prices separated by space: 2899 3499
```

## Output:
```
Maximum Profit: 600
```

---
## ✅ Complexity Analysis
Time Complexity: O(n)

Space Complexity: O(1)

---

## 🙌 Contribution
Crafted with precision by Vikash Joshi as part of the GeeksforGeeks 160 Days DSA Challenge.
Follow the journey to sharpen your fundamentals in Data Structures & Algorithms — one day at a time! 🚀

⭐ If this repo adds value to your learning, consider giving it a ⭐️ and sharing it with peers.

---
