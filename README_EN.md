# Standard Block Comparison Method

**An auditing framework to break free from "number magic" and measure the true effectiveness of administrative measures.**

## Overview
Huge figures announced by governments and corporations, such as "cumulative total of X people" or "budget of Y billion yen," are often used to obscure the reality (ROI).
This repository provides the "Standard Block Comparison Method," a technique to mathematically determine whether a measure functions as social infrastructure or is merely a statistical "error" by breaking these numbers down to the smallest unit: the "Standard Block" (Basic Municipality).

This method applies the concept of Fermi estimation, using the number of basic municipalities in Japan (approx. 1,700) as a constant to calculate an index (Administrative Density) that allows anyone to intuitively grasp the scale of a project.

## Purpose
*   **DX of Administrative Auditing:** Conducting logical administrative evaluations based on formulas rather than emotions.
*   **Visualization of Scale:** Converting enormous numbers into a "life size" (capacity per municipality) that citizens can actually feel.
*   **Contribution to Civic Tech:** Publishing a universally verifiable evaluation format as open source.

## The Formula

The Effectiveness Impact ($I$) of an administrative measure is defined by the following formula:

$$ I = \frac{V}{B} $$

Here, the Standard Block ($B$) is calculated as follows:

$$ B = \frac{P \times R}{N} $$

### Definitions
*   $P$ (Population): Total population of Japan (approx. 124 million *as of 2023 estimates*)
*   $R$ (Ratio): Ratio of the target attribute (e.g., 1.0 for total population, 0.15 for young adults, etc.)
*   $N$ (Number): Total number of basic municipalities in Japan (approx. 1,718)
*   $V$ (Value): Announced outcome figure (e.g., cumulative 3,000 users, 10 billion yen budget)
*   $B$ (Block): Standard Block (Average target number per municipality)
*   $I$ (Impact): Effectiveness Impact
*   
### Criteria (v2.0)
The calculated Impact value ($I$) represents how many of Japan’s 1,718 municipalities could be fully covered by the measure. Based on this, the "Social Implementation Stage" is judged.

| Impact Value ($I$)     | Estimated Coverage Rate | Verdict           | Benchmark / Meaning |
|------------------------|--------------------------|-------------------|----------------------|
| **$I < 1.0$**          | Less than 0.05%          | **Error Level**   | Out of scope. Cannot even cover one standard municipality. |
| **$1.0 ≤ I < 17$**     | Less than 1%             | **Localized**     | Experimental phase. Not even reaching early adopters. |
| **$17 ≤ I < 172$**     | 1%–10%                   | **Penetration**   | “One per classroom” level. Awareness is beginning to spread. |
| **$172 ≤ I < 859$**    | 10%–50%                  | **Infrastructure**| “One in ten” level. Becoming a foundational public service. |
| **$I ≥ 859$**          | Over 50%                 | **Social OS**     | Majority adoption. A prerequisite for modern society. |

## Case Studies

### 1. Kashiwa City, Chiba Pref.: Preconception Care Project
*   **Link:** [Read full analysis: Kashiwa (JP)](reports/kashiwa_report_2025.md)
*   **Context:** The city introduced apps and services in collaboration with private companies as a "countermeasure against the declining birthrate."
*   **Announced Figure ($V$):** 3,000 users
*   **Target Ratio ($R$):** 0.15 (Assumed women of reproductive age)
*   **Standard Block ($B$):** $124,000,000 \times 0.15 \div 1,718 \approx 10,826$ people
*   **Analysis Result ($I$):** $3,000 \div 10,826 \approx$ **0.27**
*   **Conclusion:** Calculated nationally, this equates to only "0.3 users per municipality." The penetration rate as a policy is at a **"margin of error"** level.

### 2. Osaka-Kansai Expo: Visitor Target
*   **Link:** [Read full analysis: Osaka-Kansai Expo 2025](reports/osaka_expo_analysis_en.md)
*   **Context:** Visitor target for the Expo scheduled for 2025.
*   **Announced Figure ($V$):** 28.2 million people
*   **Target Ratio ($R$):** 1.0 (Total population)
*   **Standard Block ($B$):** $124,000,000 \times 1.0 \div 1,718 \approx 72,176$ people
*   **Analysis Result ($I$):** $28,200,000 \div 72,176 \approx$ **390**
*   **Interpretation:** While this figure gives an Impact of 390, paradoxically it suggests a logistical unreality: "An average of 16,000 people per municipality must be mobilized (including repeats during the period)" to achieve this goal.

## Usage
### 1. Python Script (For Engineers)

You can easily verify numbers at hand using the Python script included in this repository.

### Requirements
*   Python 3.6+

### Execution Commands
```bash
# Example: Verifying headcount (3,000 people, target ratio 100%)
python methodology/block_calculator.py --value 3000 --target_ratio 1.0

# Example: Verifying budget (10 billion yen, target ratio 100%)
python methodology/block_calculator.py --value 10000000000 --target_ratio 1.0
```

### 2. Google Sheets (For Everyone)
You can use this method without coding skills.
Copy the code from `methodology/google_sheets_script.js` into your Google Sheet's "Extensions > Apps Script".

**Formulas:**
*   Calculate Score: `=IMPACT_SCORE(Value, TargetRatio)`
*   Get Verdict: `=IMPACT_VERDICT(Score)`
