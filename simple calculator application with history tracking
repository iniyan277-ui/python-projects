"""
Simple Calculator Application
A beginner-friendly calculator with history tracking
"""

def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


def power(a, b):
    """Calculate power"""
    return a ** b


def square_root(a):
    """Calculate square root"""
    if a < 0:
        return "Error: Cannot calculate square root of negative number"
    return a ** 0.5


class Calculator:
    """Calculator class with history tracking"""
    
    def __init__(self):
        """Initialize calculator with empty history"""
        self.history = []
    
    def calculate(self, num1, operator, num2=None):
        """
        Perform calculation based on operator
        
        Args:
            num1: First number
            operator: Operation to perform (+, -, *, /, ^, sqrt)
            num2: Second number (not needed for sqrt)
        
        Returns:
            Result of the calculation
        """
        result = None
        
        if operator == '+':
            result = add(num1, num2)
        elif operator == '-':
            result = subtract(num1, num2)
        elif operator == '*':
            result = multiply(num1, num2)
        elif operator == '/':
            result = divide(num1, num2)
        elif operator == '^':
            result = power(num1, num2)
        elif operator == 'sqrt':
            result = square_root(num1)
        else:
            return "Error: Invalid operator"
        
        # Store in history
        if operator == 'sqrt':
            self.history.append(f"sqrt({num1}) = {result}")
        else:
            self.history.append(f"{num1} {operator} {num2} = {result}")
        
        return result
    
    def get_history(self):
        """Return calculation history"""
        return self.history
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
        print("History cleared!")


def display_menu():
    """Display calculator menu"""
    print("\n" + "="*40)
    print("       SIMPLE CALCULATOR")
    print("="*40)
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (^)")
    print("6. Square Root (sqrt)")
    print("7. View History")
    print("8. Clear History")
    print("9. Exit")
    print("="*40)


def main():
    """Main calculator function"""
    calc = Calculator()
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == '9':
            print("Thank you for using the calculator! Goodbye!")
            break
        
        elif choice == '7':
            if not calc.get_history():
                print("History is empty!")
            else:
                print("\nCalculation History:")
                for i, record in enumerate(calc.get_history(), 1):
                    print(f"{i}. {record}")
        
        elif choice == '8':
            calc.clear_history()
        
        elif choice in ['1', '2', '3', '4', '5']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                operators = {
                    '1': '+',
                    '2': '-',
                    '3': '*',
                    '4': '/',
                    '5': '^'
                }
                
                operator = operators[choice]
                result = calc.calculate(num1, operator, num2)
                print(f"\nResult: {result}\n")
            
            except ValueError:
                print("Error: Please enter valid numbers!\n")
        
        elif choice == '6':
            try:
                num = float(input("Enter number: "))
                result = calc.calculate(num, 'sqrt')
                print(f"\nResult: {result}\n")
            
            except ValueError:
                print("Error: Please enter a valid number!\n")
        
        else:
            print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()
