# 🎰 Niquel

A small Python project that simulates a slot machine through the terminal.

This project was created mainly as a **programming study project**. The goal is not to create a professional casino system, but to practice basic programming concepts by building something from scratch.

## 💡 Project Idea

The player starts by choosing how much fictional money they want in their bank.

This value represents the total amount of money available for that game.

For example:

```text
Bank: 500
```

The player can then transfer part of the money from the bank to the house:

```text
Bank: 400
House: 100
```

Inside the house, the player chooses how much they want to bet.

For example:

```text
House: 100
Bet: 20
```

After that, the player chooses how many spins they want to make.

```text
Number of spins: 5
```

The machine performs the spins one by one, showing a small animation before displaying the final result.

## 🍓 Results

The slot machine has five symbols:

```text
🍓 Strawberry
🍇 Grape
🥭 Mango
💣 Bomb
🔄 Retry
```

Each special result has a different effect:

| Result |   Multiplier |
| ------ | -----------: |
| 🍓🍓🍓 |           x2 |
| 🍇🍇🍇 |           x5 |
| 🥭🥭🥭 |          x10 |
| 💣💣💣 | Lose the bet |
| 🔄🔄🔄 |   Free retry |

Any other combination is considered a loss.

## 🎲 How the Chances Work

The machine uses `random.choice()` to randomly select each symbol.

In normal mode:

```python
niquel = ["🍓", "🍇", "🥭", "💣", "🔄"]
```

There are five possible symbols.

Since every symbol appears once in the list, each symbol has approximately:

```text
20%
```

chance of being selected on each roll.

Because the machine has three independent rolls, getting three identical symbols is much less likely than getting a single symbol.

For example, the probability of getting:

```text
🍓🍓🍓
```

is:

```text
1/5 × 1/5 × 1/5 = 1/125
```

which is approximately:

```text
0.8%
```

The same principle applies to the other special combinations in normal mode.

## 🔐 VIP Mode

There is also a small secret mode.

When starting the program, if the player enters:

```text
VIP
```

instead of entering the initial bank value, VIP mode is activated.

The player then chooses the initial bank normally.

In VIP mode, the program uses a different list:

```python
vip_niquel = [
    "🍓", "🍓", "🍓",
    "🍇", "🍇",
    "🥭",
    "💣",
    "🔄"
]
```

Some symbols appear more than once.

Because `random.choice()` chooses from the entire list, repeating a symbol increases its probability of being selected.

The purpose of this system is to practice the idea that the structure of a list can affect probability.

## 🎰 Spin System

The player can choose how many spins they want.

For example:

```text
How many spins do you want? 5
```

The program will perform:

```text
SPIN 1
SPIN 2
SPIN 3
SPIN 4
SPIN 5
```

Each spin contains a small animation using `time.sleep()` to make the machine feel like it is actually spinning.

## 🏦 Bank and House

The project separates the player's money into two places.

### Bank

The bank represents the money the player currently owns but has not placed into the house.

### House

The house represents the money that the player has transferred into the game.

This allows the player to control how much money they want to put into the machine.

After the spins, the player can transfer the money from the house back to the bank.

For example:

```text
Bank: 400
House: 140
```

After transferring:

```text
Bank: 540
House: 0
```

## 💀 Game Over

If the bank reaches:

```text
0
```

the player has no money left and the game ends.

The initial bank value therefore works like a kind of "life" for the player.

A smaller starting value makes the game harder, while a larger value gives the player more room to continue playing.

## 📚 Learning Purpose

This project was created as a personal programming exercise.

The first version was written manually using the concepts I was studying at the time.

After building the initial version, I used ChatGPT to help finish some parts of the project and learned new things from the changes.

The goal was not simply to copy a finished program, but to understand the logic and use the project as a way to learn.

The code is intentionally kept relatively simple because this is a learning project. I want to be able to read the code, understand what each part does, and continue improving it myself.

## 🚧 Possible Future Improvements

Some things that could be added in the future:

* Automatically calculate and display the probabilities
* Add more symbols
* Add different difficulty levels
* Add spin history
* Add session statistics
* Improve the spinning animation
* Add sounds
* Save progress to a file
* Add a ranking system
* Create a graphical interface

For now, the main goal is simply to keep learning Python by building things.

---

**Study project — Python 🎰🐍**
