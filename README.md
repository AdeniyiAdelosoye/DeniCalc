# ✦ DeniCalc ✦
### Powerful Scientific Calculator

**DeniCalc** is a Python-based desktop scientific calculator developed using Tkinter. It supports everyday arithmetic, advanced mathematical expressions, scientific functions, fraction conversion, and complex combinations of mathematical operations.

Developed by **Adeniyi Adelosoye**.

## Features

### 1. Basic Arithmetic

DeniCalc supports addition, subtraction, multiplication, division, decimal calculations, modulo (remainder), and parentheses.

| Expression | Result |
|---|---:|
| `25+17` | 42 |
| `100÷4` | 25 |
| `(15+5)×3` | 60 |
| `17%5` | 2 |
| `7×8-6` | 50 |

The calculator follows standard mathematical operator precedence.

**Note:** The `%` operator calculates the remainder after division rather than automatically converting a number into a percentage.

### 2. Trigonometric Functions

Trigonometric calculations operate in **degrees (DEG)**.

Supported functions:

- `sin(x)` — Sine
- `cos(x)` — Cosine
- `tan(x)` — Tangent
- `sec(x)` — Secant
- `cosec(x)` — Cosecant
- `cot(x)` — Cotangent
- `atan(x)` — Inverse tangent, returning degrees

| Expression | Result |
|---|---:|
| `sin(30)` | 0.5 |
| `cos(60)` | 0.5 |
| `tan(45)` | 1 |
| `sec(60)` | 2 |
| `cosec(30)` | 2 |
| `atan(1)` | 45 |

### 3. Hyperbolic Functions

DeniCalc includes:

- `sinh(x)` — Hyperbolic sine
- `cosh(x)` — Hyperbolic cosine

These functions use radian-based arguments, consistent with Python's mathematical library.

### 4. Powers and Exponents

Supported operations include:

- Squaring (`x²`)
- Cubing (`x³`)
- Custom exponentiation (`xʸ`)
- Positive and negative exponents
- Decimal exponents
- Superscript notation for integer powers

| Expression | Result |
|---|---:|
| `5²` | 25 |
| `4³` | 64 |
| `2¹⁰` | 1024 |
| `2⁻³` | 0.125 |
| `9^(0.5)` | 3 |

The custom exponent button provides a separate exponent-entry field.

### 5. Roots and Radicals

DeniCalc supports:

- `√` — Square root
- `³√` — Cube root
- `⁴√` — Fourth root
- `⁵√` — Fifth root
- `root(x,n)` — General nth-root evaluation through the expression parser

| Expression | Result |
|---|---:|
| `√(144)` | 12 |
| `³√(125)` | 5 |
| `⁴√(81)` | 3 |
| `⁵√(32)` | 2 |
| `³√(-27)` | -3 |

The evaluator rejects unsupported real-number root operations, such as even roots of negative numbers.

### 6. Logarithms

Supported logarithmic functions:

- `log(x)` — Base-10 logarithm
- `ln(x)` — Natural logarithm

| Expression | Result |
|---|---:|
| `log(1000)` | 3 |
| `log(100)` | 2 |
| `ln(1)` | 0 |

### 7. Factorials

The factorial function calculates the product of positive integers up to a specified non-negative integer.

| Expression | Result |
|---|---:|
| `fact(5)` | 120 |
| `fact(7)` | 5040 |
| `fact(0)` | 1 |

The `x!` button inserts the factorial function.

### 8. Permutations and Combinations

DeniCalc supports combinatorial calculations:

- `nPr(n,r)` — Permutations, where arrangement order matters
- `nCr(n,r)` — Combinations, where arrangement order does not matter

| Expression | Result |
|---|---:|
| `nPr(5,2)` | 20 |
| `nCr(5,2)` | 10 |
| `nCr(10,3)` | 120 |
| `nPr(6,3)` | 120 |

A dedicated comma button separates function arguments.

### 9. Fraction Calculations and Conversion

The `a/b` button inserts a division separator for entering fractions.

Examples include:

- `1/2`
- `5/6`
- `1/2+1/4`
- `(2/3)×(3/4)`

The `S⇔D` button switches between decimal and simplified fractional representations when a sufficiently accurate simple fraction is available.

**Example:**

1. Enter `1/2+1/4`.
2. Press `=`.
3. DeniCalc displays `0.75`.
4. Press `S⇔D` to display `3/4`.
5. Press `S⇔D` again to return to `0.75`.

Fraction conversion uses Python's `fractions.Fraction` with a maximum simplified denominator of 1000.

### 10. Mathematical Constants

Supported constants:

- `pi` — Pi (π)
- `e` — Euler's number

These can be used in expressions alongside other supported mathematical operations.

### 11. Scientific Notation

The `×10ˣ` button supports expressions involving powers of ten.

| Expression | Result |
|---|---:|
| `2×10^(3)` | 2000 |
| `5×10^(-2)` | 0.05 |
| `3×10^(4)` | 30000 |

### 12. Reciprocal and Absolute Value

Supported operations:

