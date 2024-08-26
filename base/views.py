from github import Github
from django.http import HttpResponse
from django.shortcuts import render
from .utils import get_folder_structure, build_folder_structure



def get_repo_structures(request):
    return render(request, "base/index.html")

def repostructure(request):
    if request.POST:
        repo_url = request.POST.get('repo', None)

        # Github username
        username = "akhil484"
        # pygithub object
        g = Github('')
        
        try:
            parts = repo_url.strip('/').split('/')
            repo_owner = parts[-2]
            repo_name = parts[-1]
            # Get the repository object
            repo = g.get_repo(f"{repo_owner}/{repo_name}")
            
            # Get all contents at once
            all_contents = repo.get_git_tree(repo.default_branch, recursive=True).tree
            folder_structure = build_folder_structure(all_contents)
        except Exception as e:
            return render(request, "base/folder_struct.html", {'error': True, 'error_msg': f'An error has occurred: {str(e)}. Please make sure your URL is correct and corresponds to a repository on GitHub.'})
        
        return render(request, "base/folder_struct.html", {'error': False, 'repo_url': repo_url, 'folder_structure': folder_structure})