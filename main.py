class Logger:
    def log(self, msg):
        print(msg)

class Service:
    def __init__(self, logger):
        self.logger = logger

    def run(self):
        self.logger.log("service run")

Service(Logger()).run()
