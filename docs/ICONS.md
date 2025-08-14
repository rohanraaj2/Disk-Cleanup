# Icon Files Documentation

This document explains the icon files included in the Disk-Cleanup project.

## Current Status

The icon files in this project are currently **placeholder files** that need to be replaced with proper image files for production use.

## Icon Files Location

- **Linux**: `Linux/icon.png` - 64x64 PNG format
- **Windows**: `Windows/icon.ico` - Multi-size ICO format
- **macOS**: `macOS/icon.icns` - Apple ICNS format

## Creating Proper Icons

### Recommended Icon Design
The icon should represent disk cleanup functionality:
- Hard drive or disk symbol
- Cleaning elements (sparkles, broom, cleaning symbols)
- Colors: Blue/tech colors for the disk, bright colors for cleaning elements
- Simple, recognizable design that works at small sizes

### Linux (PNG)
```bash
# Create 64x64 PNG with transparency
# Tools: GIMP, Inkscape, online editors
# Format: PNG with alpha channel
```

### Windows (ICO)
```bash
# Create multi-size ICO file containing:
# 16x16, 32x32, 48x48, 64x64 pixels
# Tools: GIMP with ICO plugin, IcoFX, online converters
```

### macOS (ICNS)
```bash
# Create ICNS with multiple resolutions for Retina displays
# Tools: Icon Composer (Xcode), Image2icon, iconutil
# Command: iconutil -c icns icon.iconset
```

## Integration

Icons are referenced in:
- `Linux/UbuntuDiskCleanup.desktop` (Icon=./icon.png)
- `Windows/DiskCleanupGUIApp.lnk` (when created as proper shortcut)
- `macOS/DiskCleanupGUIApp.app/Contents/Info.plist` (CFBundleIconFile)

## To-Do

- [ ] Replace placeholder files with actual icon images
- [ ] Test icon display on each platform
- [ ] Ensure proper transparency and scaling
- [ ] Verify icons work in dark/light themes
