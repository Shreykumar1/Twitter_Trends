# STIR Twitter Trends Viewer

## Overview

STIR Twitter Trends Viewer is a web application designed to fetch and display the top trending topics on Twitter. Utilizing technologies such as Selenium, ProxyMesh, and MongoDB, it provides a seamless experience for users to access real-time trends.

## Key Features

- **Automated Trend Fetching**: Logs into Twitter and retrieves the latest trending topics, storing them in a MongoDB database.
- **Proxy Support**: Integrates ProxyMesh for secure and anonymous web scraping.
- **User-Friendly Interface**: Presents trends with timestamps, IP addresses, and JSON records in a clean layout.
- **MongoDB Storage**: Ensures unique IDs for easy access to stored trends.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.8 or higher
- A MongoDB instance (local or cloud)
- Selenium WebDriver (Microsoft Edge)
- Node.js (optional for additional features)
- ProxyMesh credentials

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/TheCoderAdi/stir-webscrape-intern
   cd stir-webscrape-intern
   ```

2. **Install Dependencies**:
   Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Configuration**:
   Create a `.env` file in the root directory with the following content:
   ```plaintext
   TWITTER_USERNAME="your-twitter-username"
   TWITTER_PASSWORD="your-twitter-password"
   MONGO_URI="mongodb://localhost:27017"
   PROXYMESH_USERNAME="your-proxymesh-username"
   PROXYMESH_PASSWORD="your-proxymesh-password"
   ```

### Running the Application

1. **Start the Flask Server**:
   ```bash
   python app.py
   ```

2. **Access the Application**:
   Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB
- **Web Scraping**: Selenium
- **Proxy Management**: ProxyMesh
