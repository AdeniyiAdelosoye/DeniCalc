import tkinter as tk
import math
import re
import ast
from fractions import Fraction

SUPERSCRIPTS = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")

NORMAL_DIGITS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻", "0123456789-")

power_entry_active = False
exponent_base_position = None
last_answer = None
just_calculated = False
fraction_view = False


root = tk.Tk()
root.title("DeniCalc | Scientific Calculator")
root.geometry("950x850")
root.minsize(750, 600)
root.configure(bg="#2f3542")

brand_label = tk.Label(
    root,
    text="✦ DeniCalc ✦",
    font=("Segoe UI", 30, "bold"),
    bg="#2f3542",
    fg="#00E5FF"
)
brand_label.pack(pady=(12, 0))

brand_subtitle = tk.Label(
    root,
    text="POWERFUL SCIENTIFIC CALCULATOR",
    font=("Segoe UI", 10, "bold"),
    bg="#2f3542",
    fg="#FFD166"
)
brand_subtitle.pack(pady=(0, 4))

header = tk.Label(
    root,
    text="Enter your expression:",
    font=("Arial", 14, "bold"),
    bg="#2f3542",
    fg="#f1f2f6"
)
header.pack(pady=(4, 8))

mode_label = tk.Label(
    root,
    text="SCIENTIFIC MODE  |  Trigonometry: Degrees (DEG)",
    font=("Arial", 10),
    bg="#2f3542",
    fg="#a4b0be"
)
mode_label.pack(pady=2)

entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=70,
    bd=3,
    relief="flat",
    justify="center"
)
entry.pack(pady=5)

exponent_entry = tk.Entry(
    entry,
    font=("Arial", 10, "bold"),
    width=5,
    justify="center",
    bd=0,
    relief="flat",
    bg="#eaf2ff",
    fg="#1e40af",
    insertbackground="#1e40af",
    highlightthickness=1,
    highlightbackground="#93c5fd",
    highlightcolor="#2563eb"
)

exponent_entry.place_forget()

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="#2f3542"
)
result_label.pack(pady=10)

def safe_factorial(x):
    if x < 0 or x != int(x) or x > 170:
        raise ValueError("Invalid factorial")

    return math.factorial(int(x))

def safe_npr(n, r):
    if n != int(n) or r != int(r):
        raise ValueError("Use whole numbers")

    n, r = int(n), int(r)

    if n < 0 or r < 0 or r > n or n > 170:
        raise ValueError("Invalid permutation")

    return math.perm(n, r)


def safe_ncr(n, r):
    if n != int(n) or r != int(r):
        raise ValueError("Use whole numbers")

    n, r = int(n), int(r)

    if n < 0 or r < 0 or r > n or n > 170:
        raise ValueError("Invalid combination")

    return math.comb(n, r)


def safe_nth_root(x, n):
    if n != int(n) or n < 1 or n > 100:
        raise ValueError("Invalid root degree")

    n = int(n)

    if x < 0:
        if n % 2 == 0:
            raise ValueError("Even root of negative number")

        return -((-x) ** (1 / n))

    return x ** (1 / n)

FUNCTIONS = {
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "sec": lambda x: 1 / math.cos(math.radians(x)),
    "cosec": lambda x: 1 / math.sin(math.radians(x)),
    "cot": lambda x: 1 / math.tan(math.radians(x)),
    "atan": lambda x: math.degrees(math.atan(x)),
    "sqrt": math.sqrt,
    "abs": abs,
    "log": math.log10,
    "ln": math.log,
    "fact": safe_factorial,
    "sinh": math.sinh,
    "cosh": math.cosh,
    "nPr": safe_npr,
    "nCr": safe_ncr,
    "root": safe_nth_root,
}

CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}

OPERATORS = {
    ast.Add: lambda a, b: a + b,
    ast.Sub: lambda a, b: a - b,
    ast.Mult: lambda a, b: a * b,
    ast.Div: lambda a, b: a / b,
    ast.Pow: lambda a, b: a ** b,
    ast.Mod: lambda a, b: a % b,
}


