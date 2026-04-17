Daily Python practice log: Solving 3 logic problems every day ro sharpen my coding skills. This repository tracks my journey to automation mastery, one script at a time.

## Day 1 - Problem Solving 
14-Apr-2026

**1. Valid Anagram** -> Sorting approach (O(n log n))

**2. Group Anagrams** -> HashMap + sorted key (O(n*k log k))

**3. Longest Consecutive Sequence** -> Set-based O(n) solution

## Day 2 - Sliding Window
17-Apr-2026

**1. Longest Substring Without Repeating Characters**

    - Applied Variable Window with set()
    - Understood expand + shrink logic

**2. Maximum Sum Subarray of Size k**

    - Applied Fixed Sliding Window
    - Opimized sum calculation using window shift

**3. Minimum Size Subarray Sum**

    - Practiced shrinking window to find minimum length
    - Strengthened condition-based window handling

**Key Learnings**

- Sliding window has **two main patterns**:
  - Fixed Window -> size remains same
  - Variable Window -> expands and shrinks based on conditions

- Core Formula:

    new_sum = old_sum - outgoing + incoming

- Important Concept:
    - Expand window -> increase sum
    - Shrink window _> optimize result

- **Time Complexity**

    All problems are optimized to:
  - O(n) time
  - O(1) / O(n) space depending on the data structure used