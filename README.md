# carnegie test
 
## <a id="toc-table-of-contents"></a> Table of Contents:
------
- [Introduction](#toc-introduction)
- [Required Modules](#toc-reqs)
- [How to Run](#toc-how-to-run)


## <a id="toc-introduction"></a>Introduction: 

This code solution was written using Python 3. 

## <a id="toc-reqs"></a>Required Modules (requirements.txt): 

No special modules were required.

## <a id="toc-how-to-run"></a>How to Run: 

```python3 main.py```

## <a id="toc-problem-statement"></a>Problem: 

Picking the Next Problem

Implement a system that chooses the next problem for a student to work on by examining “skills”. Each skill has a unique name. Each student has a set of skills that she is working on. For each of these skills, the student has a current score (a number between 0% and 100%). Each problem has a unique name and a list of skills that it exercises (i.e., skills for which a student’s score will increase or decrease as a result of working on the problem).

The system should take a student and a set of problems as input and return the most appropriate next problem for that student. There is guaranteed to be at least one problem that exercises each student skill. Problems may exercise more than one student skill, and may include skills that are not in the student’s set of skills.

For example, a problem like “simplify 1/2 - 3.4” would have skills like “subtract-fractions” and “subtract-decimals”. A problem like “graph the equation y=3x+4” would have skills like “plot-y-intercept” and “determine-slope”.

There are several possible heuristics for deciding which problem is most appropriate. For this exercise, implement the following heuristic: Choose a problem that exercises the most student skills whose scores are below a certain threshold (say, 95%).

Consider the following example data:

prob1, with skills: {add-decimals}
prob2, with skills: {add-decimals, multiply-decimals}
prob3, with skills: {add-fractions}
prob4, with skills: {add-fractions, multiply-fractions}
prob5, with skills: {multiply-decimals, multiply-fractions}
prob6, with skills: {add-fractions, add-decimals}
A student with scores {add-decimals=97%, add-fractions=17%, multiply-fractions=53%} should get prob4.

A student with scores {add-fractions=96%, multiply-fractions=81%, add-decimals=33%, multiply-decimals=47%} should get prob2 or prob5.

A student with scores {add-fractions=23%} should get prob3, prob4, or prob6.