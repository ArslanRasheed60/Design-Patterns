import copy
from abc import ABC, abstractmethod
from typing import Any, Dict


class Prototype(ABC):
    """
    The Prototype interface declares the cloning methods.
    """
    
    @abstractmethod
    def clone(self) -> 'Prototype':
        pass


class Vehicle(Prototype):
    """
    Concrete implementation of Prototype for Vehicle objects.
    """
    
    def __init__(self, make: str, model: str, color: str, **extras: Any):
        self.make = make
        self.model = model
        self.color = color
        self.extras = extras or {}
    
    def __str__(self) -> str:
        extras_str = ', '.join(f"{k}: {v}" for k, v in self.extras.items())
        return f"{self.color} {self.make} {self.model} " + (f"({extras_str})" if extras_str else "")
    
    def clone(self) -> 'Vehicle':
        """
        Create a deep copy of this object.
        """
        return copy.deepcopy(self)


class VehicleRegistry:
    """
    Prototype manager that stores pre-built prototypes.
    """
    
    def __init__(self):
        self._prototypes: Dict[str, Prototype] = {}
    
    def register(self, name: str, prototype: Prototype) -> None:
        self._prototypes[name] = prototype
    
    def unregister(self, name: str) -> None:
        if name in self._prototypes:
            del self._prototypes[name]
    
    def clone(self, name: str, **attrs: Any) -> Prototype:
        """
        Clone a prototype and update its attributes.
        """
        if name not in self._prototypes:
            raise ValueError(f"No prototype registered with name: {name}")
        
        obj = self._prototypes[name].clone()
        
        # Update attributes if provided
        for key, value in attrs.items():
            setattr(obj, key, value)
            
        return obj


def main():
    # Create a prototype registry
    registry = VehicleRegistry()
    
    # Create and register some prototypes
    base_car = Vehicle("Toyota", "Corolla", "Blue")
    registry.register("base_car", base_car)
    
    premium_car = Vehicle("BMW", "5 Series", "Black", 
                          engine="V6", navigation=True, sunroof=True)
    registry.register("premium_car", premium_car)
    
    # Clone and customize vehicles
    car1 = registry.clone("base_car", color="Red")
    car2 = registry.clone("premium_car", color="Silver", sunroof=False)
    
    # Create a completely new car using the prototype
    car3 = registry.clone("base_car")
    car3.make = "Honda"
    car3.model = "Civic"
    car3.color = "White"
    car3.extras["seats"] = 5
    
    # Print the results
    print(f"Original base car: {base_car}")
    print(f"Cloned car 1: {car1}")
    print(f"Cloned premium car: {car2}")
    print(f"Custom new car: {car3}")


if __name__ == "__main__":
    main()
