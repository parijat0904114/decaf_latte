# decaf_latte
# GRIND 75 Problems and their nuts and bolts

This repository contains my solutions to the GRIND 75 problems. The aim of this repository is to reflect my self-improvement journey in coding by documenting my progress in problem-solving skills. [Grind 75](https://www.techinterviewhandbook.org/grind75)

## Problem List

| # | Title | Solution | Brute Force Complexity | Optimized Complexity|
| --- | --- | --- | --- | --- |
| 1 | Two Sum | [Solution](./GRIND_75/leetcode_1_two_sum.py) | T: _O(n²)_ <br> S: _O(1)_ | T: _O(n)_ <br> S: _O(n)_ |
| 20 | Valid Parentheses | [Solution](./GRIND_75/leetcode_20_valid_parentheses.py) | | T: _O(len(s)_ <br> S: _O(len(s)_ |
| 21 | Merge Two Sorted Lists | [Solution](./GRIND_75/leetcode_21_merge_two_sorted_lists.py) | | m = len(list1), n = len(list2) <br> T: _O(m+n)_ <br> S: _O(1)_ (additional nodes just point to list1 or list2)|
| 121 | Best Time to Buy and Sell Stock | [Solution](./GRIND_75/leetcode_121_best_time_to_buy_and_sell_stock.py) | T: _O(n²)_ <br> S: _O(1)_ | T: _O(n)_ <br> S: _O(1)_ |
| 125 | Valid Palindrome | [Solution](./GRIND_75/leetcode_125_valid_palindrome.py) | T: _O(n)_ <br> S: _O(n)_ | T: _O(n)_ <br> S: _O(1)_ |
| 226 | Invert Binary Tree | [Solution](./GRIND_75/leetcode_226_invert_binary_tree.py) | | DFS with Recursion <br> T: _O(n)_ <br> S: _O(n)_ <br><br> DFS with Stack <br> T: _O(n)_ S: _O(n)_ <br><br> BFS <br> T: _O(n)_ <br> S: _O(n)_ |
| 242 | Valid Anagram | [Solution](./GRIND_75/leetcode_242_valid_anagram.py) | T: _O(nlogn)_ <br> S: _O(1) or _O(n)_ <br> (Depending on Sorting Algorithm) | For ASCII (Solution 3), frequence of 26 letters are calculated <br> T: _O(n)_ S: _O(1)_ <br> For Unicode (Solution 3) <br> T: _O(n)_ <br> S: _O(U)_ U= # of unique UNICODE characters | 


## Analysis

### Time Complexity

The time complexity of each solution is analyzed and documented in the table above. The notation used for time complexity is Big O notation.

### Space Complexity

The space complexity of each solution is analyzed and documented in the table above. The notation used for space complexity is Big O notation.

# A tale of GIT
[Link](./Git_Documentation)

# A handy link of DocString (cmd + shift + 2)
[Docstring Extension and Details](https://github.com/NilsJPWerner/autoDocstring/tree/c9da64126fd9e667decd9d85b4e5b53c60372ea7?tab=readme-ov-file)

# Powerful Action Verbs for a Resume
Harvard action verbs are a curated list of powerful, descriptive verbs often recommended by career advisors and resume experts. These verbs are specifically chosen to help job seekers articulate their accomplishments and skills more effectively and vividly on their resumes and in interviews. By using these action verbs, individuals can present their experiences and achievements in a dynamic and impactful way, making it easier for employers to recognize their potential value and contributions to a role or organization. This approach aids in creating a more engaging and persuasive narrative about one's professional journey. You will find the action verbs in the following link.
[Action Verbs](https://www.alumni.hbs.edu/Documents/careers/ActionVerbsList.pdf)

# What to Sort and Not to Sort, That's the Question
[Link](./sorting)
## Contributing
Constructive criticism is welcome. I would appreciate your comments, feedback, and any other suggestions you may have.
