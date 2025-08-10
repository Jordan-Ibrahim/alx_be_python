class Calculator:
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """Prints the calculation type and returns the product of a and b. """
        print(f"Calculator Type: {cls.calculation_type}")
        return a * b
    
    
