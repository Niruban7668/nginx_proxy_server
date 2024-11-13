# NGINX Proxy Server with Python Web Application

This project demonstrates how to configure an NGINX proxy server to forward incoming traffic to a Python web application hosted locally. When users connect to the hosted nginx server's port, they are redirected to the Python web application and receive a response.

---

## Prerequisites

- **Ubuntu/Debian-based systems** (for NGINX installation instructions)
- **Python 3.11** installed with the required web framework (e.g., Flask).

---

## Installation and Setup

### Step 1: Install NGINX

To install NGINX on your system, follow these steps:

```
  sudo apt update
  sudo apt install nginx -y
```

Verify the installation by checking the NGINX version:

```
  nginx -v
```

Start and enable the NGINX service:
```
  sudo systemctl start nginx
  sudo systemctl enable nginx
```

### Step 2: Python Web Application

Refer to the following [Python code](./app.py) for hosting the web application. This app listens on 127.0.0.1 at port 5000.

#### Install flask

```
  pip install flask
```

### Step 3: NGINX Configuration

Refer to the following [Configuration file](./nginx.conf) to configure NGINX as a reverse proxy.

Steps to Apply Configuration:

1. Open the NGINX configuration file 

```
  sudo nano /etc/nginx/sites-available/default
```
2. Replace its contents with the above configuration.

3. Test the configuration for syntax errors:
```
  sudo nginx -t
```
4. Restart NGINX to apply the changes:
```
  sudo systemctl restart nginx
```

### Step 4: Testing the Setup

Start the Python web application by running:
```
  python3 app.py
```
Access the application through NGINX by navigating to http://localhost in your web browser or using curl:
```
    curl http://localhost/api/
```
If everything is configured correctly, you should see the response from the Python application.
