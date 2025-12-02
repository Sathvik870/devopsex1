"""Simple safe calculator CLI.

Usage:
  python calculator.py

Type an expression (e.g. 2+3*4 or 2 ^ 3) and press Enter. Type 'q' or Ctrl+C to quit.

This evaluator uses Python's AST to only allow numeric literals and safe operators.
"""
from __future__ import annotations

import ast
import operator as _op
from typing import Union


_OPERATORS = {
    ast.Add: _op.add,
    ast.Sub: _op.sub,
    ast.Mult: _op.mul,
    ast.Div: _op.truediv,
    ast.Pow: _op.pow,
    ast.Mod: _op.mod,
}


def _eval_node(node: ast.AST) -> Union[int, float]:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError(f"Unsupported constant: {node.value!r}")

    if isinstance(node, ast.BinOp):
        left = _eval_node(node.left)
        right = _eval_node(node.right)
        op_type = type(node.op)
        if op_type in _OPERATORS:
            try:
                return _OPERATORS[op_type](left, right)
            except ZeroDivisionError as e:
                raise ValueError("Division by zero") from e
        raise ValueError(f"Unsupported operator: {op_type!r}")

    if isinstance(node, ast.UnaryOp):
        operand = _eval_node(node.operand)
        if isinstance(node.op, ast.UAdd):
            return +operand
        if isinstance(node.op, ast.USub):
            return -operand
        raise ValueError(f"Unsupported unary operator: {type(node.op)!r}")

    raise ValueError(f"Unsupported expression: {type(node)!r}")


def evaluate(expression: str) -> Union[int, float]:
    """Safely evaluate a numeric expression and return the result.

    Supported operators: +, -, *, /, %, ** (or ^ will be accepted and treated as power).
    Parentheses are supported.
    """
    if not isinstance(expression, str):
        raise ValueError("Expression must be a string")

    expr = expression.strip()
    if not expr:
        raise ValueError("Empty expression")

    # Allow users to write ^ for power (common in calculators)
    expr = expr.replace("^", "**")

    try:
        tree = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise ValueError("Invalid expression syntax") from e

    # Walk AST to ensure it contains only allowed node types
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            raise ValueError("Function calls are not allowed")
        if isinstance(node, ast.Name):
            raise ValueError("Names are not allowed in expressions")

    return _eval_node(tree.body)


def _main() -> None:
    print("Simple calculator — enter expressions (type 'q' to quit)")
    try:
        while True:
            try:
                s = input("> ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not s:
                continue
            if s.lower() in {"q", "quit", "exit"}:
                break
            try:
                result = evaluate(s)
            except ValueError as e:
                print(f"Error: {e}")
            else:
                print(result)
    except (KeyboardInterrupt, EOFError):
        pass


if __name__ == "__main__":
    _main()
