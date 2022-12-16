# Flask REST-API
Simple Rest API created with Flask

### Dependencies

- Python 3.10.6
- pip3
- docker-compose

## Running 
**Clone the repository**

```
~$ git clone https://github.com/lspaulucio/flask-rest-api.git
```

Once all dependencies are installed run the following command to install the necessary python packages.

```bash
~$ pip3 install -r requirements.txt
```

On linux terminal, go to project folder and execute the command to start the services:

  ```bash
  ~$ docker-compose up
  ```

(Optional) If you have cmake installed you also can run the following command to start the services:
  ```bash
  ~$ make compose
  ```

Once the services are up, you can access the API's swagger documentation at http://127.0.0.1:5000/api-docs

