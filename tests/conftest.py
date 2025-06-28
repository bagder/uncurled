"""Shared pytest fixtures and configuration for all tests."""

import os
import tempfile
from pathlib import Path
from typing import Generator

import pytest


@pytest.fixture
def temp_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


@pytest.fixture
def temp_file(temp_dir: Path) -> Generator[Path, None, None]:
    """Create a temporary file in the temp directory."""
    temp_file = temp_dir / "test_file.txt"
    temp_file.write_text("test content")
    yield temp_file


@pytest.fixture
def mock_env_vars() -> Generator[dict, None, None]:
    """Mock environment variables for testing."""
    original_env = os.environ.copy()
    test_env = {
        "TEST_VAR": "test_value",
        "DEBUG": "true",
    }
    os.environ.update(test_env)
    yield test_env
    # Restore original environment
    os.environ.clear()
    os.environ.update(original_env)


@pytest.fixture
def sample_markdown_file(temp_dir: Path) -> Path:
    """Create a sample markdown file for testing."""
    md_file = temp_dir / "sample.md"
    md_file.write_text("""# Sample Markdown

## Section 1
This is a sample section.

* [Link to page](page.md)
* [Another link](../LICENSE)

## Section 2
More content here.
""")
    return md_file


@pytest.fixture
def sample_config() -> dict:
    """Provide a sample configuration dictionary."""
    return {
        "name": "test_project",
        "version": "1.0.0",
        "debug": True,
        "settings": {
            "timeout": 30,
            "retries": 3,
        }
    }


@pytest.fixture(autouse=True)
def reset_sys_modules():
    """Reset sys.modules to prevent module caching issues between tests."""
    import sys
    modules_before = set(sys.modules.keys())
    yield
    modules_after = set(sys.modules.keys())
    for module in modules_after - modules_before:
        if module.startswith("test_"):
            del sys.modules[module]


@pytest.fixture
def mock_file_system(tmp_path: Path) -> dict:
    """Create a mock file system structure for testing."""
    structure = {
        "root": tmp_path,
        "src": tmp_path / "src",
        "tests": tmp_path / "tests",
        "docs": tmp_path / "docs",
    }
    
    # Create directories
    for dir_path in structure.values():
        dir_path.mkdir(exist_ok=True)
    
    # Create some sample files
    (structure["src"] / "main.py").write_text("print('Hello World')")
    (structure["docs"] / "README.md").write_text("# Project Documentation")
    
    return structure


@pytest.fixture
def capture_stdout(monkeypatch):
    """Capture stdout for testing print statements."""
    import io
    import sys
    
    captured_output = io.StringIO()
    monkeypatch.setattr(sys, "stdout", captured_output)
    
    def get_output():
        return captured_output.getvalue()
    
    return get_output