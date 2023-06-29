# Timer Project

This project is a web application that implements the Pomodoro Technique timer using Python Django.

## Features

- Start the timer with a specified duration.
- Stop the timer and resume it later.
- Reset the timer to its original duration.

## Technologies Used

- Python
- Django
- Django REST Framework

## Installation

1. Clone the repository:
   ```shell
   git clone https://github.com/your-username/codemunk.git
   cd codemunk
   ```

2. Create a virtual environment:
   ```shell
   python -m venv venv
   ```

3. Activate the virtual environment:
   - For Windows:
     ```shell
     venv\Scripts\activate
     ```
   - For Linux/macOS:
     ```shell
     source venv/bin/activate
     ```

4. Install the dependencies:
   ```shell
   pip install -r requirements.txt
   ```

5. Apply the database migrations:
   ```shell
   python manage.py migrate
   ```

6. Run the development server:
   ```shell
   python manage.py runserver
   ```

7. Access the application at `http://localhost:8000` in your web browser.

## API Endpoints

- `POST /api/timer/start`: Start the timer.
  - Request body:
    ```json
    {
      "duration": 25
    }
    ```
  - Response body:
    ```json
    {
      "status": "success",
      "message": "Timer started successfully.",
      "remaining_time": 1500,
      "is_running": true
    }
    ```

- `POST /api/timer/stop`: Stop the timer.
  - Response body:
    ```json
    {
      "status": "success",
      "message": "Timer stopped successfully.",
      "remaining_time": 1480,
      "is_running": false
    }
    ```

- `POST /api/timer/reset`: Reset the timer.
  - Response body:
    ```json
    {
      "status": "success",
      "message": "Timer reset successfully.",
      "remaining_time": 1500,
      "is_running": false
    }
    ```

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Open a pull request to the original repository.


## Acknowledgments

- [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
