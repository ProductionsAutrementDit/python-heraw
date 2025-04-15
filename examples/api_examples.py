import os
from heraw.client import Heraw

# Get API key from environment variable
api_key = os.environ.get("HERAW_API_KEY")
workspace_name = os.environ.get("HERAW_WORKSPACE", "my-workspace")

if not api_key:
    print("Please set the HERAW_API_KEY environment variable")
    exit(1)

# Initialize the client
client = Heraw(api_key=api_key)


def file_examples():
    """Examples of working with files"""
    try:
        # Get folder to use for file creation
        folders = client.get_folder_content(
            "root", workspace_name=workspace_name, basic=True
        )
        if "folders" in folders and folders["folders"]:
            folder_uuid = folders["folders"][0]["uuid"]

            # Create a new file entry
            file_data = {
                "folderUuid": folder_uuid,
                "mimeType": "text/plain",
                "size": 1024,
                "name": "example.txt",
                "version": 1,
            }
            new_file = client.create_file(file_data, workspace_name=workspace_name)
            print(f"Created new file: {new_file['name']} with UUID: {new_file['uuid']}")

            # Update file status
            updated_file = client.update_file_status(
                new_file["uuid"], "in_progress", workspace_name=workspace_name
            )
            print(f"Updated file status to: {updated_file['status']}")

            # Get file custom fields
            custom_fields = client.get_file_custom_fields(
                new_file["uuid"], workspace_name=workspace_name
            )
            print(f"File has {len(custom_fields)} custom fields")

            # Create a new version
            version_data = {
                "folderUuid": folder_uuid,
                "mimeType": "text/plain",
                "size": 2048,
                "name": "example.txt",
                "version": 2,
            }
            new_version = client.create_file_version(
                new_file["uuid"], version_data, workspace_name=workspace_name
            )
            print(f"Created new version: {new_version['version']}")

            # Delete the file (example only - commented out)
            # client.delete_file(new_file["uuid"], workspace_name=workspace_name)
            # print(f"Deleted file: {new_file['name']}")
        else:
            print("No folders found to create file in")
    except Exception as e:
        print(f"Error in file examples: {e}")


def project_examples():
    """Examples of working with projects"""
    try:
        # List projects
        projects = client.list_projects(workspace_name=workspace_name)
        print(f"Found {len(projects)} projects")

        # Create a new project
        project_data = {
            "name": "Example Project",
            "startDate": "2024-04-15T00:00:00Z",
            "endDate": "2024-07-01T00:00:00Z",
            "companyName": "ACME Inc.",
            "disableCasts": False,
        }

        try:
            new_project = client.create_project(
                project_data, workspace_name=workspace_name
            )
            print(
                f"Created new project: {new_project['name']} with UUID: {new_project['uuid']}"
            )

            # Get the project
            project = client.get_project(
                new_project["uuid"], workspace_name=workspace_name
            )
            print(f"Retrieved project: {project['name']}")

            # Update the project
            update_data = {
                "name": "Updated Example Project",
                "endDate": "2024-08-01T00:00:00Z",
            }
            updated_project = client.update_project(
                new_project["uuid"], update_data, workspace_name=workspace_name
            )
            print(f"Updated project name to: {updated_project['name']}")

            # Get project teams
            teams = client.get_project_teams(
                new_project["uuid"], workspace_name=workspace_name
            )
            print(f"Project has {len(teams)} teams")

            # Update project status
            status_update = client.update_project_status(
                new_project["uuid"], "IN_PROGRESS"
            )
            print(f"Updated project status to: {status_update['status']}")

            # Delete the project (example only - commented out)
            # client.delete_project(new_project["uuid"], workspace_name=workspace_name)
            # print(f"Deleted project: {new_project['name']}")
        except Exception as e:
            print(f"Error in project creation/management: {e}")

        # Search for projects
        search_criteria = {
            "name": "Example",
            "status": "IN_PROGRESS",
            "page": 1,
            "resultsPerPage": 10,
        }
        try:
            search_results = client.search_projects(
                search_criteria, workspace_name=workspace_name
            )
            print(f"Found {len(search_results)} projects matching search criteria")
        except Exception as e:
            print(f"Error in project search: {e}")

    except Exception as e:
        print(f"Error in project examples: {e}")


