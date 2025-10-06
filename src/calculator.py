"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""

def add(a, b):
    """Add two numbers together"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers with input validation and logging."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    
    print(f"Multiplying {a} × {b}")  # Added logging
    result = a * b
    print(f"Result: {result}")
    return result

def divide(a, b):
    """Divide a by b with enhanced error handling."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError(f"Cannot divide {a} by zero - division by zero is undefined")
    
    print(f"Dividing {a} ÷ {b}")  # Added logging
    result = a / b
    print(f"Result: {result}")
    return result

class TestMultiplyDivideWithValidation:
    """Test multiplication and division with input validation."""

      def test_multiply_by_zero(self):
        """Test multiplying by zero """
        assert multiply(5,0) == 0
        assert multiply(0,10) == 0
          
     def test_multiply_positive_number(self):
        """Test multiplying positive numbers"""
        assert multiply(2, 3) == 6
        assert multiply(4, 5) == 20


    def test_multiply_negative_number(self):
        """Test multiplying negative numbers"""
        assert multiply(-2, 3) == -6
        assert multiply(-4, -5) == 20

     def test_divide_positive_number(self):
        """Test dividing positive numbers"""
        assert divide(10, 2) == 5
        assert divide(15, 3) == 5
         
    def test_divide_negative_number(self):
        """Test dividing negative numbers"""
        assert divide(-10, 2) == -5
        assert divide(-12, -3) == 4

    def test_multiply_input_validation(self):
        """Test multiply rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply("5", 3)
        with pytest.raises(TypeError, match="Both arguments must be numbers"):
            multiply(5, "3")
    
    def test_divide_input_validation(self):
        """Test divide rejects non-numeric inputs."""
        with pytest.raises(TypeError, match="Division requires numeric inputs"):
            divide("10", 2)
    def power(a,b):
        """Raise a to the power of b"""
        return a ** b

    def square_root(a):
        """calculate square root of a"""
        if a<0:
            raise ValueError("Cannot calculate square root of negative number")
            return a ** 0.5

if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
