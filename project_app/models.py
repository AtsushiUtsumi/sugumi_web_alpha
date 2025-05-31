from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.TextField()
    
    def __str__(self):
        return self.project_name


class ProjectRepository:
    def find_all(self):
        pass
    
    def find_by_id(self, project_id):
        pass


class ProjectRepositoryCsv(ProjectRepository):
    def __init__(self, file_name='project.csv'):
        self.file_name = file_name
        try:
            with open(file_name, 'a') as file:
                file.write("1, sugumi-web, SUGUMIのウェブバージョン\n")
        except Exception:
            pass

    def find_all(self):
        projects = []
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip():
                        project_data = line.strip().split(',')
                        if len(project_data) >= 3:
                            project = type('Project', (), {})()
                            project.project_id = project_data[0].strip()
                            project.project_name = project_data[1].strip()
                            project.project_description = project_data[2].strip()
                            projects.append(project)
        except Exception:
            pass
        return projects

    def find_by_id(self, project_id):
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    if line.strip():
                        project_data = line.strip().split(',')
                        if len(project_data) >= 3 and int(project_data[0].strip()) == project_id:
                            project = type('Project', (), {})()
                            project.project_id = project_data[0].strip()
                            project.project_name = project_data[1].strip()
                            project.project_description = project_data[2].strip()
                            return project
        except Exception:
            pass
        return None
