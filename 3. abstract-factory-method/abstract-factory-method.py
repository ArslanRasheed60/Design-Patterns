from abc import ABC, abstractmethod

class GUIFactory(ABC):
    """Abstract Factory"""
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_checkbox(self):
        pass

class WindowsFactory(GUIFactory):
    """Concrete Factory for Windows GUI"""
    def create_button(self):
        return WindowsButton()

    def create_checkbox(self):
        return WindowsCheckbox()

class WebFactory(GUIFactory):
    """Concrete Factory for Web GUI"""
    def create_button(self):
        return WebButton()

    def create_checkbox(self):
        return WebCheckbox()

class Button(ABC):
    """Abstract Product A"""
    @abstractmethod
    def render(self):
        pass

class WindowsButton(Button):
    """Concrete Product A1"""
    def render(self):
        return "Rendering Windows Button"

class WebButton(Button):
    """Concrete Product A2"""
    def render(self):
        return "Rendering Web Button"

class Checkbox(ABC):
    """Abstract Product B"""
    @abstractmethod
    def render(self):
        pass

class WindowsCheckbox(Checkbox):
    """Concrete Product B1"""
    def render(self):
        return "Rendering Windows Checkbox"

class WebCheckbox(Checkbox):
    """Concrete Product B2"""
    def render(self):
        return "Rendering Web Checkbox"

def client_code(factory: GUIFactory):
    """Client code that works with factories and products"""
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(f"Button: {button.render()}")
    print(f"Checkbox: {checkbox.render()}")

# Example usage
if __name__ == "__main__":
    print("Using Windows GUI factory:")
    client_code(WindowsFactory())
    
    print("\nUsing Web GUI factory:")
    client_code(WebFactory())