def evaluate_node(node):
    if isinstance(node, ast.Constant):
        if type(node.value) in (int, float):
            return node.value
        raise ValueError("Invalid constant")

    if isinstance(node, ast.BinOp):
        operation = OPERATORS.get(type(node.op))
        if operation is None:
            raise ValueError("Unsupported operator")

        left = evaluate_node(node.left)
        right = evaluate_node(node.right)

        if isinstance(node.op, ast.Pow) and abs(right) > 100:
            raise ValueError("Exponent too large")

        return operation(left, right)

    if isinstance(node, ast.UnaryOp):
        value = evaluate_node(node.operand)

        if isinstance(node.op, ast.USub):
            return -value

        if isinstance(node.op, ast.UAdd):
            return value

    if isinstance(node, ast.Name):
        if node.id in CONSTANTS:
            return CONSTANTS[node.id]

    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise ValueError("Invalid function")

        function = FUNCTIONS.get(node.func.id)

        if function is None or node.keywords:
            raise ValueError("Unsupported function")

        expected_args = 2 if node.func.id in ("nPr", "nCr", "root") else 1

        if len(node.args) != expected_args:
            raise ValueError("Incorrect number of arguments")

        arguments = [evaluate_node(arg) for arg in node.args]

        return function(*arguments)

    raise ValueError("Invalid expression")


def evaluate_expression(expression):
    expression = re.sub(
        r"([⁰¹²³⁴⁵⁶⁷⁸⁹]+)√\(([^()]*)\)",
        lambda m: (
            f"root({m.group(2)},"
            f"{m.group(1).translate(NORMAL_DIGITS)})"
        ),
        expression
    )
    expression = expression.replace("√(", "sqrt(")

    expression = expression.replace("×", "*").replace("÷", "/")
    expression = expression.replace("^", "**")
    expression = re.sub(
        r"([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)",
        lambda match: "**" + match.group(1).translate(NORMAL_DIGITS),
        expression
    )
    expression = expression.replace("π", "pi")


    expression = re.sub(r"(\d|\))(?=\()", r"\1*", expression)
    expression = re.sub(
        r"(\d|\))(?=(?:sin|cos|tan|sec|cosec|cot|atan|sqrt|pi|e|log|ln|fact|abs|sinh|cosh|nPr|nCr|root)\b)",
        r"\1*",
        expression
    )
    expression = re.sub(r"\b(pi|e)(?=\()", r"\1*", expression)

    tree = ast.parse(expression, mode="eval")
    result = evaluate_node(tree.body)

    if isinstance(result, complex) or not math.isfinite(result):
        raise ValueError("Result is not finite")

    return result


def calculate():
    global last_answer, just_calculated, fraction_view

    expression = entry.get().strip()
    fraction_view = False

    if not expression:
        result_label.config(
            text="Please enter an expression",
            fg="#ffa500"
        )
        return

    try:
        result = evaluate_expression(expression)

        last_answer = result
        CONSTANTS["ANS"] = result
        just_calculated = True
        fraction_view = False

        if result == int(result):
            display_result = str(int(result))
        else:
            display_result = str(round(result, 4))

        result_label.config(
            text=f"Result: {display_result}",
            fg="#2ed573"
        )

    except (ValueError, SyntaxError, ZeroDivisionError,
            OverflowError, TypeError, RecursionError):
        result_label.config(
            text="Error: Invalid Expression",
            fg="#ff4757"
        )


