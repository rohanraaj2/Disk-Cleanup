# Disk-Cleanup

Cross-platform GUI disk cleanup tool for Linux, Windows, and macOS.

---

## Overview

Disk-Cleanup is a portable, interactive disk cleanup tool with a visual GUI. It works across Linux, Windows, and macOS and can run directly from a USB drive without installation. The tool provides:

* Visual disk usage summary
* Interactive deletion of large folders/files
* Safe system cache/log cleanup
* Ext4 reserved space reduction on Linux
* Portable and offline usage

---

## Repository Structure

```
Disk-Cleanup/
├─ README.md
├─ LICENSE
├─ cleanup_gui.py
├─ Linux/
├─ Windows/
└─ macOS/
```

### Linux/

Contains launch scripts and files for Linux systems:

```
Linux/
├─ run.sh
├─ UbuntuDiskCleanup.desktop
└─ README_LAUNCH_HERE.txt
```

### Windows/

Contains launch scripts and files for Windows systems:

```
Windows/
├─ run.bat
└─ README_LAUNCH_HERE.txt
```

### macOS/

Contains launch scripts and files for macOS systems:

```
macOS/
├─ run.command
├─ Launch_Instructions.md
└─ README_LAUNCH_HERE.txt
```

### docs/

Optional folder for documentation, screenshots, or diagrams.

**Main Application:** The main GUI application `cleanup_gui.py` is located in the root directory and is shared across all platforms.

---

## Installation

### Linux/macOS

1. Clone or download the repository.
2. Ensure Python 3 and tkinter are installed.
3. Make scripts executable if necessary:

```bash
chmod +x Linux/run.sh
chmod +x macOS/run.command
```

4. Launch:

```bash
# Linux
cd Linux && ./run.sh
# macOS
cd macOS && ./run.command
```

Or double-click `UbuntuDiskCleanup.desktop` on Linux (after copying to desktop).

### Windows

1. Clone or download the repository.
2. Ensure Python 3 and tkinter are installed.
3. Navigate to the Windows folder and double-click `run.bat` to launch.

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
