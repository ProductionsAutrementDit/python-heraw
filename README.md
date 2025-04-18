# Heraw Python SDK

A Python client for the Heraw API with full type annotations.

## Installation

```bash
pip install heraw
```

## Usage

```python
from heraw import Heraw

# Initialize the client with your API key
client = Heraw(api_key="your_api_key")

# Work with projects
projects = client.list_projects(workspace_name="my-workspace")
for project in projects:
    print(f"Project: {project['name']} ({project['uuid']})")
    if project.get('company'):
        print(f"  Company: {project['company']['name']}")
    print(f"  Status: {project['status']}")
    print(f"  Created: {project['created']}")

# Create a new project
new_project = client.create_project({
    "name": "New Project",
    "startDate": "2024-04-01T00:00:00.000Z",
    "endDate": "2024-06-30T00:00:00.000Z",
    "companyName": "ACME Inc.",
    "disableCasts": False
}, workspace_name="my-workspace")

# Work with files
file = client.upload_file({
    "folderUuid": new_project["folderUuid"],
    "uploadGroup": ""
}, workspace_name="my-workspace", file_path="video.mp4)

# Work with folders
folder = client.get_folder(new_project["folderUuid"], workspace_name="my-workspace")
content = client.get_folder_content(new_project["folderUuid"], workspace_name="my-workspace")
```

## Type Annotations

This SDK includes complete TypedDict definitions for all API resources, providing IDE autocompletion and type checking:

```python
from heraw import Heraw, ProjectDict, FileDict

# All methods return properly typed objects
projects: List[ProjectDict] = client.list_projects(workspace_name="my-workspace")
project: ProjectDict = client.get_project("project-123", workspace_name="my-workspace")

# Project resource example
"""
{
    "uuid": "00000000-0000-0000-0000-000000000001",
    "name": "Example Project",
    "startDate": "2023-01-01T00:00:00.000Z",
    "endDate": "2023-02-01T00:00:00.000Z",
    "created": "2023-01-15T10:30:00.000Z",
    "updated": "2023-01-16T14:25:00.000Z",
    "status": "IN_PROGRESS",
    "folderUuid": "00000000-0000-0000-0000-000000000002",
    "castsDisabled": false,
    "hasCast": false,
    "hasStats": false,
    "user": "00000000-0000-0000-0000-000000000003",
    "company": {
        "uuid": "00000000-0000-0000-0000-000000000004",
        "name": "Example Company",
        "color": "#3f51b5"
    },
    "role": null,
    "isFavorite": false,
    "color": "#000000",
    "logoUrl": "https://example.com/logo.png",
    "backgroundUrl": null,
    "size": 12345678,
    "hasNotificationSettings": true,
    "team": null,
    "taskCounts": {
        "projectUuid": "00000000-0000-0000-0000-000000000001",
        "toDo": 5,
        "inProgress": 3,
        "toValidate": 2,
        "done": 10
    }
}
"""
```

## Authentication

You need to create an API key from the heraw dashboard and provide it when initializing the client.

## API Reference

### Client Initialization

```python
from heraw import Heraw

# Default base URL is https://app.heraw.com/public/v1
client = Heraw(api_key="your_api_key")

# Custom base URL
client = Heraw(api_key="your_api_key", base_url="https://custom-instance.heraw.com/public/v1")
```

### Entities API

Methods for working with entities:
- `list_entities(workspace_name) -> List[EntityDict]`: List all entities in a workspace
- `create_entity(data, workspace_name) -> EntityDict`: Create an entity
- `update_entity(entity_uuid, data, workspace_name) -> EntityDict`: Update an entity
- `delete_entity(entity_uuid, workspace_name) -> Dict[str, Any]`: Delete an entity

### Projects API

Methods for working with projects:

