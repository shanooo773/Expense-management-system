# Expense Management System

This project is an expense management system that consists of a Streamlit frontend application and a FastAPI backend server.


## Project Structure

- **frontend/**: Contains the Streamlit application code.
- **backend/**: Contains the FastAPI backend server code.
- **tests/**: Contains the test cases for both frontend and backend.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.

- <img width="700" height="615" alt="image" src="https://github.com/user-attachments/assets/c4573f98-856a-463b-b3b6-2e01e0be01c1" />
- <img width="638" height="727" alt="image" src="https://github.com/user-attachments/assets/829cf22e-73c1-418e-b5ec-ee948e651b59" />
- <img width="613" height="582" alt="image" src="https://github.com/user-attachments/assets/bdbf2f4a-46c7-468a-a291-a40a8ec98582" />


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shanooo773/Expense-management-system.git
   cd Expense-management-system
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn server.server:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run frontend/app.py
   ```