- `1/x` — Reciprocal
- `abs(x)` — Absolute value

| Expression | Result |
|---|---:|
| `1/4` | 0.25 |
| `abs(-25)` | 25 |

The reciprocal button can wrap an existing expression in `1/(...)`.

### 13. Advanced Mathematical Expression Evaluation

DeniCalc can evaluate mathematical expressions combining multiple functions, parentheses, exponentiation, roots, trigonometry, logarithms, factorials, and combinatorial operations.

**The following advanced expressions were verified during project testing:**

| # | Expression | Result |
|---|---|---:|
| 1 | `2(3+4)²+fact(5)` | 218 |
| 2 | `nCr(10,3)+nPr(5,2)` | 140 |
| 3 | `³√(125)+⁴√(16)+⁵√(32)` | 9 |
| 4 | `sin(30)²+cos(30)²` | 1 |
| 5 | `3(2+5)+4sin(30)` | 23 |
| 6 | `√(81)+fact(4)÷3` | 17 |
| 7 | `(5²+3³)÷2` | 26 |
| 8 | `log(1000)+ln(1)+2³` | 11 |
| 9 | `nCr(10,3)×2+√(144)` | 252 |
| 10 | `(sin(30)+cos(60))×10³` | 1000 |
| 11 | `fact(5)÷(3²+1)` | 12 |
| 12 | `2(3+4)²+³√(125)×fact(3)` | 128 |

These tests demonstrate support for nested and combined mathematical operations, implicit multiplication, operator precedence, and advanced scientific functions.

### 14. Implicit Multiplication

DeniCalc recognizes certain expressions where multiplication is mathematically implied.

Examples:

- `2(3+4)`
- `4sin(30)`
- `2pi`

The application uses regular expressions to normalize supported forms of implicit multiplication before evaluation.

### 15. Previous Answer Memory

The `ANS` button allows users to reuse the result of a previous successful calculation.

For example:

- Calculate `25×4`, obtaining 100.
- Enter `ANS+50`.
- The new result is 150.

### 16. Input Controls

| Button | Function |
|---|---|
| `AC` | Clears the current expression and result |
| `⌫` | Deletes a character |
| `=` | Evaluates the expression |
| `ANS` | Reuses the previous answer |
| `a/b` | Inserts a fraction/division separator |
| `S⇔D` | Toggles decimal and fractional representations |
| `,` | Separates arguments in multi-argument functions |
| `xʸ` | Opens custom exponent input |

The Enter key can also be used to evaluate expressions.

### 17. Input Validation and Error Handling

DeniCalc includes safeguards for:

- Division by zero
- Invalid mathematical expressions
- Unsupported mathematical functions
- Incorrect numbers of function arguments
- Invalid factorial inputs
- Invalid permutation and combination inputs
- Unsupported root operations
- Excessively large exponent inputs
- Non-finite mathematical results

Invalid expressions display an error message instead of terminating the application under the handled error conditions.

## How DeniCalc Works

DeniCalc uses Python's **Abstract Syntax Tree (AST)** module to parse and evaluate mathematical expressions.

Rather than executing user input through unrestricted Python `eval()`, the application evaluates a defined set of supported mathematical operators, functions, and constants.

Regular expressions normalize mathematical notation, including multiplication symbols, roots, superscript exponents, and implicit multiplication.

The application combines this expression-processing system with a Tkinter graphical user interface.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Tkinter | Desktop graphical interface |
| math | Mathematical functions and constants |
| ast | Expression parsing and controlled evaluation |
| re | Expression normalization and pattern matching |
| fractions | Fraction representation and conversion |

All listed modules are part of Python's standard library.

## Installation

**Requirements:** Python 3.8 or newer, with Tkinter available.

1. Clone the repository:

```bash
git clone https://github.com/AdeniyiAdelosoye/DeniCalc.git
```

2. Navigate into the project directory:

```bash
cd DeniCalc
```

3. Run the calculator:

```bash
python denicalc.py
```

On some systems, use `python3 denicalc.py`.

No third-party Python packages are required.

## Limitations

- Trigonometric functions operate in degree mode without a separate DEG/RAD switch.
- Non-integer results are displayed rounded to four decimal places.
- Fraction conversion uses a limited-denominator approximation.
- Complex-number arithmetic is not generally supported.
- Certain calculations are subject to floating-point precision limitations.
- The application requires a compatible desktop environment with Tkinter support.
- It is not a symbolic algebra system and does not perform symbolic differentiation or integration.

## Project Purpose

DeniCalc was developed to strengthen practical software development skills through a functional Python desktop application.

The project demonstrates experience with:

- Graphical user interface development
- Mathematical computation
- Expression parsing and evaluation
- Input validation and exception handling
- Python standard-library modules
- Function-based application architecture
- Testing and debugging
- User-focused application design

## Author

**Adeniyi Adelosoye**

Software Engineering | Python Development

**GitHub:** https://github.com/AdeniyiAdelosoye

**LinkedIn:** https://www.linkedin.com/in/adeniyi-adelosoye-9990b7315
