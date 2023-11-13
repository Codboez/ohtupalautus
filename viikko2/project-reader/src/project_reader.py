from urllib import request
from project import Project
from toml import loads

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        content = request.urlopen(self._url).read().decode("utf-8")
        
        content_dict = loads(content)
        info = content_dict["tool"]["poetry"]

        return Project(info["name"], info["description"], info["license"], list(info["authors"]),
                       list(info["dependencies"]), list(info["group"]["dev"]["dependencies"]))
