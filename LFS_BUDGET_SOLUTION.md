# Git LFS Budget Solution

## Problem
The repository exceeded its Git LFS budget when trying to download large files, particularly:
- `assets/videos/Elara Aerospace Pitch v1.mp4` (893 MB)
- `assets/slides/Pitchdeck Ignition Aerospace.pdf` (large file)

## Solution Implemented

### 1. Updated `.gitignore`
Added comprehensive rules to prevent large files from being tracked:

```gitignore
# Large media files that exceed Git LFS budget
assets/videos/
assets/videos/*
assets/slides/
assets/slides/*
*.mp4
*.mov
*.avi
*.mkv
*.webm
*.flv

# Large image files
*.psd
*.ai
*.eps
*.tiff
*.tif

# Large documents
*.pdf
*.doc
*.docx
*.ppt
*.pptx
*.xls
*.xlsx

# Backup files
*.bak
*.backup
*~
```

### 2. Alternative Solutions for Large Files

#### Option A: External Hosting
- Host videos on YouTube/Vimeo and embed
- Host PDFs on Google Drive/Dropbox and link
- Use CDN services for large media files

#### Option B: Optimize Files
- Compress videos to web-optimized formats (MP4, WebM)
- Reduce PDF file sizes
- Optimize images before committing

#### Option C: Git LFS Configuration
If you need to track large files, configure Git LFS properly:

```bash
# Install Git LFS
git lfs install

# Track specific file types
git lfs track "*.mp4"
git lfs track "*.pdf"
git lfs track "*.psd"

# Add .gitattributes
git add .gitattributes
```

### 3. Recommended Actions

1. **Remove existing large files from tracking:**
   ```bash
   git rm --cached "assets/videos/Elara Aerospace Pitch v1.mp4"
   git rm --cached "assets/slides/Pitchdeck Ignition Aerospace.pdf"
   ```

2. **Commit the changes:**
   ```bash
   git add .gitignore
   git commit -m "Update .gitignore to prevent LFS budget issues"
   ```

3. **For CI/CD builds:**
   - Add `--depth 1` to git clone to reduce download size
   - Use `git sparse-checkout` to only download needed files
   - Consider using GitHub Actions with `actions/checkout@v4`

### 4. Build Configuration

For CI/CD systems, add these environment variables:
```yaml
env:
  GIT_LFS_SKIP_SMUDGE: 1
```

Or use this git clone command:
```bash
git clone --depth 1 --filter=blob:none https://github.com/elara-aerospace/elara-aerospace.github.io.git
```

## Benefits
- ✅ Prevents LFS budget exceeded errors
- ✅ Faster repository cloning
- ✅ Reduced storage costs
- ✅ Better CI/CD performance
- ✅ Maintains website functionality

## Next Steps
1. Remove large files from Git history if needed
2. Set up external hosting for large media files
3. Update documentation to reflect new file hosting strategy
4. Monitor repository size regularly 