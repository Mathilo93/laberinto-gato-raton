# Cat and Mouse Maze 🐭😼

## 🧠 Description
Python project that simulates a grid-based chase between a mouse and a cat.

The mouse tries to escape by reaching the goal, while the cat attempts to catch it first. Both agents make decisions using the Minimax algorithm with different evaluation functions.

---

## ⚙️ Technologies
- Python
- Minimax algorithm
- Evaluation heuristics
- Console / terminal

---

## 🚀 How to run

```bash
python laberinto_gato_raton.py
```

---

## 🎮 Game Rules
- The mouse starts near the top-left corner.
- The cat starts near the bottom-right corner.
- The goal is located at the bottom-right corner.
- The mouse can move in 4 directions.
- The cat can move in 8 directions.
- The simulation ends when:
  - the mouse reaches the goal 🏁
  - the cat catches the mouse 💀
  - or the turn limit is reached

---

## 🧠 AI Logic

### 🐭 Mouse (Maximizer)
- Minimizes distance to the goal
- Maximizes distance from the cat

👉 Goal: escape without being caught

### 😾 Cat (Minimizer)
- Minimizes distance to the mouse

👉 Goal: catch the mouse as quickly as possible

---

## ⚖️ Design Decisions
- The mouse moves in 4 directions while the cat moves in 8 to create balance.
- Separate evaluation functions are used to model different behaviors.
- Initial random turns are included to make the simulation less predictable.

---

## 📈 Learnings
During this project I worked on:
- 2D grid representation (matrices)
- Coordinate handling and movement logic
- Implementation of the Minimax algorithm
- Designing evaluation heuristics
- Balancing behavior between two competing agents

---

## 🔧 Possible Improvements
- Add obstacles or walls (real maze)
- Implement alpha-beta pruning for optimization
- Allow user interaction
- Adjust dynamic minimax depth

---

## 👤 Author
Project developed by Mathilo.