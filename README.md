# mkdocs-task-collector

`mkdocs-task-collector` is a versatile MkDocs plugin designed to streamline your documentation workflow by automatically scanning your Markdown files for specific annotations like `TODO`, `NOTE`, and `PLACEHOLDER`. It generates a comprehensive and organized task list, making it easier to manage and track tasks, notes, and placeholders within your documentation.

![Plugin example functionality](https://github.com/costantinoai/mkdocs-task-collector/blob/main/assets/example.png)

## Roadmap

TODO: tags should not be collected if wrapped in quotes (e.g., ``TODO``), because usualy this is what we do when we describe the tags (and not use them).
TODO: make links in the Task list clickable (specific files, possibly lines?)

## Features

- **Automated Annotation Scanning**: Effortlessly detects `TODO`, `NOTE`, and `PLACEHOLDER` annotations in your Markdown files, saving you time and ensuring no task is overlooked.
- **Consolidated Task List**: Automatically creates a structured task list in a Markdown file, organized by the source file and line number, providing a clear overview of all annotations.
- **Seamless Integration**: Integrates flawlessly into the MkDocs build process, both locally and remotely (e.g., GitHub Pages), without requiring additional configuration.
- **Automatic Deployment**: Ensures that your task list is always up-to-date and published on your website, provided it is referenced in the `nav` section of your `mkdocs.yml` file.
- **Zero Configuration**: No extra configuration needed – simply add the plugin to your `mkdocs.yml` file, and you're ready to go.

## Installation

Install the plugin using `pip`:

```
pip install mkdocs-task-collector
```

## Configuration

Add the `task_collector` plugin to your `mkdocs.yml` configuration file:

```
plugins:
  - search
  - task_collector:
      output_file: 'tasks-list.md'
```

To ensure the generated task list is part of your documentation navigation, add it to the `nav` section in your `mkdocs.yml` file:

```
nav:

    Home: index.md
    Tasks: tasks-list.md
```

## Usage

When you build your MkDocs site, the plugin will scan for `TODO`, `NOTE`, and `PLACEHOLDER` annotations and generate a `tasks-list.md` file in your documentation.

### Example

Suppose you have the following Markdown files:

**`docs/example1.md`**:

```
# Example 1

This is a test document.

TODO: Add more content here.

NOTE: Review this section for accuracy.
```

**`docs/example2.md`**:

```
# Example 2

PLACEHOLDER: Insert diagram here.

TODO: Update the introduction.
```

After running `mkdocs build`, the plugin will generate a `tasks-list.md` with the following content:

```
# Task List

## example1.md
+ Line 5 - **TODO**: Add more content here.
+ Line 7 - **NOTE**: Review this section for accuracy.

## example2.md
+ Line 5 - **PLACEHOLDER**: Insert diagram here.
+ Line 7 - **TODO**: Update the introduction.
```

## Additional Information

### Task List File Management

- **Generation**: The `tasks-list.md` file is generated during the build process.
- **Saving**: This file is saved into the `docs` folder if the generated file is different from the existing local file or if the local file is not found.

### Deployment Considerations

- **Local Deployments**: The `tasks-list.md` file is required for local deployments to ensure it is part of the built site.
- **Remote Deployments (e.g., GitHub Pages)**:
  - If you are using GitHub Pages or similar solutions for automatic deployment (where the website is built remotely), add `tasks-list.md` to your `.gitignore` file.
  - This ensures that if no task list is present in the main branch of the repository, the file will be generated in the deployed environment every time the site is built from the MkDocs documentation. Thus, a page for this file will be created in the documentation if it is correctly specified in the `nav` section of the `mkdocs.yml` file.

### Example `.gitignore` Entry

Add the following line to your `.gitignore` to exclude `tasks-list.md`:

```
docs/tasks-list.md
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

