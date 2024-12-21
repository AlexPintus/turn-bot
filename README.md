# TurnBot

## Overview

This project was created to fulfill a personal need, so it may lack some features or depth. Contributions are welcome to expand and improve it!

To simplify its usage, a basic script has been provided via `Makefile`, which includes commands to:
- **Initialize** the project (first-time setup).
- **Run** the project.
- **Push** changes to GitHub.

You can execute these functionalities by running:

- **`init`**: For first-time setup of the project.
  ```bash
  make init
  ```

- **`run`**: To execute the project.
  ```bash
  make run
  ```

- **`push`**: To push changes to GitHub.
  ```bash
  make push message="your_commit_info"
  ```

Depending on your Linux distribution, you may need to install `make` to use this feature.

## Licenses

The `licences` folder includes two files:

- **`LICENCE`**: The current license for this software.
- **`LIBRARY_LICENCE`**: The licenses of the libraries used in the project.
  - The license for the Helsinki-NLP library is detailed in the `LICENCE` file.
  - For other libraries, after installing dependencies from `requirements.txt`, you can find their licenses in the `LICENCE` files located within the `.venv` directory.

## How to Use the Project

### Step 1: Set Up a Virtual Environment

Create a virtual environment with:

```bash
python -m venv .venv
```

### Step 2: Activate the Virtual Environment

- **On Windows:**

  ```bash
  .venv\Scripts\activate
  ```

- **On macOS/Linux:**

  ```bash
  source .venv/bin/activate
  ```

### Step 3: Install Dependencies

Install the required dependencies with:

```bash
pip install -r requirements.txt
```

### Step 4: Prepare a `.env` File

To run the project, ensure you have a `.env` file in the root directory of the project. This file should include your Discord API token in the following format:

```env
DISCORD_TOKEN='your_discord_token_here'
```

### Step 5: Configure Your IDE

Make sure to configure your virtual environment in your IDE (e.g., Visual Studio Code or your IDE of choice). For Visual Studio Code, follow these steps:

1. Open the Command Palette (Ctrl+Shift+P or Cmd+Shift+P on macOS).
2. Select `Python: Select Interpreter`.
3. Choose the interpreter located in `.venv` (e.g., `.venv/bin/python` or `.venv\Scripts\python.exe`).

Refer to your IDE's documentation if you're using a different tool.

## Contributing

Feel free to add new features, enhance existing ones, or expand the project in any way you see fit!
