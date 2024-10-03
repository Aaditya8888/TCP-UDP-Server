## Secure TCP/UDP Message Receiving Server

### Overview
This server application is designed to communicate securely over TCP and UDP protocols. It ensures message confidentiality, integrity, and security using encryption and user authentication. The server can receive both plain text and files (images, audio, documents) while maintaining security through AES-256 encryption and virus scanning.

### Features:
1. **Login Functionality with bcrypt Hashing**:  
   The server securely stores your credentials by hashing the username and password using the **bcrypt** algorithm when logging in. This ensures that your credentials are never stored in plain text, providing a higher level of security.
   
2. **Anonymous Message Reception**:  
   Users can choose to receive messages anonymously without requiring a login.

3. **Message Encryption**:  
   Messages are encrypted using **AES-256** encryption to ensure that any communication between clients and the server remains confidential. Man-in-the-middle or other eavesdropping attacks are mitigated using this encryption method.

4. **Protocol Selection**:  
   Users can choose between TCP (reliable, connection-oriented) or UDP (fast, connectionless) protocols for message reception.

5. **Message Storage (for Logged-in Users Only)**:  
   Messages are stored in encrypted format (AES-256) for logged-in users. Only the last 5 messages will be stored and displayed when requested.

6. **File Reception with Antivirus Scanning**:  
   If using UDP, users can receive files in multiple formats (images, audio, PDFs, etc.). The server scans these files for authenticity using **ClamAV** to ensure they are free from malware. Files are only available for download after passing the scan.

7. **User Input Validation**:  
   Any invalid input will prompt the user with instructions to follow the proper usage format.

8. **Notice**:  
   Users are reminded that this tool is intended for legal use only and should not be employed for malicious purposes.

### Getting Started

1. **Installation**:  
   - Ensure you have Python 3 installed.
   - Install required modules:
     ```
     pip install pycryptodome bcrypt clamd
     ```

2. **Running the Server**:  
   Run the `tcp_udp_server.py` script. The server will display a banner and prompt you for login credentials or anonymous mode, as well as whether to use TCP or UDP for message reception.

3. **Message Encryption**:  
   All messages are encrypted with AES-256, ensuring confidentiality.

4. **File Scanning**:  
   Files received via UDP are scanned for viruses using ClamAV before being made available for download.

### Usage

1. Upon starting, you'll be prompted to either:
   - Login with a **bcrypt-hashed username and password**, or 
   - Continue anonymously.
   
2. Select either TCP or UDP for communication.  
   - In **TCP mode**, messages will be received with reliable delivery.  
   - In **UDP mode**, messages are received quickly without guaranteed delivery, and you can receive files.

### License
This tool is provided for educational and legal use only. Ensure you're complying with applicable laws and regulations when using this application.

---
