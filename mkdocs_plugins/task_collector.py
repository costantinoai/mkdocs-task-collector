from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File
from mkdocs.config import config_options
import os
import re

class TaskCollectorPlugin(BasePlugin):
    config_scheme = (
        ('output_file', config_options.Type(str, default='TaskList.md')),
    )

    def on_files(self, files, config):
        """
        Processes each Markdown file to search for specific keywords ('NOTE', 'TODO', 'PLACEHOLDER')
        and generates a task list file grouped by file.
        """
        # Define the regex pattern to capture specific keywords
        pattern = re.compile(r'\b(NOTE|TODO|PLACEHOLDER)\b')

        # Get the output file name and path to avoid processing it
        output_filename = self.config['output_file']
        output_filepath = os.path.join(config['docs_dir'], output_filename)

        # Dictionary to hold tasks grouped by file
        tasks_by_file = {}

        for file in files:
            if file.src_path.endswith('.md') and file.abs_src_path != output_filepath:
                with open(file.abs_src_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()

                # Collect all tasks for the current file
                for i, line in enumerate(lines):
                    if pattern.search(line):
                        # Capture the entire line and store it under the respective file heading
                        tasks_by_file.setdefault(file.src_path, []).append(
                            f"+ Line {i+1} - {line.strip()}")

        # Start building the content for the output file
        content = "# Task List\n\n"
        for file_path, tasks in tasks_by_file.items():
            content += f"## {file_path}\n"
            content += "\n".join(tasks) + "\n\n"

        # Write to the output file
        self.write_output_file(output_filepath, content)
        return files

    def write_output_file(self, output_filepath, content):
        """
        Writes content to the specified file and ensures it's added to the list of site files without causing re-build loops.
        """
        try:
            existing_content = ''
            if os.path.exists(output_filepath):
                with open(output_filepath, 'r', encoding='utf-8') as f:
                    existing_content = f.read().replace('\r\n', '\n')

            if existing_content != content.replace('\r\n', '\n'):
                with open(output_filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
        except IOError as e:
            print(f"Error writing to {output_filepath}: {str(e)}")

