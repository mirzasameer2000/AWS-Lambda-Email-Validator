# AWS-Lambda-Email-Validator

An **AWS Lambda (Python 3.13)** email format validator built in **AWS Academy Learner Lab (Arden University)** using **Amazon Q Developer** inside the **Lambda code editor**.  
It validates a single email or runs **batch validation** using `testCases`, returning a structured JSON summary.

---

## Project Overview

This project was created as part of a lab to:

- Set up an **AWS Lambda environment** in AWS Academy Learner Lab
- Use the **AWS Lambda code editor** with **Amazon Q Developer** (inline suggestions + function generation)
- Implement email format validation using a **regular expression (regex)**
- Create and run **Lambda test events** in the AWS Console

---

## Features

✅ Validates an email address format using regex  
✅ Supports **two input formats**:
- **Single email**: `{"email": "user@example.com"}`
- **Batch tests**: `{"testCases": [{"name": "...", "email": "..."}]}`

✅ Batch mode returns:
- Total tests
- Passed / failed counts
- Per-test PASS/FAIL results

---

## Tech Stack

- **AWS Lambda**
- **Python 3.13**
- **Amazon Q Developer** (Lambda editor auto-suggestions)
- **Regex** for validation
- JSON request/response handling

---

## AWS Lab Setup (What I did)

### Task 1 — Creating an AWS Lambda environment

1. Start **AWS Academy Learner Lab**.
2. Open **AWS Management Console** (AWS link above terminal window).
3. Search **Lambda** and open the service.
4. Confirm region: **N. Virginia (us-east-1)**.
5. Choose **Create function** and configure:

- **Function name:** `myFunction` (or any name)
- **Runtime:** `Python 3.13`
- **Architecture:** `x86_64`
- **Permissions:** Change default execution role  
  - **Execution role:** Use an existing role  
  - **Existing role:** `LabRole`

6. Choose **Create function**.

✅ In the Lambda code editor, **Amazon Q Developer** runs as an extension and provides auto-suggestions.

---

### Task 2 — Exploring Amazon Q Developer full function generation

Inside `lambda_function.py`, Amazon Q Developer was used to help generate/refactor functions using comments/signatures.  
The function validates email format using a **regex pattern**, and the handler supports both single and batch test events.

---

## How It Works

### 1) Batch mode (`testCases`)

If the event contains `testCases`, the function:
- Validates each email
- Builds a result entry with PASS/FAIL
- Returns a JSON response with a **summary** and **results**

### 2) Single mode (`email`)

If the event contains `email`, the function:
- Validates the email
- Returns:
  - `statusCode: 200` if valid  
  - `statusCode: 400` if invalid

---

## Test Events

### A) Single email test (Lab requirement)

Create a test event in Lambda:

- **Event Name:** `TestEmail`
- **Event JSON:**

```json
{
  "email": "user@example.com"
}
