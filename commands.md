# Initializing Docker for getting selenium chrome

Run following command for get selenium chrome:
 > docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:latest

# Virtual Environment

### Create
> python -m venv .venv 

### Activate

- Linux
  
  > source /.venv/bin/activate

- Windows
  
  > .\\.venv\Scripts\activate


# Install Dependencies

> pip install -r requirements.txt

# Running Project with several url

> python screenshots.py \<urls>