#!/usr/bin/env python3
"""
Download Jordan Maxwell audio and video content from Internet Archive.

This script downloads freely available Jordan Maxwell lectures, interviews,
and presentations from the Internet Archive for educational and research purposes.
"""

import os
import sys
import urllib.request
import json
from pathlib import Path
from urllib.parse import urljoin

# Internet Archive collections with Jordan Maxwell content
ARCHIVE_ITEMS = [
    "jordan-maxwell-good",  # Audio and video collection
    "youtube-U1IMrZ21kho",  # Lost Knowledge Series video
]

OUTPUT_DIR = Path("source_material")


def download_file(url, filename, output_dir):
    """Download a file from URL to the specified directory."""
    output_path = output_dir / filename
    
    # Skip if file already exists
    if output_path.exists():
        print(f"✓ Already downloaded: {filename}")
        return True
    
    try:
        print(f"Downloading: {filename}")
        print(f"  URL: {url}")
        
        # Download with progress indication
        urllib.request.urlretrieve(url, output_path)
        
        file_size = output_path.stat().st_size / (1024 * 1024)  # Size in MB
        print(f"✓ Downloaded: {filename} ({file_size:.2f} MB)")
        return True
        
    except Exception as e:
        print(f"✗ Error downloading {filename}: {e}")
        if output_path.exists():
            output_path.unlink()  # Clean up partial download
        return False


def get_archive_metadata(item_id):
    """Fetch metadata for an Internet Archive item."""
    metadata_url = f"https://archive.org/metadata/{item_id}"
    
    try:
        with urllib.request.urlopen(metadata_url) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"Error fetching metadata for {item_id}: {e}")
        return None


def download_from_archive_item(item_id, output_dir, file_types=None):
    """
    Download files from an Internet Archive item.
    
    Args:
        item_id: Internet Archive item identifier
        output_dir: Directory to save downloaded files
        file_types: List of file extensions to download (e.g., ['mp4', 'mp3'])
                   If None, downloads common audio/video formats
    """
    if file_types is None:
        file_types = ['mp4', 'mp3', 'avi', 'mkv', 'mov', 'webm', 'm4a', 'flac', 'wav']
    
    print(f"\n{'='*70}")
    print(f"Processing Internet Archive item: {item_id}")
    print(f"{'='*70}")
    
    metadata = get_archive_metadata(item_id)
    if not metadata:
        print(f"Could not fetch metadata for {item_id}")
        return 0
    
    files = metadata.get('files', [])
    downloaded_count = 0
    
    # Filter for audio/video files
    media_files = [
        f for f in files 
        if f.get('name', '').split('.')[-1].lower() in file_types
    ]
    
    if not media_files:
        print(f"No audio/video files found in {item_id}")
        return 0
    
    print(f"Found {len(media_files)} media file(s) to download")
    
    for file_info in media_files:
        filename = file_info.get('name')
        if not filename:
            continue
        
        # Construct download URL
        url = f"https://archive.org/download/{item_id}/{filename}"
        
        if download_file(url, filename, output_dir):
            downloaded_count += 1
    
    return downloaded_count


def create_readme(output_dir):
    """Create a README file in the source_material directory."""
    readme_path = output_dir / "README.md"
    
    readme_content = """# Jordan Maxwell Source Material

This directory contains audio and video content from Jordan Maxwell's teachings,
downloaded from the Internet Archive for educational and research purposes.

## Sources

All content has been downloaded from the Internet Archive, which hosts freely
available Jordan Maxwell lectures, interviews, and presentations:

- Internet Archive: https://archive.org/

## Content

The materials include:
- Lectures on esoteric knowledge, symbolism, and hidden history
- Interviews and presentations
- Educational content on various topics related to Jordan Maxwell's research

## Usage

This content is intended for:
- Research for "The Essential Jordan Maxwell" book project
- Educational purposes
- Preservation of Jordan Maxwell's teachings

## Copyright Notice

All content belongs to the original copyright holders. This material is collected
under fair use for educational and research purposes. If you are a copyright holder
and have concerns, please contact the repository maintainer.

## Downloaded Files

"""
    
    # List downloaded files
    media_files = []
    for ext in ['mp4', 'mp3', 'avi', 'mkv', 'mov', 'webm', 'm4a', 'flac', 'wav']:
        media_files.extend(output_dir.glob(f"*.{ext}"))
    
    if media_files:
        readme_content += "\nThe following files have been downloaded:\n\n"
        for file in sorted(media_files):
            size = file.stat().st_size / (1024 * 1024)  # Size in MB
            readme_content += f"- {file.name} ({size:.2f} MB)\n"
    else:
        readme_content += "\nNo files have been downloaded yet.\n"
    
    with open(readme_path, 'w') as f:
        f.write(readme_content)
    
    print(f"\n✓ Created README: {readme_path}")


def main():
    """Main function to download Jordan Maxwell source material."""
    print("="*70)
    print("Jordan Maxwell Source Material Downloader")
    print("="*70)
    print("\nThis script downloads freely available Jordan Maxwell content")
    print("from the Internet Archive for educational and research purposes.\n")
    
    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR.absolute()}\n")
    
    total_downloaded = 0
    
    # Download from each archive item
    for item_id in ARCHIVE_ITEMS:
        count = download_from_archive_item(item_id, OUTPUT_DIR)
        total_downloaded += count
    
    # Create README
    create_readme(OUTPUT_DIR)
    
    print("\n" + "="*70)
    print(f"Download complete! Total files downloaded: {total_downloaded}")
    print(f"Files saved to: {OUTPUT_DIR.absolute()}")
    print("="*70)
    
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nDownload interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}")
        sys.exit(1)
