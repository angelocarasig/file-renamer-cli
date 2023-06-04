# Python Scripts
A collection of helpful scripts. More often than not, these are scripts to do with file system management.

# file renamer
Useful for removing certain substrings such as file extensions from the current working directory (works on both files and directories).

# file date grouper
Organizes all files in a folder based on month and year.

# file-folder-renamer

NOTE: Depth limited to 1 (not going to bother for more unless use-case gets extended)

Sample before/after structure
```
root_folder/
├── subfolder1/
│   ├── data1
│   ├── data2
│   └── data3
├── subfolder2/
│   ├── data1
│   ├── data2
│   └── data3
└── subfolder3/
    ├── data1
    ├── data2
    └── data3
```

```
root_folder/
├── subfolder1/
│   ├── [data1] subfolder1
│   ├── [data2] subfolder1
│   └── [data3] subfolder1
├── subfolder2/
│   ├── [data1] subfolder2
│   ├── [data2] subfolder2
│   └── [data3] subfolder2
└── subfolder3/
    ├── [data1] subfolder3
    ├── [data2] subfolder3
    └── [data3] subfolder3
```