from django.shortcuts import render
from django.http import HttpResponse
from .models import ProjectRepositoryCsv
import os


project_repository = ProjectRepositoryCsv()


def hello(request, name=None):
    try:
        with open('test.txt', 'a') as file:
            file.write("HOGE\n")
        with open('test.txt', 'r') as file:
            lines = file.readlines()
        if len(lines) > 3:
            return render(request, 'jss.html', {'name': lines})
        return render(request, 'hello.html', {'name': name})
    except Exception:
        return render(request, 'hello.html', {'name': name})


def project_list(request):
    rows = project_repository.find_all()
    return render(request, 'hello.html', {'name': str(len(rows)) + "件のプロジェクトがあります"})


def project_detail(request, project_id):
    try:
        entity = project_repository.find_by_id(int(project_id))
        if entity is None:
            return render(request, 'hello.html', {'name': "プロジェクトが見つかりません"})
        return render(request, 'hello.html', {'name': entity.project_name})
    except Exception:
        return render(request, 'hello.html', {'name': "プロジェクトが見つかりません"})
