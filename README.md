Simple Python Calculator

Files:
- `calculator.py`: CLI calculator with a safe expression evaluator.
- `test_calculator.py`: Unit tests using Python's `unittest`.

Quick start (PowerShell):

Run the calculator:

```powershell
python .\calculator.py
```

Try expressions like:
- `2+3*4`
- `2 ^ 3` (caret `^` is accepted as power)
- `-5 + (2*3)`

Run tests:

```powershell
python -m unittest test_calculator.py
```

Notes:
- The evaluator is intentionally restrictive: no names or function calls are allowed.
- Use `q` or press Ctrl+C to exit the interactive calculator.
