# UpBeat

UpBeat is a simple music streaming application built with Python and React, aimed at enhancing your music listening experience.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)

## Features

- **User-Friendly Interface:** Intuitive design for easy navigation and seamless music playback.
- **Search and Discover:** Explore a vast library of music and discover new tracks based on your preferences.
- **Playlist Management:** Create and manage personalized playlists to curate your favorite songs.

## Installation

### Backend

1. **Prerequisites:** Ensure you have [Python](https://www.python.org/) and [PostgreSQL](https://www.postgresql.org/) installed on your system.

2. **Clone Repository:** Clone the UpBeat backend repository to your local machine:
    ```
    https://github.com/hajarLamharchi/UpBeat.git
    ```

3. **Set Up PostgreSQL Database:**

    - Install PostgreSQL on your local machine.
    - Create a PostgreSQL user and database named "Upbeat", and note down the username, password, and host.


4. **Install Backend Dependencies:** Install the required Python dependencies:
    ```
    cd server 
    pip install -r requirements.txt
    ```

5. **Set Up Environment Variables:** Add the following environment variables to get the app started. These variables should include your PostgreSQL credentials, Flask secret key, Spotify API client ID and secret, mail server configuration, and server host.
    ```
    export DB_USERNAME=<your_db_username>
    export DB_PASSWORD=<your_db_password>
    export DB_HOST=<your_db_host>
    export DB_NAME=<your_db_name>
    export FLASK_SECRET_KEY=<your_flask_secret_key>
    export SPOTIFY_CLIENT_ID=<your_spotify_client_id>
    export SPOTIFY_CLIENT_SECRET=<your_spotify_client_secret>
    export MAIL_SERVER=<your_mail_server>
    export MAIL_PORT=<your_mail_port>
    export MAIL_USERNAME=<your_mail_username>
    export MAIL_PASSWORD=<your_mail_password>
    export MAIL_SALT=<your_mail_salt>
    export SERVER_HOST=<your_server_host>
    ```

6. **Start the Backend Server:** From the backend directory, run the Flask server:
    ```
    python app.py
    ```

### Frontend

1. **Prerequisites:** Ensure you have [Node.js](https://nodejs.org/) installed on your system.

2. **Install Frontend Dependencies:** Navigate to the frontend directory and install the required npm packages:
    ```
    cd client
    npm run dev
    ```

## Usage

1. **Set Up Environment Variables:** Before running the frontend application, ensure that the backend server is running and the necessary environment variables are set up as specified in the backend README.

2. **Start the Frontend Server:** From the frontend directory, start the React development server:
    ```
    npm start
    ```

3. **Access the Application:** Open your web browser and navigate to the URL where the frontend server is running (by default, http://localhost:5173/).
