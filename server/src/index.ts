import { GameLoop } from './gameLoop';

const gameLoop = new GameLoop((deltaTime: number) => {
    for (let i = 0; i < 10000; i++) {}

    console.log("FPS:", 1000 / deltaTime);
}, 60);

gameLoop.start();