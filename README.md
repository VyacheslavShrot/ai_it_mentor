# AI IT Mentor

### STRUCTURE

- FastAPI project with endpoints 
that can be used to upload a roadmap file generated from a gpt model to the computer


- OpenAI library for working with gpt is used
```
openai==1.14.2
```

- I use the kafka-python libraries to work with Kafka
```
kafka-python==2.0.2
```

- FastAPI service is started via Uvicorn
```
uvicorn==0.29.0
```


- The generation process from OpenAI and the file upload process
takes place on the Kafka side, which is connected via docker-compose


- The configuration is located in the .env_dev file
  - To change it to another file, modify the following line in src/app.py
```
env.read_env('.env') -> .env set to the new env file
```

- The startup is done with the src/manage.py
file and in this file you can add other startups before or after the services are started
```
import subprocess

if __name__ == "__main__":
    """
            Here you can perform actions before starting the services
    """
    server_process = subprocess.Popen(["python", "server_run.py"])
    consumer_process = subprocess.Popen(["python", "kafka_run.py"])

    server_process.wait()
    consumer_process.wait()
```


### INSTALLATION

- I hope you already have python, pip and docker installed


- Copy this repository to your system
```
https://github.com/VyacheslavShrot/ai_it_mentor.git
```

- Install requirements.txt
```
pip install -r requirements.txt
```

- To configure the Kafka queue retention period, specify the desired number of milliseconds
on a line in the "docker-compose.yml" file
  - Where 86400000 is 24 hours of queue storage
```
KAFKA_LOG_RETENTION_MS: "86400000"
```

- Create an .env file at the src level of the directory (ai_it_mentor/.env)
  - Define OPENAI_API_KEY variable to work with gpt
```
OPENAI_API_KEY=sk-lb...
```


### START

- Start Docker-Compose, where services are defined to work with Kafka
```
docker-compose up -d
```

- Go to the work directory
```
cd src
```

- Start FastAPI and Kafka services
```
python3 manage.py
```