def toggle_fraction():
    global fraction_view

    if last_answer is None:
        result_label.config(
            text="Calculate something first",
            fg="#ffa500"
        )
        return

    if fraction_view:
        if last_answer == int(last_answer):
            display = str(int(last_answer))
        else:
            display = str(round(last_answer, 4))

        fraction_view = False

    else:
        fraction = Fraction(last_answer).limit_denominator(1000)

        if abs(float(fraction) - last_answer) > 1e-10:
            result_label.config(
                text="No simple fraction available",
                fg="#ffa500"
            )
            return

        display = str(fraction)
        fraction_view = True

    result_label.config(
        text=f"Result: {display}",
        fg="#2ed573"
    )

def insert_text(value):
    global just_calculated

    if just_calculated:
        entry.delete(0, tk.END)

        if value in ("+", "-", "×", "÷", "%", "*", "/"):
            entry.insert(0, "ANS")

        just_calculated = False

    entry.insert(tk.INSERT, value)
    entry.focus_set()


def start_exponent():
    global power_entry_active, exponent_base_position

    expression = entry.get()
    position = entry.index(tk.INSERT)

    if position == 0 or not expression[:position].strip():
        result_label.config(
            text="Enter a base number first",
            fg="#ffa500"
        )
        return

    power_entry_active = True
    exponent_base_position = position

    exponent_entry.delete(0, tk.END)

    root.update_idletasks()

    from tkinter import font as tkfont

    entry_font = tkfont.Font(font=entry.cget("font"))

    text_before_cursor = expression[:position]
    text_width = entry_font.measure(expression)
    before_width = entry_font.measure(text_before_cursor)

    text_start_x = (entry.winfo_width() - text_width) // 2


    x = text_start_x + before_width + 2
    y = -20

    exponent_entry.place(x=x, y=1, width=32, height=18)
    exponent_entry.lift()
    exponent_entry.focus_set()


def finish_exponent():
    global power_entry_active, exponent_base_position

    exponent = exponent_entry.get().strip()

    if not exponent:
        return False

    # Allow integer and decimal exponents, including negative values
    if not re.fullmatch(r"-?(?:\d+(?:\.\d*)?|\.\d+)", exponent):
        result_label.config(
            text="Error: Invalid exponent",
            fg="#ff4757"
        )
        return False

    if exponent.lstrip("-").isdigit():
        display_exponent = exponent.translate(SUPERSCRIPTS)
        expression_exponent = display_exponent
    else:
        expression_exponent = f"^({exponent})"

    entry.insert(exponent_base_position, expression_exponent)

    exponent_entry.place_forget()
    power_entry_active = False
    exponent_base_position = None

    entry.focus_set()
    return True

button_frame = tk.Frame(root, bg="#2f3542")
button_frame.pack(pady=8)

buttons = [
    ["sin", "cos", "tan", "cosec", "sec", "cot"],
    ["atan", "√", "x²", "1/x", "pi", "e"],
    ["7", "8", "9", "(", ")", "⌫"],
    ["4", "5", "6", "+", "-", "AC"],
    ["1", "2", "3", "×", "÷", "xʸ"],
    [".", "0", "%", "x³", "ANS", "="],
    ["log", "ln", "x!", "|x|", "sinh", "cosh"],
    ["nPr", "nCr", "³√", "×10ˣ", "⁴√", "⁵√"]
]

