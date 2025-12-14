# Quick Start Guide: Download Jordan Maxwell Content

This guide will help you quickly start downloading Jordan Maxwell audio and video content for "The Essential Jordan Maxwell" book project.

## Step 1: Prerequisites

Ensure you have Python 3 installed:
```bash
python3 --version
```

If not installed, download from: https://www.python.org/downloads/

## Step 2: Choose Your Download Method

### Option A: Automatic Download from Internet Archive (Recommended)

This is the easiest method for getting freely available content:

```bash
python3 download_source_material.py
```

The script will automatically:
- Download from the "jordan-maxwell-good" collection
- Download the "Lost Knowledge Series" video
- Save all files to `source_material/` directory
- Create a README with file inventory

**Expected time**: 5-30 minutes depending on file sizes and internet speed

### Option B: YouTube Downloads

For additional content from YouTube:

1. Install yt-dlp:
   ```bash
   pip install yt-dlp
   # or
   pip3 install yt-dlp
   ```

2. Run the YouTube downloader:
   ```bash
   python3 download_youtube.py
   ```

3. Follow the interactive menu:
   - Option 1: Download a specific video (paste the URL)
   - Option 2: Download the entire podcast playlist
   - Option 3: Exit

**Note**: Downloading entire playlists can take hours depending on the number of videos.

### Option C: Manual Download

If scripts don't work, manually download from:

1. Internet Archive: https://archive.org/details/jordan-maxwell-good
2. YouTube: https://www.youtube.com/c/JordanMaxwellVideos
3. Odysee: https://odysee.com/@jordanmaxwellvideos

Save files to the `source_material/` directory.

## Step 3: Verify Downloads

Check what was downloaded:
```bash
ls -lh source_material/
```

Read the documentation:
```bash
cat source_material/README.md
```

## Step 4: Start Your Research

Now you can:
1. Watch/listen to the downloaded content
2. Take notes for the book
3. Identify key themes and topics
4. Organize content by subject matter

## Troubleshooting

### "No address associated with hostname" error
- Check your internet connection
- Verify archive.org is accessible from your location
- Try using a VPN if the site is blocked

### "yt-dlp is not installed" message
- Install it: `pip install yt-dlp`
- If pip isn't found, install Python properly first

### Downloads are slow
- This is normal for large video files
- Consider downloading overnight
- Try downloading fewer items at a time

### Storage space issues
- Video files are large (500MB - 2GB each)
- Ensure you have 10GB+ free space
- Consider downloading audio-only versions

## Need More Help?

1. Read the comprehensive guide: [DOWNLOAD_INSTRUCTIONS.md](DOWNLOAD_INSTRUCTIONS.md)
2. Check the implementation details: [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md)
3. Review the main README: [Readme.md](Readme.md)

## Important Reminders

- ✅ Downloads are for educational/research purposes only
- ✅ Content is copyrighted - respect fair use doctrine
- ✅ Do not redistribute or use commercially
- ✅ Large files are excluded from git (via .gitignore)

Happy researching! 🎬🎙️📚
