#!/usr/bin/env python3
"""
Build script for Client Knowledge Pack.

Generates:
1. Single merged markdown file (dist/{client}-knowledge-pack.md)
2. Zipped agent/ directory (dist/{client}-knowledge-pack.zip)

Usage:
    python3 scripts/build_agent_pack.py --client {client-name}
"""

import argparse
import json
import os
import shutil
from pathlib import Path
from zipfile import ZipFile


def load_json_file(filepath):
    """Load and parse JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def read_file(filepath):
    """Read file contents as string."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def write_file(filepath, content):
    """Write content to file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)


def get_agent_files(agent_dir):
    """Get all markdown files from agent directory, sorted by name."""
    files = []
    for filepath in sorted(Path(agent_dir).glob('*.md')):
        files.append(filepath)
    return files


def build_merged_markdown(agent_dir, repo_root, client_name):
    """Build single merged markdown file."""
    content_parts = []
    
    # Add header
    content_parts.append(f"# {client_name.title()} Knowledge Pack\n")
    content_parts.append("This is a self-contained knowledge pack for AI assistants.\n")
    content_parts.append("---\n\n")
    
    # Add agent files
    agent_files = get_agent_files(agent_dir)
    for filepath in agent_files:
        filename = filepath.name
        if filename == 'README.md':
            continue  # Skip README, it's for humans
        
        content_parts.append(f"## {filename}\n\n")
        content_parts.append(f"*Source: `agent/{filename}`*\n\n")
        content_parts.append("---\n\n")
        content_parts.append(read_file(filepath))
        content_parts.append("\n\n")
    
    # Add evidence appendix
    evidence_manifest_path = Path(agent_dir) / 'evidence-manifest.json'
    if evidence_manifest_path.exists():
        evidence_manifest = load_json_file(evidence_manifest_path)
        content_parts.append("# Evidence Appendix\n\n")
        content_parts.append("*The following files are referenced in the knowledge pack above.*\n\n")
        content_parts.append("---\n\n")
        
        for file_info in evidence_manifest.get('files', []):
            filepath = Path(repo_root) / file_info['path']
            if filepath.exists():
                content_parts.append(f"## {file_info['path']}\n\n")
                content_parts.append(f"*{file_info.get('description', 'Evidence file')}*\n\n")
                content_parts.append("---\n\n")
                try:
                    content_parts.append(read_file(filepath))
                except Exception as e:
                    content_parts.append(f"*Error reading file: {e}*\n\n")
                content_parts.append("\n\n")
            else:
                content_parts.append(f"## {file_info['path']}\n\n")
                content_parts.append(f"*File not found: {filepath}*\n\n")
        
        if evidence_manifest.get('note'):
            content_parts.append(f"\n\n*Note: {evidence_manifest['note']}*\n\n")
    
    return ''.join(content_parts)


def create_zip(agent_dir, output_path):
    """Create zip file of agent directory."""
    with ZipFile(output_path, 'w') as zipf:
        for root, dirs, files in os.walk(agent_dir):
            # Skip __pycache__ and other hidden directories
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for file in files:
                filepath = Path(root) / file
                arcname = filepath.relative_to(Path(agent_dir).parent)
                zipf.write(filepath, arcname)


def main():
    parser = argparse.ArgumentParser(description='Build Client Knowledge Pack')
    parser.add_argument('--client', required=True, help='Client name (e.g., superfeet)')
    args = parser.parse_args()
    
    client_name = args.client.lower()
    repo_root = Path(__file__).parent.parent
    agent_dir = repo_root / 'agent'
    dist_dir = repo_root / 'dist'
    
    # Validate agent directory exists
    if not agent_dir.exists():
        print(f"Error: agent/ directory not found at {agent_dir}")
        return 1
    
    # Create dist directory
    dist_dir.mkdir(exist_ok=True)
    
    # Build merged markdown
    print(f"Building merged markdown for {client_name}...")
    merged_content = build_merged_markdown(agent_dir, repo_root, client_name)
    merged_file = dist_dir / f"{client_name}-knowledge-pack.md"
    write_file(merged_file, merged_content)
    print(f"✓ Created {merged_file}")
    
    # Create zip file
    print(f"Creating zip file for {client_name}...")
    zip_file = dist_dir / f"{client_name}-knowledge-pack.zip"
    create_zip(agent_dir, zip_file)
    print(f"✓ Created {zip_file}")
    
    # Print summary
    print(f"\n✓ Knowledge pack built successfully!")
    print(f"  - Merged markdown: {merged_file}")
    print(f"  - Zip file: {zip_file}")
    print(f"\nNext steps:")
    print(f"  1. Review {merged_file}")
    print(f"  2. Upload to Custom GPT or other AI platform")
    print(f"  3. Test with questions from agent/evals.yaml")
    
    return 0


if __name__ == '__main__':
    exit(main())
