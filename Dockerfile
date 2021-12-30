FROM python:3.9

# Set app workdir
WORKDIR /usr/src/app

# Expose port
EXPOSE 80

# Copy dependencies list
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt && pip install setuptools 

# Copy app sources
COPY . .

# Install app
RUN pip install .

# Run app
CMD ["db0mb3r", "--ip", "0.0.0.0", "--port", "80"]

