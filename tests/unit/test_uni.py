"""Basic tests for uni.py module to demonstrate testing infrastructure."""

from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

import uni


class TestUniModule:
    """Tests for the uni module."""
    
    @pytest.mark.unit
    def test_get_first_anchor_with_header(self, temp_dir):
        """Test get_first_anchor with a file containing headers."""
        test_file = temp_dir / "test.md"
        test_file.write_text("# Test Header\nSome content")
        
        result = uni.get_first_anchor(str(test_file))
        assert result == "#test-header"
    
    @pytest.mark.unit
    def test_get_first_anchor_no_header(self, temp_dir):
        """Test get_first_anchor with a file without headers."""
        test_file = temp_dir / "test.md"
        test_file.write_text("No headers here\nJust plain text")
        
        result = uni.get_first_anchor(str(test_file))
        assert result == "#"
    
    @pytest.mark.unit
    def test_get_first_anchor_multiple_headers(self, temp_dir):
        """Test get_first_anchor returns only the first header."""
        test_file = temp_dir / "test.md"
        test_file.write_text("Some text\n## First Header\n## Second Header")
        
        result = uni.get_first_anchor(str(test_file))
        assert result == "#first-header"