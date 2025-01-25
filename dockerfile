# Use a base image with necessary libraries
FROM ubuntu:22.04

# Install dependencies and add the PPA
RUN apt-get update && apt-get install -y \
    software-properties-common \
    && add-apt-repository ppa:xtradeb/apps \
    && apt-get update \
    && apt-get install -y \
    ungoogled-chromium \
    chromium-chromedriver \
    libnss3 \
    libgbm1 \
    libatk-bridge2.0-0 \
    libgtk-3-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    libxshmfence1 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install Selenium
RUN pip3 install selenium webdriver-manager beautifulsoup4

# Copy your Selenium script into the container
COPY newtest.py /app/newtest.py

# Set working directory
WORKDIR /app

# Command to run the script
CMD ["python3", "/app/newtest.py"]
