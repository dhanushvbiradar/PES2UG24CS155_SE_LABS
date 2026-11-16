# Lab 5: Static Code Analysis — Reflection

## 1. What is static code analysis, and why is it useful?

Static code analysis examines source code without executing the program to identify potential bugs, security vulnerabilities, and coding-style violations. In this lab, Pylint helped identify code-quality problems, Flake8 detected formatting and style violations, and Bandit identified potentially unsafe coding practices. These tools help developers detect problems early and improve code maintainability.

## 2. What security issues were identified, and how were they fixed?

Bandit identified three security concerns in the original program: SQL injection risk caused by constructing SQL queries using string formatting, weak MD5 hashing, and possible command injection through `os.system()`. I replaced the SQL construction with parameterised queries, replaced MD5 token generation with Python's `secrets` module, and removed shell execution in favour of Python's `print()` function. After making these changes, Bandit reported no issues in the updated program.

## 3. How did Pylint and Flake8 improve the code?

Pylint identified problems such as missing docstrings, inconsistent function naming, unused imports, and an unused function argument. Flake8 detected style violations, including excessive line lengths, an ambiguous variable name, an unused import, and an incorrect comparison with `None`. I corrected these issues by improving naming, adding docstrings, removing unused code, and following Python's formatting conventions. The final Pylint score was 10.00/10, and the Flake8 report was empty.

## 4. What did I learn from this lab?

I learned that a program producing the expected output does not necessarily mean its code is secure, maintainable, or well-formatted. Different static analysis tools identify different categories of problems, so using Pylint, Bandit, and Flake8 together provides broader coverage. I also learned the importance of rerunning the tools after fixing issues to verify that the changes resolved the reported findings.
