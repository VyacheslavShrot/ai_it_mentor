import subprocess

if __name__ == "__main__":
    """
            Here you can perform actions before starting the services
    """
    server_process = subprocess.Popen(["python", "server_run.py"])
    consumer_process = subprocess.Popen(["python", "kafka_run.py"])

    server_process.wait()
    consumer_process.wait()
