import re
import os
import logging
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class TaskCollectorPlugin(BasePlugin):
    """
    A MkDocs plugin that collects tasks (NOTE, TODO, PLACEHOLDER) from markdown files
    and generates a task list file grouped by file.
    """

    config_scheme = (
        ('output_file', config_options.Type(str, default='TaskList.md')),
    )

    def __init__(self):
        # Initialize the logger for this plugin
        self.logger = logging.getLogger('mkdocs.plugins.task_collector')

    def on_files(self, files, config):
        """
        Process each Markdown file to search for specific keywords and generate a task list file.

        Args:
            files: A list of MkDocs File objects representing all the files in the documentation.
            config: The MkDocs configuration dictionary.

        Returns:
            The list of files, potentially modified.
        """
        # Define the regex pattern to capture specific keywords not preceded or followed by a backtick
        pattern = re.compile(r'(?<!`)\b(NOTE|TODO|PLACEHOLDER)\b(?!`)')

        # Get the output file name and path to avoid processing it
        output_filename = self.config['output_file']
        output_filepath = os.path.join(config['docs_dir'], output_filename)

        # Dictionary to hold tasks grouped by file
        tasks_by_file = {}

        for file in files:
            # Process only Markdown files that are not the output file
            if file.src_path.endswith('.md') and file.abs_src_path != output_filepath:
                self.logger.info(f"Processing file: {file.src_path}")
                try:
                    with open(file.abs_src_path, 'r', encoding='utf-8') as f:
                        lines = f.readlines()

                    # Collect all tasks for the current file
                    for i, line in enumerate(lines):
                        match = pattern.search(line)
                        if match:
                            # Capture the entire line and store it under the respective file heading
                            task = f"+ Line {i+1} - {line.strip()}"
                            tasks_by_file.setdefault(file.src_path, []).append(task)
                            self.logger.debug(f"Found task in {file.src_path}: {task}")
                except IOError as e:
                    self.logger.error(f"Error reading file {file.src_path}: {str(e)}")

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
        Write content to the specified file and ensure it's added to the list of site files.

        Args:
            output_filepath: The path where the output file should be written.
            content: The content to write to the file.
        """
        try:
            # Check if the file exists and read its content
            existing_content = ''
            if os.path.exists(output_filepath):
                with open(output_filepath, 'r', encoding='utf-8') as f:
                    existing_content = f.read().replace('\r\n', '\n')

            # Compare existing content with new content
            if existing_content != content.replace('\r\n', '\n'):
                # Write new content if it's different from existing content
                with open(output_filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                self.logger.info(f"Task list written to {output_filepath}")
            else:
                self.logger.info(f"No changes in task list, file not updated: {output_filepath}")
        except IOError as e:
            self.logger.error(f"Error writing to {output_filepath}: {str(e)}")
