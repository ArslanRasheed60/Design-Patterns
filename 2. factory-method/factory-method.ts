// Product
interface INotification {
    send(recipient: string, message: string): string;
}

// Concrete Products
class EmailNotification implements INotification {
    send(recipient: string, message: string): string {
        return `Sending email to ${recipient}: ${message}`;
    }
}

class SMSNotification implements INotification {
    send(recipient: string, message: string): string {
        return `Sending SMS to ${recipient}: ${message}`;
    }
}

class PushNotification implements INotification {
    send(recipient: string, message: string): string {
        return `Sending push notification to device ${recipient}: ${message}`;
    }
}

class SlackNotification implements INotification {
    send(recipient: string, message: string): string {
        return `Sending Slack message to channel ${recipient}: ${message}`;
    }
}

class WhatsAppNotification implements INotification {
    send(recipient: string, message: string): string {
        return `Sending WhatsApp to ${recipient}: ${message}`;
    }
}

class TelegramNotification implements INotification {
    send(recipient: string, message: string): string {
        return `Sending Telegram message to ${recipient}: ${message}`;
    }
}

// Creator (Factory)
interface NotificationFactory {
    createNotification(): INotification;
    sendNotification(recipient: string, message: string): string;
}

abstract class AbstractNotificationFactory implements NotificationFactory {
    // Factory method to be implemented by subclasses
    abstract createNotification(): INotification;

    // Client code that uses the factory method
    sendNotification(recipient: string, message: string): string {
        const notification = this.createNotification();
        return notification.send(recipient, message);
    }
}

// Concrete Creators
class EmailNotificationFactory extends AbstractNotificationFactory {
    createNotification(): INotification {
        return new EmailNotification();
    }
}

class SMSNotificationFactory extends AbstractNotificationFactory {
    createNotification(): INotification {
        return new SMSNotification();
    }
}

class PushNotificationFactory extends AbstractNotificationFactory {
    createNotification(): INotification {
        return new PushNotification();
    }
}

class SlackNotificationFactory extends AbstractNotificationFactory {
    createNotification(): INotification {
        return new SlackNotification();
    }
}

class WhatsAppNotificationFactory extends AbstractNotificationFactory {
    createNotification(): INotification {
        return new WhatsAppNotification();
    }
}

class TelegramNotificationFactory extends AbstractNotificationFactory {
    createNotification(): INotification {
        return new TelegramNotification();
    }
}
// Client code that works with any notification factory
function clientCode(factory: NotificationFactory, recipient: string, message: string): void {
    console.log(factory.sendNotification(recipient, message));
}

// Example usage
const emailFactory = new EmailNotificationFactory();
clientCode(emailFactory, "user@example.com", "Hello via Email!");

const smsFactory = new SMSNotificationFactory();
clientCode(smsFactory, "+1234567890", "Hello via SMS!");

const pushFactory = new PushNotificationFactory();
clientCode(pushFactory, "device-12345", "Hello via Push Notification!");

const slackFactory = new SlackNotificationFactory();
clientCode(slackFactory, "#general", "Hello via Slack!");

const whatsappFactory = new WhatsAppNotificationFactory();
clientCode(whatsappFactory, "+1234567890", "Hello via WhatsApp!");

const telegramFactory = new TelegramNotificationFactory();
clientCode(telegramFactory, "@username", "Hello via Telegram!");