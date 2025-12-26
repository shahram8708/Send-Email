# Send Email – Flask Application

Send Email is a Flask-based web application that allows users to send emails through any SMTP server using a simple web interface. The application provides fields to enter SMTP credentials, compose an email, and send it securely using TLS. It also includes a page to view previously sent emails, which are stored locally in the browser using LocalStorage.

The project focuses on simplicity, usability, and client-side management of sent email history.

---

## Overview

The application includes:

* A Flask backend to serve pages and handle email sending.
* An email form interface where users provide SMTP details and compose an email.
* Secure sending using TLS with Python’s `smtplib`.
* A “Sent Emails” page that displays previously sent emails saved in LocalStorage.
* A clean, responsive UI with inline styling.
* Debug mode enabled by default.

---

## Features

* Web interface to send emails via SMTP
* Fields for:

  * SMTP server
  * SMTP port
  * SMTP username
  * SMTP password (with show/hide toggle)
  * Sender email
  * Receiver email
  * Subject
  * Message body
* Sends email using TLS
* Displays success / failure response
* Stores sent email details in browser LocalStorage
* View/Delete sent email history on a dedicated page
* Responsive, styled UI
* Runs locally using Flask

---

## Tech Stack

**Backend**

* Python
* Flask
* smtplib
* email.mime

**Frontend**

* HTML
* CSS (inline)
* JavaScript (fetch + LocalStorage)

Dependencies are listed in `requirements.txt`.

---

## Project Structure

```
Send-Email-main/
│
├── app.py                      # Flask backend + email sending logic
├── requirements.txt            # Python dependencies
│
└── templates/
    ├── index.html              # Email sender form UI
    └── emails.html             # Sent emails history UI
```

---

## Installation

1. Ensure Python is installed.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The app runs in debug mode and is typically available at:

```
http://127.0.0.1:5000/
```

---

## Usage

### Send an Email

1. Open the application in your browser.
2. Fill in:

   * SMTP server details
   * Login credentials
   * Sender and recipient email addresses
   * Subject and message
3. Click **Send Email**.
4. The application will:

   * Attempt SMTP connection with TLS
   * Login
   * Send the email
   * Return a JSON success or failure message
5. The email details are saved to LocalStorage for history.

### View Sent Emails

1. Click **View Emails** from the main page, or visit:

```
/emails
```

2. View:

   * From
   * To
   * Subject
   * Message
   * Timestamp
3. Delete entries if desired.

---

## Notes

* SMTP credentials are entered manually in the form; no environment configuration is required.
* Sent emails are stored only in the browser’s LocalStorage, not on the server.
* The application runs in debug mode by default.
* There is no license file included in this project.
