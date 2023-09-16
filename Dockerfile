# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Expose port 8501 for Streamlit
EXPOSE 8501

# Run streamlit command to start your app
CMD ["streamlit", "run", "Homepage.py"]

