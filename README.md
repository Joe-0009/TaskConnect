# TaskConnect

TaskConnect is a web application that connects users with professionals for various tasks such as plumbing, electrical work, gardening, and more.

## Table of Contents
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- User Registration and Login
- Profile Management for Users and Workers
- Job Posting and Viewing

## Tech Stack
- **Frontend**: React
- **Backend**: Flask
- **Database**: PostgreSQL

## Installation

### Prerequisites
- Python 3.x
- Node.js
- PostgreSQL

### Backend Setup
1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/taskconnect.git
    cd taskconnect
    ```
2. Create a virtual environment and activate it:
    ```bash
    python3 -m venv env
    source env/bin/activate
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the PostgreSQL database and update the configuration in `config.py`.

### Frontend Setup
1. Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2. Install the required packages:
    ```bash
    npm install
    ```
3. Start the development server:
    ```bash
    npm start
    ```

## Usage
1. Start the backend server:
    ```bash
    flask run
    ```
2. Open your browser and go to `http://localhost:3000` to access the application.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License.
