import sys
import types
import os
import shutil

# Create minimal stub modules for mkdocs
mkdocs = types.ModuleType('mkdocs')
mkdocs.plugins = types.ModuleType('mkdocs.plugins')
class BasePlugin:
    config_scheme = ()
mkdocs.plugins.BasePlugin = BasePlugin

mkdocs.config = types.ModuleType('mkdocs.config')
class StubType:
    def __init__(self, *_args, **_kwargs):
        pass
config_options = types.SimpleNamespace(Type=StubType)
mkdocs.config.config_options = config_options

mkdocs.structure = types.ModuleType('mkdocs.structure')
mkdocs.structure.files = types.ModuleType('mkdocs.structure.files')
class File:
    def __init__(self, src_path, docs_dir, site_dir, use_directory_urls):
        self.src_path = src_path
        self.abs_src_path = os.path.join(docs_dir, src_path)
        self.dest_path = src_path
        self.abs_dest_path = os.path.join(site_dir, src_path)
        self.url = src_path
    def __repr__(self):
        return f"File({self.src_path})"
mkdocs.structure.files.File = File
class Files(list):
    def get_file_from_path(self, path):
        for f in self:
            if f.src_path == path:
                return f
        return None
mkdocs.structure.files.Files = Files

sys.modules['mkdocs'] = mkdocs
sys.modules['mkdocs.plugins'] = mkdocs.plugins
sys.modules['mkdocs.config'] = mkdocs.config
sys.modules['mkdocs.config.config_options'] = mkdocs.config
sys.modules['mkdocs.structure'] = mkdocs.structure
sys.modules['mkdocs.structure.files'] = mkdocs.structure.files

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mkdocs_plugins.task_collector import TaskCollectorPlugin


def test_collect_tasks(tmp_path):
    docs_dir = tmp_path / "docs"
    site_dir = tmp_path / "site"
    docs_dir.mkdir()
    site_dir.mkdir()

    (docs_dir / "a.md").write_text("TODO: first\n# TODO ignore\n")
    (docs_dir / "b.md").write_text("NOTE: second\n% NOTE ignore\n")

    files = Files([
        File("a.md", str(docs_dir), str(site_dir), True),
        File("b.md", str(docs_dir), str(site_dir), True),
    ])

    plugin = TaskCollectorPlugin()
    plugin.config = {
        'output_file': 'TaskList.md',
        'keywords': ['TODO', 'NOTE'],
        'repo_branch': 'main',
    }

    config = {
        'docs_dir': str(docs_dir),
        'site_dir': str(site_dir),
        'use_directory_urls': True,
        'repo_url': 'https://example.com/repo'
    }

    plugin.on_files(files, config)

    output = docs_dir / 'TaskList.md'
    assert output.exists()
    text = output.read_text()
    assert 'a.md' in text
    assert 'b.md' in text
    assert 'ignore' not in text