def folder_examples():
    """Examples of working with folders"""
    try:
        # Get a folder
        folder = client.get_folder("root", workspace_name=workspace_name)
        print(f"Root folder UUID: {folder['uuid']}")

        # Get folder content
        content = client.get_folder_content(
            folder["uuid"], workspace_name=workspace_name
        )
        print(
            f"Root folder has {len(content.get('folders', []))} subfolders and {len(content.get('files', []))} files"
        )

        # Create a new folder
        folder_data = {
            "parentFolderUuid": folder["uuid"],
            "name": "Example Folder",
            "copyParentProperties": True,
            "copyParentMembers": True,
        }
        try:
            new_folder = client.create_folder(
                folder_data, workspace_name=workspace_name
            )
            print(
                f"Created new folder: {new_folder['name']} with UUID: {new_folder['uuid']}"
            )

            # Invite users to folder (example only - use real emails and UUIDs)
            """
            invitation_data = {
                "message": "Please join this folder",
                "members": [
                    {
                        "email": "user@example.com",
                        "role": "ROLE_SPECTATOR",
                        "canDownload": True,
                        "canExport": False
                    }
                ]
            }
            invitation = client.invite_users_to_folder(
                new_folder["uuid"], invitation_data, workspace_name=workspace_name
            )
            print(f"Invited users to folder")
            """

            # Delete the folder (example only - commented out)
            # client.delete_folder(new_folder["uuid"], workspace_name=workspace_name)
            # print(f"Deleted folder: {new_folder['name']}")
        except Exception as e:
            print(f"Error in folder creation/management: {e}")

    except Exception as e:
        print(f"Error in folder examples: {e}")


def cast_examples():
    """Examples of working with casts"""
    try:
        # List casts
        casts = client.list_casts(workspace_name=workspace_name)
        print(f"Found {len(casts)} casts")

        # Create a new cast (example only - not executed since it needs real file UUIDs)
        """
        cast_data = {
            "name": "Example Cast",
            "download": True,
            "comment": True,
            "expires": "2024-07-01T00:00:00Z",
            "filesToCast": ["file-uuid-1", "file-uuid-2"],
            "projectUuid": "project-uuid"
        }
        new_cast = client.create_cast(cast_data, workspace_name=workspace_name)
        print(f"Created new cast: {new_cast['name']} with UUID: {new_cast['uuid']}")
        
        # Update the cast
        update_data = {
            "name": "Updated Example Cast",
            "expires": "2024-08-01T00:00:00Z"
        }
        updated_cast = client.update_cast(
            new_cast["uuid"], update_data, workspace_name=workspace_name
        )
        print(f"Updated cast name to: {updated_cast['name']}")
        
        # Share the cast
        share_data = {
            "emails": ["user1@example.com", "user2@example.com"],
            "castName": "Shared Cast",
            "message": "Please review this cast"
        }
        share_result = client.share_cast(new_cast["uuid"], share_data, workspace_name=workspace_name)
        print(f"Shared cast with {len(share_data['emails'])} users")
        
        # Delete the cast
        client.delete_cast(new_cast["uuid"], workspace_name=workspace_name)
        print(f"Deleted cast: {new_cast['name']}")
        """
    except Exception as e:
        print(f"Error in cast examples: {e}")


