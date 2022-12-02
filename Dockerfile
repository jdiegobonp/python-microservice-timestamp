FROM python:3.8-alpine
# Define workdir /app
COPY ./requirements.txt /app/requirements.txt
# Execute pipe install to apply the libraries required.
WORKDIR /app
# Copy requirements.txt to container
RUN pip install -r requirements.txt
# Copy all files inside the container
COPY . /app
# Configure the container to run in an executed manner
ENTRYPOINT [ "python" ]
# Execute python file
CMD ["main.py" ]
