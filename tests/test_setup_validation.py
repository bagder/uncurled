"""Validation tests to verify the testing infrastructure is properly configured."""

import sys
from pathlib import Path

import pytest


class TestSetupValidation:
    """Test class to validate the testing infrastructure setup."""
    
    def test_pytest_installed(self):
        """Verify pytest is installed and importable."""
        assert "pytest" in sys.modules
        assert hasattr(pytest, "__version__")
    
    def test_pytest_cov_installed(self):
        """Verify pytest-cov is installed."""
        try:
            import pytest_cov
            assert pytest_cov is not None
        except ImportError:
            pytest.fail("pytest-cov is not installed")
    
    def test_pytest_mock_installed(self):
        """Verify pytest-mock is installed."""
        try:
            import pytest_mock
            assert pytest_mock is not None
        except ImportError:
            pytest.fail("pytest-mock is not installed")
    
    def test_conftest_fixtures_available(self, temp_dir, temp_file, mock_env_vars, sample_config):
        """Verify that fixtures from conftest.py are available."""
        assert isinstance(temp_dir, Path)
        assert temp_dir.exists()
        assert temp_dir.is_dir()
        
        assert isinstance(temp_file, Path)
        assert temp_file.exists()
        assert temp_file.read_text() == "test content"
        
        assert isinstance(mock_env_vars, dict)
        assert mock_env_vars["TEST_VAR"] == "test_value"
        
        assert isinstance(sample_config, dict)
        assert sample_config["name"] == "test_project"
    
    @pytest.mark.unit
    def test_unit_marker(self):
        """Test that unit test marker works."""
        assert True
    
    @pytest.mark.integration
    def test_integration_marker(self):
        """Test that integration test marker works."""
        assert True
    
    @pytest.mark.slow
    def test_slow_marker(self):
        """Test that slow test marker works."""
        assert True
    
    def test_project_structure(self):
        """Verify the project structure is set up correctly."""
        project_root = Path(__file__).parent.parent
        
        # Check main directories exist
        assert (project_root / "tests").exists()
        assert (project_root / "tests" / "unit").exists()
        assert (project_root / "tests" / "integration").exists()
        
        # Check configuration files exist
        assert (project_root / "pyproject.toml").exists()
        assert (project_root / ".gitignore").exists()
        
        # Check __init__.py files exist
        assert (project_root / "tests" / "__init__.py").exists()
        assert (project_root / "tests" / "unit" / "__init__.py").exists()
        assert (project_root / "tests" / "integration" / "__init__.py").exists()
    
    def test_coverage_configuration(self):
        """Verify coverage is properly configured."""
        from pathlib import Path
        project_root = Path(__file__).parent.parent
        pyproject_path = project_root / "pyproject.toml"
        
        assert pyproject_path.exists()
        content = pyproject_path.read_text()
        
        # Check coverage configuration sections
        assert "[tool.coverage.run]" in content
        assert "[tool.coverage.report]" in content
        assert "[tool.coverage.html]" in content
        assert "[tool.coverage.xml]" in content
        assert "cov-fail-under=80" in content
    
    def test_mock_functionality(self, mocker):
        """Test that pytest-mock mocker fixture works."""
        mock_func = mocker.Mock(return_value=42)
        result = mock_func()
        
        assert result == 42
        mock_func.assert_called_once()
    
    def test_temp_file_fixture_cleanup(self, temp_file):
        """Test that temporary files are cleaned up properly."""
        assert temp_file.exists()
        # File should be cleaned up after test completes