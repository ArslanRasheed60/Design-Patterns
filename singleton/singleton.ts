class Singleton {
    private static instance: Singleton;
    private static instanceLock: boolean = false;
    
    // Public property to store data
    public value: any;

    /**
     * The Singleton's constructor should always be private to prevent direct
     * construction calls with the `new` operator.
     */
    private constructor(value: any) {
        if (Singleton.instance) {
            throw new Error("Use Singleton.getInstance() instead of new Singleton()");
        }
        this.value = value;
        Singleton.instanceLock = false;
    }

    /**
     * The static method that controls the access to the singleton instance.
     * This implementation let you subclass the Singleton class while keeping
     * just one instance of each subclass around.
     */
    public static getInstance(value: any = null): Singleton {
        if (!Singleton.instance) {
            // Prevent constructor from being called directly
            if (Singleton.instanceLock) {
                throw new Error("Use getInstance() instead of new Singleton()");
            }
            
            Singleton.instanceLock = true;
            Singleton.instance = new Singleton(value);
        }
        return Singleton.instance;
    }

    /**
     * Business logic method example
     */
    public someBusinessLogic(): string {
        return `Executing business logic with value: ${this.value}`;
    }
}

/**
 * Example usage
 */
function clientCode() {
    const s1 = Singleton.getInstance("First instance");
    const s2 = Singleton.getInstance("Second instance");

    if (s1 === s2) {
        console.log('Singleton works, both variables contain the same instance.');
    } else {
        console.log('Singleton failed, variables contain different instances.');
    }

    console.log(`s1 value: ${s1.value}`);
    console.log(`s2 value: ${s2.value}`);

    // The second initialization parameter is ignored
    s2.value = "Updated value";
    console.log(`s1 value after update: ${s1.value}`);
    console.log(`s2 value after update: ${s2.value}`);
    
    // Business logic example
    console.log(s1.someBusinessLogic());
}

// Run the example
clientCode();