# DiskCleanupGUIApp

Cross-platform GUI disk cleanup tool for Linux, Windows, and macOS.

---

## Overview

DiskCleanupGUIApp is a portable, interactive disk cleanup tool with a visual GUI. It works across Linux, Windows, and macOS and can run directly from a USB drive without installation. The tool provides:

* Visual disk usage summary
* Interactive deletion of large folders/files
* Safe system cache/log cleanup
* Ext4 reserved space reduction on Linux
* Portable and offline usage

---

## Repository Structure

```
DiskCleanupGUIApp/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ Linux/
├─ Windows/
├─ macOS/
└─ docs/
```

### Linux/

Contains scripts and files for Linux systems:

```
Linux/
├─ cleanup_gui.py
├─ run.sh
├─ UbuntuDiskCleanup.desktop
├─ icon.png
└─ README_LAUNCH_HERE.txt
```

### Windows/

Contains scripts and files for Windows systems:

```
Windows/
├─ cleanup_gui.py
├─ run.bat
├─ DiskCleanupGUIApp.lnk
├─ icon.ico
└─ README_LAUNCH_HERE.txt
```

### macOS/

Contains scripts and files for macOS systems:

```
macOS/
├─ cleanup_gui.py
├─ run.command
├─ DiskCleanupGUIApp.app
├─ icon.icns
└─ README_LAUNCH_HERE.txt
```

### docs/

Optional folder for documentation, screenshots, or diagrams.

---

## Installation

### Linux/macOS

1. Extract the `Linux` or `macOS` folder from the repository.
2. Ensure Python 3 is installed.
3. Make scripts executable if necessary:

```bash
chmod +x run.sh
chmod +x run.command
```

4. Launch:

```bash
# Linux
./run.sh
# macOS
./run.command
```

Or double-click `UbuntuDiskCleanup.desktop` on Linux or `DiskCleanupGUIApp.app` on macOS.

### Windows

1. Extract the `Windows` folder from the repository.
2. Ensure Python 3 is installed.
3. Double-click `DiskCleanupGUIApp.lnk` to launch.

---

## Usage

1. Launch the GUI on your platform.
2. View the visual disk usage summary.
3. Select folders/files for cleanup.
4. Click `Cleanup` to remove selected items safely.
5. On Linux, optionally reduce ext4 reserved space.

---

## License

This project is licensed under the MIT License. See LICENSE file for details.

---

## Contributions

Contributions are welcome! Please fork the repository and submit a pull request for improvements or new features.

---

## Contact

For questions or support, open an issue on the GitHub repository.
