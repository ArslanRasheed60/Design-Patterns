"""
Implementation of the Builder Design Pattern
The Builder pattern is a creational design pattern that lets you construct complex objects step by step.
It separates the construction of a complex object from its representation, so the same construction process
can create different representations.
"""

class Product:
    """The complex object under construction"""
    def __init__(self):
        self.parts = []

    def add(self, part):
        """Add a part to the product"""
        self.parts.append(part)

    def show(self):
        """Display the parts of the product"""
        print("Product Parts:", self.parts)


class Builder:
    """Abstract Builder interface"""
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def get_result(self):
        pass


class ConcreteBuilder(Builder):
    """Concrete implementation of the Builder interface"""
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        """Build part A of the product"""
        self.product.add("PartA")

    def build_part_b(self):
        """Build part B of the product"""
        self.product.add("PartB")

    def get_result(self):
        """Return the constructed product"""
        return self.product


class Director:
    """Director class that constructs the product using the builder"""
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        """Construct the product using the builder"""
        self.builder.build_part_a()
        self.builder.build_part_b()


if __name__ == "__main__":
    # Example usage
    builder = ConcreteBuilder()
    director = Director(builder)
    director.construct()
    product = builder.get_result()
    product.show()