def custom_field_examples():
    """Examples of working with custom fields"""
    try:
        # List custom fields
        custom_fields = client.list_custom_fields(workspace_name=workspace_name)
        print(f"Found {len(custom_fields)} custom fields")

        # Create a new custom field
        field_data = {
            "name": "Example Field",
            "type": "STRING",
            "multiple": False,
            "associations": ["FILES"],
            "associationTargetIdentifier": "all",
        }
        try:
            new_field = client.create_custom_field(
                field_data, workspace_name=workspace_name
            )
            print(
                f"Created new custom field: {new_field['name']} with UUID: {new_field['uuid']}"
            )

            # Update the custom field
            update_data = {"name": "Updated Example Field"}
            updated_field = client.update_custom_field(
                new_field["uuid"], update_data, workspace_name=workspace_name
            )
            print(f"Updated custom field name to: {updated_field['name']}")

            # Delete the custom field (example only - commented out)
            # client.delete_custom_field(new_field["uuid"], workspace_name=workspace_name)
            # print(f"Deleted custom field: {new_field['name']}")
        except Exception as e:
            print(f"Error in custom field creation/management: {e}")

    except Exception as e:
        print(f"Error in custom field examples: {e}")


def search_examples():
    """Examples of searching"""
    try:
        # Search for content
        search_results = client.search(
            query="example",
            workspace_name=workspace_name,
            contexts=["files", "folders", "comments"],
            folder_uuid=None,  # Optional: limit to specific folder
        )
        print(f"Search found {len(search_results.get('results', []))} results")
    except Exception as e:
        print(f"Error in search examples: {e}")


def subtitle_examples():
    """Examples of working with subtitles"""
    try:
        # Upload a subtitle (example only - not executed)
        """
                # Create a simple SRT file in memory
                srt_content = '''1
        00:00:01,000 --> 00:00:04,000
        This is an example subtitle.

        2
        00:00:05,000 --> 00:00:08,000
        Created for the heraw SDK demo.
        '''
                file_data = io.BytesIO(srt_content.encode('utf-8'))

                # Upload the subtitle
                subtitle = client.upload_subtitle(
                    file_data=file_data,
                    file_name="example.srt",
                    file_uuid="file-uuid",  # Replace with a real file UUID
                    locale="en_US",
                    workspace_name=workspace_name
                )
                print(f"Uploaded subtitle with UUID: {subtitle['uuid']}")

                # Get the subtitle
                retrieved_subtitle = client.get_subtitle(
                    subtitle_uuid=subtitle["uuid"],
                    workspace_name=workspace_name,
                    format="srt"
                )
                print(f"Retrieved subtitle content")
        """
    except Exception as e:
        print(f"Error in subtitle examples: {e}")


def entity_examples():
    """Examples of working with generic entities"""
    try:
        # List entities
        entities = client.list_entities(workspace_name=workspace_name)
        print(f"Found {len(entities)} entities")

        # Create an entity (example only - using a hypothetical endpoint)
        """
        entity_data = {
            "name": "Example Entity",
            "description": "This is an example entity"
        }
        new_entity = client.create_entity(entity_data, workspace_name=workspace_name)
        print(f"Created new entity with ID: {new_entity['id']}"))
        
        # Update an entity
        update_data = {
            "name": "Updated Example Entity"
        }
        updated_entity = client.update_entity(new_entity["uuid"], update_data, workspace_name=workspace_name)
        print(f"Updated entity name to: {updated_entity['name']}")
        
        # Delete an entity
        client.delete_entity(new_entity["uuid"], workspace_name=workspace_name)
        print(f"Deleted entity")
        """
    except Exception as e:
        print(f"Error in entity examples: {e}")


if __name__ == "__main__":
    print("\n----- File Examples -----")
    file_examples()

    print("\n----- Project Examples -----")
    project_examples()

    print("\n----- Folder Examples -----")
    folder_examples()

    print("\n----- Cast Examples -----")
    cast_examples()

    print("\n----- Custom Field Examples -----")
    custom_field_examples()

    print("\n----- Search Examples -----")
    search_examples()

    print("\n----- Subtitle Examples -----")
    subtitle_examples()

    print("\n----- Entity Examples -----")
    entity_examples()
