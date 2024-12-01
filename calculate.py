class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b

    def evaluate_expression(self, expression):
        try:
            allowed_characters = set("0123456789+-*/(). ")
            if not set(expression).issubset(allowed_characters):
                raise ValueError("Expression contains invalid characters.")
            result = eval(expression, {"__builtins__": None}, {})
            return result
        except ZeroDivisionError:
            raise ValueError("Division by zero is not allowed.")
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")