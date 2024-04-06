# Use the official Python base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app_code

# Copy the requirements file to the working directory
COPY ./requirements.txt /app_code/requirements.txt

# Install the Python dependencies
RUN pip install --no-cache-dir --upgrade -r /app_code/requirements.txt

# Copy the code to the working directory
COPY ./app /app_code/app

# Expose the port on which the application will run
EXPOSE 8000

# Run the FastAPI application using uvicorn server
CMD ["uvicorn", "app.main:app", "--port", "8000"]
