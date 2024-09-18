# Remote Learning Platform (New Learning System)

## Overview

Welcome to the Django Application. This project make the solution for the statement "Remote education can be challenging due to the lack of effective tools for course management, student engagement, and assessment".





## Installation and Setup Instructions

1. **Clone the Repository:**
    ```sh
   [ https://github.com/SARAN-SMART-2004/Remote-Learning-Platform.git](https://github.com/SARAN-SMART-2004/Remote-Learning-Platform.git)
    cd Remote-Learning-Platform
    ```
    or
2. **Download from githubt:**
    ```sh
    cd Remote-Learning-Platform
    ```
   

3. **Create and Activate a Virtual Environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate 
    ```
4. **Install Dependencies:**
    ```sh
    pip install -r requirements.txt 
    ```

5. **Configure Environment Variables:**
    Create a `.env` file in the root directory and add:
    ```env
    SECRET_KEY=your_secret_key
    DEBUG=True
    EMAIL_SERVICE=your_email_service_provider
    EMAIL_HOST_USER=your_email@example.com
    EMAIL_HOST_PASSWORD=your_email_password
    # Recaptcha keys
    RECAPTCHA_PUBLIC_KEY=your key
    RECAPTCHA_PRIVATE_KEY=your key
    # Twilio settings
    TWILIO_ACCOUNT_SID=your key
    TWILIO_AUTH_TOKEN=your key
    TWILIO_PHONE_NUMBER= your numbr
    ```

4. **Set Up the Database:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    ```
 5. **Run the Development Server:**
    ```sh
    python manage.py runserver
    ```


5. **Access the Application:**
    Open your browser and navigate to `(http://127.0.0.1:8000/)`



## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contact
If you want to contribute to this project, please fork the repository and submit a pull request.
For any inquiries, please contact saran152004s@gmail.com.








