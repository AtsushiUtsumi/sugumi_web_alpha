# エンティティ
from abc import ABCMeta, abstractmethod


class Project:
    project_id = ""
    project_name = ""
    project_description = ""


# リポジトリ
class ProjectRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_all(self) -> list[Project]:
        pass

    @abstractmethod
    def find_by_id(self, project_id: int) -> Project:
        pass

class ProjectRepositoryCsv(ProjectRepository):
    def __init__(self, file_name: str = 'project.csv'):
        self.file_name = file_name
        file = open(file_name, 'a')
        file.write("1, sugumi-web, SUGUMIのウェブバージョン\n")
        file.close()

    def find_all(self) -> list[Project]:
        projects = []
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                project_data = line.strip().split(',')
                project = Project()
                project.project_id = project_data[0]
                project.project_name = project_data[1]
                project.project_description = project_data[2]
                projects.append(project)
        return projects

    def find_by_id(self, project_id: int) -> Project:
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            for line in lines:
                project_data = line.strip().split(',')
                if int(project_data[0]) == project_id:
                    project = Project()
                    project.project_id = project_data[0]
                    project.project_name = project_data[1]
                    project.project_description = project_data[2]
                    return project
        return None