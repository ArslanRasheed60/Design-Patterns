from threading import Lock

class SingletonMeta(type):
    """
    This is a thread-safe implementation of Singleton.
    """
    _instances = {}
    _lock = Lock()  # Lock object to synchronize threads during first access

    def __call__(cls, *args, **kwargs):
        # Check if the instance exists
        if cls not in cls._instances:
            # Acquire the lock to ensure only one thread proceeds
            with cls._lock:
                # Double check in case another thread acquired the lock first
                if cls not in cls._instances:
                    # Create and store the instance
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """
    def __init__(self, value=None):
        self.value = value

    def some_business_logic(self):
        """
        Finally, any singleton should define some business logic, which can be
        executed on its instance.
        """
        return f"Executing business logic with value: {self.value}"


# Example usage
if __name__ == "__main__":
    # The client code
    s1 = Singleton("First instance")
    s2 = Singleton("Second instance")

    if id(s1) == id(s2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
    
    print(f"s1 value: {s1.value}")
    print(f"s2 value: {s2.value}")
    
    # The second initialization parameter is ignored
    s2.value = "Updated value"
    print(f"s1 value after update: {s1.value}")
    print(f"s2 value after update: {s2.value}")
    
    # Business logic example
    print(s1.some_business_logic())
