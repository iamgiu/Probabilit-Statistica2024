# 1. Statistical Analysis Scripts Repository

This repository contains a collection of Python scripts for various statistical analysis techniques used in data science and research. The scripts demonstrate implementations of hypothesis testing, regression analysis, ANOVA, confidence intervals, and other statistical methods.

# 2. Contents

## 2.1 Hypothesis Testing
- `Esercizio_ipotesi1.py` - One-sample t-test implementation
- `testipotesi_t.py` - Single sample t-test with critical value and p-value approaches
- `testipotesi_z.py` - Z-test implementation with critical value and p-value approaches
- `esercizio5.py` - Two-sample t-test implementation
- `esercizio6.py` - Mann-Whitney U test implementation
- `test_dei_segni.py` - Sign test for paired samples
- `tablet.py` - Simple t-distribution calculation

## 2.2 Regression Analysis
- `Esercizio_regressione1.py` - Simple linear regression implementation
- `intervallo_di_confidenza_regressione.py` - Linear regression with confidence intervals
- `intervallo_di_predizione_regressione.py` - Linear regression with prediction intervals

## 2.3 ANOVA (Analysis of Variance)
- `anova.py` - One-way ANOVA implementation for equal group sizes
- `anova2.py` - One-way ANOVA implementation for unequal group sizes

## 2.4 Confidence Intervals
- `esercizio4.py` - Confidence interval calculation with t-distribution
- `stima_verosimile.py` - Maximum likelihood estimation and confidence intervals

# 3. Requirements

These scripts require the following Python packages:
- numpy
- scipy.stats
- math

# 4. Usage

Each script can be run independently. Most scripts contain example data and will produce statistical outputs when executed. For example:

```bash
python testipotesi_t.py
```

This will perform a t-test with the predefined example data and print the results, including the test statistic, critical value, p-value, and decision regarding the null hypothesis.

# 5. Example Data

Many scripts include example datasets that demonstrate the statistical technique being implemented. These examples can be modified or replaced with your own data.

# 6. Notes

- These scripts are primarily for educational purposes to understand statistical concepts.
- The code includes detailed calculations and intermediate steps to help understand the statistical processes.
- Comments in Italian are present in some files to explain the statistical concepts.
