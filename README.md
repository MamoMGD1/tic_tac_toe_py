# 🤖 AI Tic-Tac-Toe

An **AI-powered Tic-Tac-Toe game** that plays optimally using the **Minimax algorithm**! The AI is trained to make the best possible moves, ensuring a challenging experience for any player. The game can be played **instantly without training**, but if you train it beforehand, it gets even smarter! 🎯

---

## 🚀 Features
✅ **Instant Play** – No need to train before playing! The AI is already optimized to play perfectly.  
✅ **Unbeatable AI** – Uses Minimax to make optimal moves, making it impossible to defeat.  
✅ **Smart Move Recording** – The AI keeps track of game states and refines its decisions over time.  
✅ **Training Mode (Optional)** – Training allows the AI to recognize board positions and optimize moves faster.  
✅ **Interactive Gameplay** – Play against an AI opponent and see its decision-making in action.  

---

## 🛠 How It Works
The AI uses the **Minimax algorithm**, which ensures optimal play by evaluating all possible moves and picking the best one. If both players play optimally, the game will always end in a **draw**. Training does not change its perfect play but **helps the AI recognize board positions faster** instead of recalculating everything from scratch.

### Why Train If It's Already Smart? 🤔
While training isn't required, it has some advantages:
- **Speeds up AI decision-making** – The AI stores previously calculated board states, reducing computation time.
- **Optimizes performance** – Helps the AI find optimal moves faster during gameplay.
- **Improves adaptive play** – Allows AI to refine its response to different scenarios.

---

## 🎮 How to Play
1. Clone the repository:
   ```sh
   git clone https://github.com/MamoMGD1/tic-tac-toe.git
   ```
2. Navigate to the project directory:
   ```sh
   cd tic-tac-toe
   ```
3. Run the game:
   ```sh
   python main.py
   ```
4. Play against the AI and try to win! 😈

---

## 🧠 How AI Makes Decisions
- The AI **evaluates all possible moves** using Minimax.
- It assigns a score to each move based on **winning, losing, or drawing**.
- **If both AIs play optimally, the game always results in a draw!**
- Training lets the AI remember board states, **reducing the need for redundant calculations**.

---

## 🔍 Future Improvements
- Implementing **Reinforcement Learning (RL)** to introduce self-improvement.
- Adding a difficulty setting where AI **can play non-optimally** for a more fun experience.
- Enhancing UI for a more engaging experience.

---

## 🏆 Contributing
Feel free to contribute! If you have ideas to improve the AI, **fork the repo** and submit a pull request.

---

## 📜 License
This project is licensed under the **MIT License**.

Happy coding! 🎮🤖
