# Proposal for the Standard Block Comparison Method (SBCM) in the Quantitative Evaluation of Administrative Measures
**― A Study on Comparability Between Basic Municipalities Using the Budget Distortion Index ($D_{index}$) ―**

## Abstract
In modern public administration management, the setting of KPIs (Key Performance Indicators) has become mandatory. However, outcome figures announced by many local governments and national projects are often difficult to evaluate intuitively due to differences in their scale (the denominator). This study proposes the **"Standard Block Comparison Method (SBCM),"** a normalization method based on the basic municipality, which is the smallest unit of Japan's governing structure. This method makes it possible to compare local government measures and national projects of different population sizes using the same indicators: **Effectiveness Impact ($I$)** and **Budget Distortion Index ($D_{index}$)**. Applying this method to cases in Kashiwa City, Kyoto City, and the 2025 Osaka-Kansai Expo successfully quantitatively detected measures characterized by "high cost and low prevalence" (budgetary distortion), which had been overlooked in traditional financial accounting.

---

## 1. Introduction

### 1.1 Background of the Study
Macro figures announced by governments and large organizations, such as "cumulative users," "economic effects," and "budget amounts," often function as **"Vanity Metrics"** that conceal the reality. For example, an outcome of "3,000 users" may function as social infrastructure in a village of 1,000 people, but in a metropolis of 10 million, it is merely a statistical error.

### 1.2 Issues and Objectives
Existing administrative evaluation methods (such as cost-benefit analysis) are highly specialized, creating a high hurdle for citizens and assemblies to conduct intuitive audits. The objective of this study is to construct a framework that allows anyone to mathematically judge the effectiveness of measures and the validity of budget allocation by normalizing all administrative figures into **"Standard Block"** units.

## 2. Methodology

### 2.1 Definition of Basic Constants
In this method, the following constants are defined based on Japan's demographics and administrative structure:

*   **Total Population ($P_{total}$):** 124 million
*   **Number of Basic Municipalities ($N_{muni}$):** 1,718 entities

From these, the **"Standard Block ($B_{std}$),"** which is the population scale of a standard municipality, is derived as follows:

$$ B_{std} = \frac{P_{total}}{N_{muni}} \approx 72,176 \quad (\text{persons}) $$

### 2.2 Effectiveness Impact ($I$)
This indicator shows the degree of influence the outcome figure ($V$) of a measure has relative to the Standard Block. Assuming the target attribute ratio is $R$, the Impact $I$ is expressed by the following equation:

$$ I = \frac{V}{B_{std} \times R} $$

In this study, $I < 1.0$ (a state where not even one municipality is covered) is defined as **"Error Level,"** and $I \ge 172$ (national prevalence exceeding 10%) is defined as **"Infrastructure Level."**

### 2.3 Budget Distortion Index ($D_{index}$)
To evaluate the balance between "prevalence" and "budget" of a measure, the Budget Distortion Index is introduced. It is the ratio of Budget Impact ($I_{budget}$) to Coverage Impact ($I_{coverage}$).

$$ D_{index} = \frac{I_{budget}}{I_{coverage}} $$

*   $I_{budget}$: Budget input normalized by municipality scale
*   $I_{coverage}$: User reach normalized by municipality scale

$D_{index} \approx 1$ indicates appropriate infrastructure investment, while $D_{index} \gg 10$ indicates the existence of extremely low cost-effectiveness, or **"Distortion."**

## 3. Case Studies

This method was applied to analyze the following three cases.

### 3.1 Case 1: Feasibility of the 2025 Osaka-Kansai Expo
SBCM was applied to the "Visitor Target of 28.2 million" set by the government and the Japan Association for the 2025 World Exposition.

*   **Calculation Result:**
    $$ I_{visitors} = \frac{28,200,000}{1,718} \approx 16,414 \quad (\text{persons/block}) $$

*   **Discussion:**
    This figure suggests that every one of the 1,718 municipalities, from Hokkaido to Okinawa, must send an average of 16,414 residents to Osaka. This is a numerical target that ignores geographical and economic constraints, and from the perspective of SBCM, it is judged to be a **"politically impossible number."**

### 3.2 Case 2: Preconception Care Project in Kashiwa City
The introduction result (3,000 users) of a declining birthrate countermeasure app in a Core City (population 435,000) was verified. The scale factor of Kashiwa City ($S_{factor} \approx 6.03$) is taken into account.

*   **Calculation Result:**
    Assuming a target ratio of 15%, the impact was $I \approx 0.27$.

*   **Discussion:**
    Since $I < 1.0$, this measure is at an **"Error Level"** that does not even satisfy the capacity of a standard single municipality. The ripple effect on the city as a whole is negligible, and its effectiveness as a policy cannot be recognized.

### 3.3 Case 3: Fiscal Structure Analysis of Shiranuka Town, Hokkaido
The financial settlement of Shiranuka Town (population approx. 7,000), which collects huge donations through "Hometown Tax" (Furusato Nozei), was analyzed.

*   **Analysis:**
    For a municipality with a population scale factor of 0.1, the revenue is about 13 times the standard, while the ratio of "object expenses" (return gifts, shipping, etc.) is extremely high.
*   **Discussion:**
    SBCM financial analysis reveals that the town's structure is closer to a **"warehouse of a giant e-commerce company"** than a public administration. In particular, infrastructure investment per capita has reached 1.3 million JPY per year, creating **"future liabilities"** that cannot be maintained in a depopulating society (4th Quadrant: High Cost / Structural Distortion).

## 4. Discussion

### 4.1 Classification by Budget Portfolio Matrix
By plotting each project on a logarithmic graph with $I_{coverage}$ (x-axis) and $I_{budget}$ (y-axis), it was confirmed that administrative projects can be classified into four quadrants.

*   **1st Quadrant (Infrastructure Type):** Waste collection, road maintenance, etc. High cost, but used by everyone.
*   **2nd Quadrant (Innovation Type):** Internal DX, etc. Low cost, demonstrating broad effectiveness.
*   **4th Quadrant (Distortion Type):** "Hakomono" (White Elephant) administration and public awareness projects with low effectiveness. These are the primary targets for auditing using this method.

### 4.2 Limitations and Challenges
Since this method specializes in quantitative evaluation, it may not be suitable for the qualitative evaluation of measures related to **"Social Inclusion,"** such as cultural projects and livelihood protection. These need to be managed separately as "social costs."

## 5. Conclusion

The Standard Block Comparison Method (SBCM) proposed in this study has made it possible to compare events of different scales by providing a common language of **"Standard Basic Municipality"** in the evaluation of administrative measures.
In particular, the introduction of the **Budget Distortion Index ($D_{index}$)** enables the immediate screening of "4th Quadrant" projects with low ROI without being misled by superficial numbers. The implementation of this framework is expected to accelerate **EBPM (Evidence-Based Policy Making)** and contribute to sustainable administrative and fiscal management.

## References
1. Melnus. (2025). Standard-Block-Comparison-Method. GitHub Repository.
2. Ministry of Internal Affairs and Communications. (2024). Population, Demographics and Number of Households based on the Basic Resident Register.
3. Kashiwa City. (2024). FY2024 Kashiwa City Revenue and Expenditure Settlement.
4. Kyoto City Finance Bureau. (2025). FY2024 Settlement Overview.
5. Japan Association for the 2025 World Exposition. (2023). Master Plan.
