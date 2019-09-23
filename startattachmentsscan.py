from locust import HttpLocust, TaskSet, task
import json

class WebsiteTasks(TaskSet):
    @task
    def send(self):
        with open('startattachmentsscan.txt') as json_file:
            jsonData = json.load(json_file)

            self.client.post(
                url="/suminda/startattachmentsscan",
                data=json.dumps(jsonData),
                auth=None,
                headers={"content-type":"application/json", "jwt_token": "test"}
            )

class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000