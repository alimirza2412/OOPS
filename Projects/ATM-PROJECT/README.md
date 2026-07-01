# Simple ATM Simulator (Python)

A beginner-friendly command-line ATM simulator built with Python and object-oriented programming. Users can create a PIN, check their balance, deposit money, and withdraw money — all through a simple text-based menu.

## Features

- 🔐 **Create PIN** — Set a PIN to secure your account
- 💰 **Check Balance** — View your current balance (PIN protected)
- 📥 **Deposit** — Add funds to your balance (PIN protected)
- 📤 **Withdraw** — Take out funds, with insufficient balance checks (PIN protected)
- 🚪 **Exit** — Leave the program gracefully

## How It Works

The program is built around a single `Atm` class that manages:

- `pin` — the user's PIN (empty until created)
- `balance` — the user's current balance (starts at 0)

When the program runs, it displays a menu in a loop until the user chooses to exit.

## Requirements

- Python 3.x (no external libraries needed)

## Usage

1. Clone or download this repository.
2. Run the script:

   ```bash
   python ops.py
   ```

3. Follow the on-screen menu:

   ```
   Hello, you are welcome to our bank
   please select the option you need
   1. Create your pin
   2. Check your bank balance
   3. Deposit amount
   4. Withdraw amount
   5. Exit
   ```

4. Enter the number corresponding to the action you want to perform.

## Example Session

```
Enter your pin: 1234
Your pin has been successfully created

Enter your pin: 1234
Enter the amount you want to deposit: 500
Deposit successful

Enter your pin: 1234
Your balance is: 500
```

## Notes / Limitations

This is a learning project and has a few simplifications worth knowing about:

- The PIN is stored as plain text in memory (not hashed or encrypted).
- Data is not persisted — balance and PIN reset every time the program restarts.
- No input validation for non-numeric amounts (entering text where a number is expected will crash the program).
- Single-user only; there's no concept of multiple accounts.

## Possible Improvements

- Add input validation and error handling (e.g. `try/except` around `int(input(...))`)
- Persist data using a file or database
- Hash/encrypt the PIN instead of storing it in plain text
- Support multiple user accounts
- Add a transaction history log

## License

Feel free to use, modify, and share this project for learning purposes.
