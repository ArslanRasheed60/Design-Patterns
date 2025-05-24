from abc import ABC, abstractmethod
from typing import Optional

# Product
class Notification(ABC):
    """Abstract Product class that defines the interface for all notification types."""
    
    @abstractmethod
    def send(self, recipient: str, message: str) -> str:
        """Send a notification to the recipient with the given message."""
        pass

# Concrete Products
class EmailNotification(Notification):
    """Concrete Product for email notifications."""
    
    def send(self, recipient: str, message: str) -> str:
        return f"Sending email to {recipient}: {message}"

class SMSNotification(Notification):
    """Concrete Product for SMS notifications."""
    
    def send(self, recipient: str, message: str) -> str:
        return f"Sending SMS to {recipient}: {message}"

class PushNotification(Notification):
    """Concrete Product for push notifications."""
    
    def send(self, recipient: str, message: str) -> str:
        return f"Sending push notification to device {recipient}: {message}"

class SlackNotification(Notification):
    """Concrete Product for Slack notifications."""
    
    def send(self, recipient: str, message: str) -> str:
        return f"Sending Slack message to channel {recipient}: {message}"

class WhatsAppNotification(Notification):
    """Concrete Product for WhatsApp notifications."""
    
    def send(self, recipient: str, message: str) -> str:
        return f"Sending WhatsApp to {recipient}: {message}"

class TelegramNotification(Notification):
    """Concrete Product for Telegram notifications."""
    
    def send(self, recipient: str, message: str) -> str:
        return f"Sending Telegram message to {recipient}: {message}"

# Creator (Factory)
class NotificationFactory(ABC):
    """Abstract Creator class that declares the factory method."""
    
    @abstractmethod
    def create_notification(self) -> Notification:
        """Factory method to be implemented by subclasses."""
        pass
    
    def send_notification(self, recipient: str, message: str) -> str:
        """Client code that uses the factory method."""
        notification = self.create_notification()
        return notification.send(recipient, message)

# Concrete Creators
class EmailNotificationFactory(NotificationFactory):
    """Concrete Creator for email notifications."""
    
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSNotificationFactory(NotificationFactory):
    """Concrete Creator for SMS notifications."""
    
    def create_notification(self) -> Notification:
        return SMSNotification()

class PushNotificationFactory(NotificationFactory):
    """Concrete Creator for push notifications."""
    
    def create_notification(self) -> Notification:
        return PushNotification()

class SlackNotificationFactory(NotificationFactory):
    """Concrete Creator for Slack notifications."""
    
    def create_notification(self) -> Notification:
        return SlackNotification()

class WhatsAppNotificationFactory(NotificationFactory):
    """Concrete Creator for WhatsApp notifications."""
    
    def create_notification(self) -> Notification:
        return WhatsAppNotification()

class TelegramNotificationFactory(NotificationFactory):
    """Concrete Creator for Telegram notifications."""
    
    def create_notification(self) -> Notification:
        return TelegramNotification()

def client_code(factory: NotificationFactory, recipient: str, message: str) -> None:
    """Client code that works with any notification factory."""
    print(factory.send_notification(recipient, message))

if __name__ == "__main__":
    # Example usage
    email_factory = EmailNotificationFactory()
    client_code(email_factory, "user@example.com", "Hello via Email!")
    
    sms_factory = SMSNotificationFactory()
    client_code(sms_factory, "+1234567890", "Hello via SMS!")
    
    push_factory = PushNotificationFactory()
    client_code(push_factory, "device-12345", "Hello via Push Notification!")
    
    slack_factory = SlackNotificationFactory()
    client_code(slack_factory, "#general", "Hello via Slack!")
    
    whatsapp_factory = WhatsAppNotificationFactory()
    client_code(whatsapp_factory, "+1234567890", "Hello via WhatsApp!")
    
    telegram_factory = TelegramNotificationFactory()
    client_code(telegram_factory, "@username", "Hello via Telegram!")