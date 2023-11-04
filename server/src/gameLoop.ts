// Proper game loop implementation:
// https://isaacsukin.com/news/2015/01/detailed-explanation-javascript-game-loops-and-timing

class GameLoop {
    private tickRate: number;
    private tickLengthMs: number;
    private isRunning: boolean;
    private previousTimestamp: number;
    private currentTimestamp: number;
    private deltaTime?: number;
    private readonly gameLogicCallback: (deltaTime: number) => void;

    constructor(gameLogicCallback: (deltaTime: number) => void, tickRate = 60) {
        this.tickRate = tickRate;
        this.tickLengthMs = 1000 / this.tickRate;
        this.isRunning = false;
        this.previousTimestamp = 0;
        this.currentTimestamp = 0;
        this.update = this.update.bind(this);
        this.gameLogicCallback = gameLogicCallback;
    }

    public start(): void {
        if (!this.isRunning) {
            this.isRunning = true;
            this.previousTimestamp = this.hrTimeMs();
            this.update();
        }
    }

    public stop(): void {
        this.isRunning = false;
    }

    private hrTimeMs(): number {
        const [seconds, nanoseconds] = process.hrtime();
        return (seconds * 1000) + (nanoseconds / 1_000_000);
    }

    public update(): void {
        if (!this.isRunning) {
            console.warn('Loop is not started.');
            return;
        }

        setTimeout(this.update, this.tickLengthMs);
        this.currentTimestamp = this.hrTimeMs();
        this.deltaTime = this.currentTimestamp - this.previousTimestamp;
        this.gameLogicCallback(this.deltaTime);
        this.previousTimestamp = this.currentTimestamp;
    }
};

export { GameLoop };
