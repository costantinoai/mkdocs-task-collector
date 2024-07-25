# mkdocs-task-collector

`mkdocs-task-collector` is a MkDocs plugin designed to scan your Markdown files for specific annotations like `TODO`, `NOTE`, and `PLACEHOLDER` and generate a structured task list. This can help you keep track of tasks, notes, and placeholders within your documentation.

## Features

- **Scans for Annotations**: Detects `TODO`, `NOTE`, and `PLACEHOLDER` annotations in your Markdown files.
- **Generates Task List**: Creates a consolidated task list in a Markdown file, organized by the source file and line number.
- **Easy Integration**: Seamlessly integrates into the MkDocs build process.

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
      output_file: 'TaskList.md'
```

## Usage

When you build your MkDocs site, the plugin will scan for `TODO`, `NOTE`, and `PLACEHOLDER` annotations and generate a `TaskList.md` file in your documentation.

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

After running `mkdocs build`, the plugin will generate a `TaskList.md` with the following content:

```
# Task List

## example1.md
+ Line 5 - **TODO**: Add more content here.
+ Line 7 - **NOTE**: Review this section for accuracy.

## example2.md
+ Line 5 - **PLACEHOLDER**: Insert diagram here.
+ Line 7 - **TODO**: Update the introduction.
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss changes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

