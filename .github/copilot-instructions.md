# Copilot Instructions for KTH Medical Messaging App

## Project Overview
- This is a Python desktop application for medical messaging, using Tkinter (via `customtkinter`) for the GUI and MongoDB (via `pymongo`) for data storage.
- The main entry point is `main.py`, which launches the GUI via `start_app()` from `GUI.py`.
- The app supports user authentication and role-based access (doctor, nurse, patient).

## Major Components
- `main.py`: Application entry point. Runs the GUI.
- `GUI.py`: Defines the main window and layout using `customtkinter`. Example: `GUI_Interface` class for window management.
- `auth.py`: Handles user login and role management. All authentication logic should be routed here.
- `database.py`: Contains MongoDB connection and messaging functions. Use this for all database interactions.
- `requirements.txt`: Only external dependency is `pymongo` (MongoDB driver).

## Developer Workflows
- **Run the app:**
  ```powershell
  python main.py
  ```
- **Install dependencies:**
  ```powershell
  pip install -r requirements.txt
  ```
- **Debugging:**
  - GUI errors: Check `GUI.py` for window/layout issues.
  - Database errors: Check `database.py` for connection and query logic.
- **Testing:**
  - No test framework detected. Add tests in a new `tests/` folder if needed.

## Patterns & Conventions
- All GUI logic is centralized in `GUI.py` using the `GUI_Interface` class.
- Authentication and role logic is separated in `auth.py`.
- Database access is abstracted in `database.py`; do not access MongoDB directly from GUI or auth modules.
- Use role-based logic for user flows (doctor, nurse, patient).
- Use `customtkinter` for all window creation and layout.

## Integration Points
- MongoDB is the only external service; connection details should be managed in `database.py`.
- No other external APIs or services detected.

## Examples
- To create a new window:
  ```python
  GUI_Interface("Window Title")
  ```
- To authenticate a user:
  ```python
  # Use functions in auth.py
  ```
- To send/get messages:
  ```python
  # Use functions in database.py
  ```

## Key Files
- `main.py`, `GUI.py`, `auth.py`, `database.py`, `requirements.txt`

---
_If any section is unclear or missing, please provide feedback for improvement._
