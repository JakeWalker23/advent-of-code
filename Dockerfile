FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
# If you have any dependencies, uncomment the next line and add a requirements.txt file
# RUN pip install --no-cache-dir -r requirements.txt

# Add a script to run solutions
COPY run_solution.sh /usr/src/app

# Make the script executable
RUN chmod +x /usr/src/app/run_solution.sh

# Command template to be overridden by `docker run` arguments
CMD ["./run_solution.sh"]