- `list_projects(workspace_name) -> List[ProjectDict]`: List all projects in a workspace
- `create_project(data, workspace_name) -> ProjectDict`: Create a new project
- `get_project(project_uuid, workspace_name) -> ProjectDict`: Get a project by UUID
- `update_project(project_uuid, data, workspace_name) -> ProjectDict`: Update a project
- `delete_project(project_uuid, workspace_name) -> Dict[str, Any]`: Delete a project
- `update_project_status(project_uuid, status) -> ProjectDict`: Update a project's status
- `search_projects(criteria, workspace_name) -> Dict[str, Any]`: Search for projects
- `get_project_custom_fields(project_uuid, workspace_name) -> Dict[str, Any]`: Get custom fields for a project
- `set_project_custom_fields(project_uuid, data, workspace_name) -> Dict[str, Any]`: Set custom fields for a project
- `get_project_teams(project_uuid, workspace_name) -> Dict[str, Any]`: Get teams for a project

### Files API

Methods for working with files:

- `list_files(workspace_name, params) -> List[FileDict]`: List files in a workspace
- `create_file(data, workspace_name) -> FileDict`: Create a new file entry to be uploaded
- `upload_file(data, workspace_name, file_path) -> FileDict`: Upload a file to a folder
- `delete_file(file_uuid, workspace_name) -> Dict[str, Any]`: Delete a file
- `delete_file_permanently(file_uuid, workspace_name) -> Dict[str, Any]`: Delete a file permanently
- `update_file_status(file_uuid, status, workspace_name) -> FileDict`: Update file status
- `get_file_version(file_uuid, file_version, workspace_name, params) -> FileDict`: Get a file version
- `create_file_version(file_uuid, data, workspace_name) -> FileDict`: Create a new version of a file
- `get_file_subtitles(file_uuid, file_version, workspace_name, params) -> List[SubtitleDict]`: Get file subtitles
- `get_file_custom_fields(file_uuid, workspace_name) -> Dict[str, Any]`: Get custom fields for a file
- `set_file_custom_fields(file_uuid, data, workspace_name) -> Dict[str, Any]`: Set custom fields for a file
- `ingest_file(data, workspace_name) -> Dict[str, Any]`: Upload a file creating missing folders
- `ingest_file_from_s3(data, workspace_name) -> Dict[str, Any]`: Upload from S3 source

### Folders API

Methods for working with folders:

- `get_folder(folder_uuid, workspace_name) -> FolderDict`: Get a folder
- `delete_folder(folder_uuid, workspace_name) -> Dict[str, Any]`: Delete a folder
- `create_folder(data, workspace_name) -> FolderDict`: Create a folder
- `get_folder_content(folder_uuid, workspace_name, basic) -> FolderContentDict`: Get folder content
- `invite_users_to_folder(folder_uuid, data, workspace_name) -> Dict[str, Any]`: Invite users to a folder
- `set_folder_teams(folder_uuid, team_uuids, workspace_name) -> Dict[str, Any]`: Set teams for a folder

### Casts API

Methods for working with casts:

- `list_casts(workspace_name, project_uuid) -> List[CastDict]`: List casts
- `create_cast(data, workspace_name) -> CastDict`: Create a new cast
- `update_cast(cast_uid, data, workspace_name) -> CastDict`: Update a cast
- `delete_cast(cast_uid, workspace_name) -> Dict[str, Any]`: Delete a cast
- `share_cast(cast_uid, data, workspace_name) -> Dict[str, Any]`: Share a cast

### Custom Fields API

Methods for working with custom fields:

- `list_custom_fields(workspace_name) -> List[CustomFieldDict]`: List all custom fields for a workspace
- `create_custom_field(data, workspace_name) -> CustomFieldDict`: Create a custom field
- `update_custom_field(custom_field_uuid, data, workspace_name) -> CustomFieldDict`: Update a custom field
- `delete_custom_field(custom_field_uuid, workspace_name) -> Dict[str, Any]`: Delete a custom field

### Search API

Methods for searching:

- `search(query, workspace_name, contexts, folder_uuid) -> SearchResultDict`: Search for files, folders, comments

### Subtitles API

Methods for working with subtitles:

- `get_subtitle(subtitle_uuid, workspace_name, format, timestamp) -> Union[SubtitleDict, Dict[str, Any]]`: Get a subtitle
- `upload_subtitle(file_data, file_name, file_uuid, locale, workspace_name) -> SubtitleDict`: Upload a subtitle file

## License

This project is licensed under the MIT License - see the LICENSE file for details. 