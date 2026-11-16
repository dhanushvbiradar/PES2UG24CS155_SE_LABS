# Lab 5 — Static Code Analysis Issues

**Project:** Dairy Milk Collection Ledger
**File:** `dairy_collection.py`
**Stage:** Original code — before fixes

## 1. Pylint Report

```text
************* Module dairy_collection
dairy_collection.py:7:0: C0301: Line too long (104/100) (line-too-long)
dairy_collection.py:11:0: C0301: Line too long (124/100) (line-too-long)
dairy_collection.py:1:0: C0114: Missing module docstring (missing-module-docstring)
dairy_collection.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
dairy_collection.py:10:0: C0103: Function name "recordMilk" doesn't conform to snake_case naming style (invalid-name)
dairy_collection.py:10:15: W0621: Redefining name 'conn' from outer scope (line 6) (redefined-outer-name)
dairy_collection.py:11:17: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dairy_collection.py:15:0: C0116: Missing function or method docstring (missing-function-docstring)
dairy_collection.py:15:0: C0103: Function name "farmerToken" doesn't conform to snake_case naming style (invalid-name)
dairy_collection.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
dairy_collection.py:19:0: C0103: Function name "dailyTotal" doesn't conform to snake_case naming style (invalid-name)
dairy_collection.py:19:15: W0621: Redefining name 'conn' from outer scope (line 6) (redefined-outer-name)
dairy_collection.py:21:11: C0209: Formatting a regular string which could be an f-string (consider-using-f-string)
dairy_collection.py:24:0: C0116: Missing function or method docstring (missing-function-docstring)
dairy_collection.py:24:0: C0103: Function name "topFarmer" doesn't conform to snake_case naming style (invalid-name)
dairy_collection.py:24:14: W0621: Redefining name 'conn' from outer scope (line 6) (redefined-outer-name)
dairy_collection.py:30:0: C0116: Missing function or method docstring (missing-function-docstring)
dairy_collection.py:30:0: C0103: Function name "printSlip" doesn't conform to snake_case naming style (invalid-name)
dairy_collection.py:34:0: C0116: Missing function or method docstring (missing-function-docstring)
dairy_collection.py:34:0: C0103: Function name "lowFat" doesn't conform to snake_case naming style (invalid-name)
dairy_collection.py:34:11: W0621: Redefining name 'conn' from outer scope (line 6) (redefined-outer-name)
dairy_collection.py:36:36: C0121: Comparison 'fat == None' should be 'fat is None' (singleton-comparison)
dairy_collection.py:39:0: C0116: Missing function or method docstring (missing-function-docstring)
dairy_collection.py:2:0: W0611: Unused import json (unused-import)

-----------------------------------
Your code has been rated at 2.00/10


## 2. Bandit Report

```text
py : [main]	INFO	profile include tests: None
At line:1 char:1
+ py -m bandit -r dairy_collection.py > bandit_report.txt 2>&1
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : NotSpecified: ([main]	INFO	profile include tests: None:String) [], Remo 
   teException
    + FullyQualifiedErrorId : NativeCommandError
 
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.13.0
Run started:2026-10-14 06:01:50.889776+00:00

Test results:
>> Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
   Severity: Medium   Confidence: Medium
   CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b608_hardcoded_sql_expressions.html
   Location: .\dairy_collection.py:11:17
10	def recordMilk(conn, farmer, litres, fat, day):
11	    conn.execute("INSERT INTO milk (farmer, litres, fat, day) VALUES ('{}', {}, {}, '{}')".format(farmer, litres, fat, day))
12	    conn.commit()

--------------------------------------------------
>> Issue: [B324:hashlib] Use of weak MD5 hash for security. Consider usedforsecurity=False
   Severity: High   Confidence: High
   CWE: CWE-327 (https://cwe.mitre.org/data/definitions/327.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b324_hashlib.html
   Location: .\dairy_collection.py:16:11
15	def farmerToken(farmer):
16	    return hashlib.md5(farmer.encode()).hexdigest()
17	

--------------------------------------------------
>> Issue: [B605:start_process_with_a_shell] Starting a process with a shell, possible injection detected, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   More Info: https://bandit.readthedocs.io/en/1.9.4/plugins/b605_start_process_with_a_shell.html
   Location: .\dairy_collection.py:31:4
30	def printSlip(farmer):
31	    os.system("echo printing slip for " + farmer)
32	

--------------------------------------------------

Code scanned:
	Total lines of code: 30
	Total lines skipped (#nosec): 0
	Total potential issues skipped due to specifically being disabled (e.g., #nosec BXXX): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0
		Low: 0
		Medium: 1
		High: 2
	Total issues (by confidence):
		Undefined: 0
		Low: 0
		Medium: 1
		High: 2
Files skipped (0):

## 3. Flake8 Report

```text
dairy_collection.py:2:1: F401 'json' imported but unused
dairy_collection.py:7:80: E501 line too long (104 > 79 characters)
dairy_collection.py:11:80: E501 line too long (124 > 79 characters)
dairy_collection.py:20:80: E501 line too long (83 > 79 characters)
dairy_collection.py:25:80: E501 line too long (90 > 79 characters)
dairy_collection.py:26:5: E741 ambiguous variable name 'l'
dairy_collection.py:36:41: E711 comparison to None should be 'if cond is None:'

## 4. Detailed Issue Analysis

The original findings are reproduced above. For each finding, document its severity, meaning, and fix in the issue table below.

| Issue / Error Code | Type / Severity | Line(s) | Description | Fix Approach |
|---|---|---|---|---|
