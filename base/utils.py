from collections import defaultdict

def folder_structure_html(key, value):
    if value == 'file':
        return f'<li class="file"><span class="file-name">{key}</span></li>'
    else:
        html = f'<li class="folder"><span class="folder-name">{key}</span><ul>'
        for k, v in sorted(value.items()):
            html += complete_folder_structure(k, v)
        html += '</ul></li>'
    return html

def get_folder_structure(contents, repo, path=""):
    structure = {}
    for content in contents:
        if content.type == "dir":
            structure[content.name] = get_folder_structure(repo.get_contents(content.path), repo, path=content.path)
        else:
            
            structure[content.name] = "file"
    return structure

def build_folder_structure(contents):
    structure = defaultdict(dict)
    for item in contents:
        try:
            path_parts = item.path.split('/')
            current = structure
            for part in path_parts[:-1]:
                current = current[part]
            if item.type == 'blob':
                current[path_parts[-1]] = "file"
            elif item.type == 'tree':
                current[path_parts[-1]] = {}
        except Exception as e:
            print(f"Error processing item {item.path}: {str(e)}")
            continue
    return dict(structure)