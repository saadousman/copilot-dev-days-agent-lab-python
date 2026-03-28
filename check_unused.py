#!/usr/bin/env python3
"""Quick script to identify potential unused variables and imports."""
import ast
import sys
from pathlib import Path

def check_file(filepath):
    """Check a single Python file for unused imports and variables."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        # Get all imports
        imports = {}
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    name = alias.asname if alias.asname else alias.name
                    imports[name] = node.lineno
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    name = alias.asname if alias.asname else alias.name
                    imports[name] = node.lineno
        
        # Get all names used in the file
        used_names = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Name):
                used_names.add(node.id)
            elif isinstance(node, ast.Attribute):
                if isinstance(node.value, ast.Name):
                    used_names.add(node.value.id)
        
        # Find unused imports
        unused = []
        for imp_name, lineno in imports.items():
            if imp_name not in used_names:
                unused.append((lineno, imp_name))
        
        if unused:
            print(f"\n{filepath}:")
            for lineno, name in sorted(unused):
                print(f"  Line {lineno}: Unused import '{name}'")
    
    except Exception as e:
        print(f"Error checking {filepath}: {e}", file=sys.stderr)

# Check all Python files
repo_root = Path("C:\Users\Dell\Documents\GitHub\vega-frontend\copilot-dev-days-agent-lab-python")
for py_file in repo_root.rglob("*.py"):
    if ".git" not in str(py_file) and "__pycache__" not in str(py_file) and ".solutions" not in str(py_file):
        check_file(py_file)
