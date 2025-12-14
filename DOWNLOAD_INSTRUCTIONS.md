# How to Download Jordan Maxwell Source Material

This guide explains how to download audio and video content from Jordan Maxwell for "The Essential Jordan Maxwell" book project.

## Quick Start

### Using the Download Script (Recommended)

1. Ensure you have Python 3 installed on your system
2. Run the download script:
   ```bash
   python3 download_source_material.py
   ```
3. The script will automatically download freely available Jordan Maxwell content from the Internet Archive into the `source_material/` directory

### What Gets Downloaded

The script automatically downloads from these Internet Archive collections:
- **jordan-maxwell-good**: Comprehensive collection of audio and video lectures
- **youtube-U1IMrZ21kho**: Lost Knowledge Series video presentations

Supported file formats:
- Video: MP4, AVI, MKV, MOV, WEBM
- Audio: MP3, M4A, FLAC, WAV

## Alternative Download Methods

### Method 1: Manual Download from Internet Archive

If the script doesn't work in your environment, you can manually download from:

1. **Jordan Maxwell Good Collection**
   - URL: https://archive.org/details/jordan-maxwell-good
   - Contains multiple lectures and presentations
   - Download individual files or use "DOWNLOAD OPTIONS" → "TORRENT" for bulk download

2. **Lost Knowledge Series**
   - URL: https://archive.org/details/youtube-U1IMrZ21kho
   - Video presentation on hidden knowledge
   - Download the MP4 file directly from the page

### Method 2: YouTube Downloads

For content from the official YouTube archive:

1. Visit: https://www.youtube.com/c/JordanMaxwellVideos
2. Use a YouTube downloader tool like:
   - `youtube-dl` (command line): `youtube-dl [VIDEO_URL]`
   - `yt-dlp` (improved fork): `yt-dlp [VIDEO_URL]`
   - Online services (search "YouTube downloader")

Example with yt-dlp:
```bash
# Install yt-dlp
pip install yt-dlp

# Download a video
yt-dlp -o "source_material/%(title)s.%(ext)s" [YOUTUBE_URL]

# Download entire playlist
yt-dlp -o "source_material/%(playlist_index)s-%(title)s.%(ext)s" [PLAYLIST_URL]
```

### Method 3: Odysee Platform

Download from the official Odysee channel:

1. Visit: https://odysee.com/@jordanmaxwellvideos
2. Browse available content
3. Click on videos to download directly

## File Organization

Save all downloaded files to the `source_material/` directory:

```
source_material/
├── README.md                          # This file
├── lecture_01_symbolism.mp4
├── lecture_02_secret_societies.mp4
├── interview_xyz.mp3
└── ...
```

## Important Notes

### Copyright and Fair Use

- All Jordan Maxwell content is copyrighted by the original creators/estate
- Downloads are for **educational and research purposes only**
- Content is used under fair use doctrine for book research
- Do not redistribute or use commercially

### Quality Recommendations

When downloading, prefer:
- **Video**: MP4 format, 720p or higher resolution
- **Audio**: MP3 format, 192kbps or higher bitrate
- Original/uncompressed versions when available

### Storage Considerations

- Video files can be large (500MB - 2GB per lecture)
- Audio files are smaller (50MB - 200MB per lecture)
- Ensure you have sufficient disk space (recommend 10GB+ free)

## Troubleshooting

### Script Issues

**Problem**: Network errors or blocked domains
- **Solution**: Use manual download methods or try from a different network

**Problem**: Script downloads wrong file types
- **Solution**: Edit the `file_types` list in the script to specify desired formats

**Problem**: Partial/corrupted downloads
- **Solution**: Delete the partial file and run the script again (it skips existing files)

### General Issues

**Problem**: Can't access Internet Archive
- **Solution**: Check if archive.org is accessible from your location, consider using a VPN

**Problem**: YouTube videos are private/removed
- **Solution**: Focus on content available on Internet Archive and Odysee

## Additional Resources

### Official Sources
- Jordan Maxwell Store: https://jordanmaxwell.com/store.html
- Jordan Maxwell Videos: https://www.jordanmaxwellvideos.com/
- Internet Archive: https://archive.org/search.php?query=jordan+maxwell

### Research Tips
1. Start with the most popular/viewed lectures
2. Focus on topics relevant to your book chapters
3. Take notes while watching/listening
4. Organize files by topic for easier reference

## Support

For issues or questions:
1. Check the README in the `source_material/` directory
2. Review this documentation
3. Open an issue in the GitHub repository
