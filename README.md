# Client-Server Authentication Example

This Python script demonstrates a basic client-server authentication mechanism using RSA key pairs for encryption and signing. It includes a Flask-based server and detailed step-by-step client output.

## Usage

1. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. Flask Configuration:

   This client-server authentication example uses Flask for the server. You can customize Flask settings by exporting environment variables or editing the `server.py` file.

   - **FLASK_APP:** Set this variable to specify the main Flask application file (default is `server.py`).

     ```bash
     export FLASK_APP=server.py
     ```

   - **FLASK_ENV:** Set this variable to control the environment (development, production, etc.). For development, use:

     ```bash
     export FLASK_ENV=development
     ```

     For production, use:

     ```bash
     export FLASK_ENV=production
     ```

   - **FLASK_RUN_HOST:** This variable determines the host on which Flask runs. By default, it's set to `127.0.0.1` (localhost).

     ```bash
     export FLASK_RUN_HOST=0.0.0.0  # To allow external access
     ```

   - **FLASK_RUN_PORT:** This variable sets the port on which Flask runs. The default is `5000`.

     ```bash
     export FLASK_RUN_PORT=8080
     ```

   You can adjust these environment variables to suit your project's needs. Refer to the Flask documentation for more configuration options.

3. Start the Flask server:

   ```bash
   flask run
   ```

   By default, the server runs on port 5000.

4. Run the client:

   ```bash
   python client.py
   ```

   Follow the detailed output to understand the authentication process.

## Dependencies

- Flask 2.1.1
- cryptography 36.0.0
- requests 2.26.0
