# Student Study Tracker
## Overview  
A simple command-line Python application built using object-oriented programming. It lets users register, login, add study sessions, and view reports summarizing their habit and study times by subject.

## Features  
- User registration and login  
- Add study sessions with subject, date, duration, and breaks  
- View total study time and breakdown per subject  
- Easy-to-use command-line interface  
- Modular design with separate classes and files  

## Technologies Used  
- Python 3  
- Basic OOP concepts (Classes for User, StudySession, Tracker)  
- No external libraries  

## How to Use  
1. Clone or download the repository.  
2. Run main.py (e.g., python main.py) to start the program.  
3. At the start menu, choose to Register, Login, or Exit.  
4. After login, add sessions or view your study report.  
5. Logout to switch users or exit the program.

## Project Structure  
- main.py — program entry point and user interface menus  
- user.py — defines User class handling user data and sessions  
- session.py — defines StudySession class  
- tracker.py — defines Tracker class managing users and workflow  

## Testing Instructions

### Manual Testing  
- *Register User:* Try registering multiple users. Test for duplicate usernames.  
- *Login:* Test login with correct and incorrect credentials.  
- *Add Study Sessions:* Add sessions with valid and invalid inputs (e.g., non-numeric durations).  
- *View Reports:* After adding study sessions, check if total and subject-wise times are correct.  
- *Logout:* Check logout functionality returns to main menu correctly.  
- *Exit Program:* Ensure the program exits cleanly at any point when chosen.

### Suggested Test Cases  
- Register user “Alice”, add 2 sessions in Math and English, verify report.  
- Try to register “Alice” again (should fail).  
- Login with wrong password (should fail) and correct password (should pass).  
- Add sessions with zero break time and non-zero break time, verify effective time calculation.  
- Logout and login as another user, verify separation of data.

### Tips  
- Run program multiple times to simulate user experience.  
- Carefully input invalid data deliberately to test error handling robustness.
  <img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/72b4650d-0d20-46bb-89a1-83695f626dbe" />
  <img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/08a5a5de-1df1-4a82-b179-4ea7eac4fe2f" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/0ee24f6e-b9bc-4d0c-b45f-069bbaffdcbd" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/628bcf75-9214-4442-8239-5284f3dfeb06" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/68179f68-ff37-4441-8e82-100a707051de" />

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/3d815e27-b6d4-45d8-8db1-09ab3fef53b2" />