def button_click(value):
    global power_entry_active, just_calculated, fraction_view

    if power_entry_active:
        if value == "=":
            if finish_exponent():
                calculate()
            return

        if value == "⌫":
            exponent_entry.delete(
                max(0, exponent_entry.index(tk.INSERT) - 1),
                tk.INSERT
            )
            return

        if value in "0123456789.-" and len(value) == 1:
            exponent_entry.insert(tk.INSERT, value)
            exponent_entry.focus_set()
            return

        if not finish_exponent():
            return

    if value == "=":
        calculate()

    elif value == "ANS":
        if last_answer is None:
            result_label.config(
                text="No previous answer",
                fg="#ffa500"
            )
        else:
            insert_text("ANS")

    elif value in ("C", "AC"):
        entry.delete(0, tk.END)
        result_label.config(text="")
        just_calculated = False
        fraction_view = False

    elif value == "⌫":
        position = entry.index(tk.INSERT)

        if position > 0:
            entry.delete(position - 1, position)

    elif value == "x²":
        insert_text("²")

    elif value == "x³":
        insert_text("³")

    elif value == "xʸ":
        start_exponent()



    elif value == "a/b":
        insert_text("/")

    elif value == "1/x":
        if just_calculated and last_answer is not None:
            expression = "ANS"
        else:
            expression = entry.get().strip()

        if not expression:
            result_label.config(
                text="Enter a number first",
                fg="#ffa500"
            )
            return

        entry.delete(0, tk.END)
        entry.insert(0, f"1/({expression})")
        just_calculated = False

    elif value == "x!":
        insert_text("fact(")

    elif value == "|x|":
        insert_text("abs(")


    elif value == "nPr":
        insert_text("nPr(")


    elif value == "nCr":
        insert_text("nCr(")

    elif value == "√":
        insert_text("√(")

    elif value in ("³√", "⁴√", "⁵√"):
        insert_text(value + "(")



    elif value == "×10ˣ":
        if just_calculated and last_answer is not None:
            entry.delete(0, tk.END)
            entry.insert(0, "ANS")
            just_calculated = False

        insert_text("×10^(")
    elif value in (

            "sin", "cos", "tan", "sec",
            "cosec", "cot", "atan", "sqrt",
            "log", "ln", "sinh", "cosh"
    ):

        insert_text(value + "(")

    else:
        insert_text(value)

for row_index, row in enumerate(buttons):
    for col_index, value in enumerate(row):
        if value == "=":
            color = "#1e90ff"
        elif value in ("C", "AC", "⌫"):
            color = "#e74c3c"
        elif value in ("+", "-", "×", "÷", "*", "/", "^", "**", "(", ")", "%", ","):
            color = "#747d8c"
        elif value in ("sin", "cos", "tan", "cosec", "sec",
                       "cot", "atan", "sqrt", "√", "x²", "x³",
                       "xʸ", "1/x", "pi", "e", "ANS",
                       "log", "ln", "x!", "|x|", "sinh", "cosh",
                       "nPr", "nCr", "³√", "×10ˣ", "⁴√", "⁵√"):
            color = "#3742fa"
        else:
            color = "#57606f"

        button = tk.Button(
            button_frame,
            text=value,
            font=("Arial", 12, "bold"),
            width=9,
            height=2,
            bg=color,
            fg="white",
            activebackground="#70a1ff",
            relief="flat",
            command=lambda v=value: button_click(v)
        )
        button.grid(
            row=row_index,
            column=col_index,
            padx=4,
            pady=4
        )
fraction_frame = tk.Frame(root, bg="#2f3542")
fraction_frame.pack(pady=5)

comma_button = tk.Button(
    fraction_frame,
    text=",",
    font=("Arial", 12, "bold"),
    width=9,
    height=2,
    bg="#747d8c",
    fg="white",
    relief="flat",
    command=lambda: button_click(",")
)

comma_button.grid(row=0, column=0, padx=4)

fraction_button = tk.Button(
    fraction_frame,
    text="a/b",
    font=("Arial", 12, "bold"),
    width=9,
    height=2,
    bg="#3742fa",
    fg="white",
    relief="flat",
    command=lambda: button_click("a/b")
)

fraction_button.grid(row=0, column=1, padx=4)

convert_button = tk.Button(
    fraction_frame,
    text="S⇔D",
    font=("Arial", 12, "bold"),
    width=9,
    height=2,
    bg="#3742fa",
    fg="white",
    relief="flat",
    command=toggle_fraction
)

convert_button.grid(row=0, column=2, padx=4)


def handle_return(event):
    if power_entry_active:
        if finish_exponent():
            calculate()
    else:
        calculate()


root.bind("<Return>", handle_return)
exponent_entry.bind("<Return>", handle_return)

root.mainloop()