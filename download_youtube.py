#!/usr/bin/env python3
"""
Helper script to download Jordan Maxwell videos from YouTube using yt-dlp.

This script provides an easy interface to download videos from the official
Jordan Maxwell YouTube archives using yt-dlp.
"""

import subprocess
import sys
from pathlib import Path

OUTPUT_DIR = Path("source_material")

# Official Jordan Maxwell YouTube resources
YOUTUBE_SOURCES = {
    "channel": "https://www.youtube.com/c/JordanMaxwellVideos",
    "podcast_playlist": "https://www.youtube.com/playlist?list=PLXFqjauWQf8my9dHqkY9yGpsjT0G9VFcl",
}


def check_yt_dlp():
    """Check if yt-dlp is installed."""
    try:
        result = subprocess.run(
            ["yt-dlp", "--version"],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✓ yt-dlp is installed (version {result.stdout.strip()})")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ yt-dlp is not installed")
        print("\nTo install yt-dlp:")
        print("  pip install yt-dlp")
        print("  or")
        print("  pip3 install yt-dlp")
        return False


def download_video(url, output_dir):
    """Download a video using yt-dlp."""
    output_template = str(output_dir / "%(title)s.%(ext)s")
    
    cmd = [
        "yt-dlp",
        "-o", output_template,
        "--format", "best",
        "--write-description",
        "--write-info-json",
        url
    ]
    
    try:
        print(f"\nDownloading from: {url}")
        subprocess.run(cmd, check=True)
        print("✓ Download completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Download failed: {e}")
        return False


def download_playlist(url, output_dir):
    """Download entire playlist using yt-dlp."""
    output_template = str(output_dir / "%(playlist_index)s-%(title)s.%(ext)s")
    
    cmd = [
        "yt-dlp",
        "-o", output_template,
        "--format", "best",
        "--write-description",
        "--write-info-json",
        "--yes-playlist",
        url
    ]
    
    try:
        print(f"\nDownloading playlist from: {url}")
        print("Note: This may take a long time depending on playlist size")
        subprocess.run(cmd, check=True)
        print("✓ Playlist download completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Playlist download failed: {e}")
        return False


def main():
    """Main function."""
    print("="*70)
    print("Jordan Maxwell YouTube Downloader (yt-dlp)")
    print("="*70)
    print()
    
    # Check if yt-dlp is installed
    if not check_yt_dlp():
        return 1
    
    # Create output directory
    OUTPUT_DIR.mkdir(exist_ok=True)
    print(f"✓ Output directory: {OUTPUT_DIR.absolute()}\n")
    
    # Show menu
    print("What would you like to download?")
    print()
    print("1. Download a specific video (you provide the URL)")
    print("2. Download the official podcast playlist")
    print("3. Exit")
    print()
    
    choice = input("Enter your choice (1-3): ").strip()
    
    if choice == "1":
        url = input("\nEnter the YouTube video URL: ").strip()
        if url:
            download_video(url, OUTPUT_DIR)
        else:
            print("No URL provided")
            return 1
    
    elif choice == "2":
        print("\nThis will download the entire Jordan Maxwell Podcast Series playlist")
        confirm = input("Continue? (y/n): ").strip().lower()
        if confirm == 'y':
            download_playlist(YOUTUBE_SOURCES["podcast_playlist"], OUTPUT_DIR)
        else:
            print("Download cancelled")
    
    elif choice == "3":
        print("Exiting...")
        return 0
    
    else:
        print("Invalid choice")
        return 1
    
    print("\n" + "="*70)
    print("Done!")
    print("="*70)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)
