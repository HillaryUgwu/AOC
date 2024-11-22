# Creating and managing a systemd service file to execute a python script

## 1. *Create the Service File*
Use the nano text editor (or your preferred text editor) to create a new service file in the /etc/systemd/system/ directory.
```bash
sudo nano /etc/systemd/system/validation_test_script.service 
```

## 2. *Define the Service*
```
[Unit]
Description=MCX Python Script
After=network.target

[Service]
Type=simple
User=admin
WorkingDirectory=/home/admin/pyscripts/
ExecStart=/usr/bin/python3 /home/admin/pyscripts/main_script.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## 3. *Set Permissions*
Set correct file permission.
```bash
sudo chmod  644 /etc/systemd/system/my_python_script.service
```

## 4. *Reload Systemd*
Reload the systemd daemon to recognize the new service file.
```bash
sudo systemctl daemon-reload
```

## 5. Manage systemd Service
### 5.1. *Enable the Service*
Set the service to start automatically at boot time (should be run only once).
```bash
sudo systemctl enable validation_test_script.service
```

### 5.2. *Disable the Service*
Do not stop a running service but prevent it from starting automatically on the next boot.
```bash
sudo systemctl disable validation_test_script.service
```

### 5.3. *Mask the Service*
Completely prevent the service from being started, either manually or automatically.
```bash
sudo systemctl mask validation_test_script.service
```

### 5.4. *Unmask the Service*
Reverse the effect of masking and allow the service to be started again.
```bash
sudo systemctl unmask validation_test_script.service 
```

### 5.5. *check if the Service is enabled on startup*
Return whether the service is enabled, disabled or static (cannot be enabled or disabled).
```bash
sudo systemctl is-enabled validation_test_script.service
```

### 5.6. *Start the Service*
Manually start the service without modifying its ability to start on boot.
```bash
sudo systemctl start validation_test_script.service 
```

### 5.7. *Stop the Service*
Manually stop the currently running service but will not affect its startup configuration.
```bash
sudo systemctl stop validation_test_script.service 
```

### 5.8. *Restart the Service*
Manually stop and then start the service again.
```bash
sudo systemctl restart validation_test_script.service 
```

## 6. *Check Status*
Verify that the service is currently running. It shows whether the service is active, inactive, or failed, along with recent log entries
```bash
sudo systemctl status validation_test_script.service  
```

## 7. *View Logs*
If you encounter any issues, view the logs for the service. It shows more detailed messages and log entries (in reverse order - starting from most recent).
```bash
journalctl -u validation_test_script.service -r
```

# Vscode extension.json

```json
{
    "recommendations": [
        "ms-python.python",
        "ms-python.vscode-pylance",
        "charliermarsh.ruff",
        "github.copilot",
        "tamasfe.even-better-toml",
        "aaron-bond.better-comments",
        "github.vscode-github-actions",
        "bierner.markdown-mermaid",
        "ms-vscode-remote.remote-containers",
    ]
}
```

# Vscode setting.json
## Folder setting
```json
{
    // Python settings
    "python.analysis.autoSearchPaths": true,
    "python.analysis.diagnosticSeverityOverrides": {
        "reportMissingImports": "none"
    },
    "python.analysis.extraPaths": [
        "${workspaceFolder}/src"
    ],
    "python.envFile": "${workspaceFolder}/.env",
    "python.terminal.activateEnvironment": true,
    "terminal.integrated.env.linux": {
        "PYTHONPATH": "${workspaceFolder}:${env:PYTHONPATH}"
    },
    "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
    // Test settings
    "python.testing.pytestEnabled": true,
    "python.testing.unittestEnabled": false,
    "python.testing.cwd": "${workspaceFolder}/tests",
    "python.testing.pytestPath": "${workspaceFolder}/.venv/bin/pytest",
    "python.testing.autoTestDiscoverOnSaveEnabled": true,
}
```

## User setting
```json
{
    // General settings
    "security.workspace.trust.untrustedFiles": "newWindow",
    "window.zoomLevel": 0,
    "window.commandCenter": false,
    "files.exclude": {
        ".git": true,
        "**/.git": false
    },
    "extensions.autoUpdate": "onlyEnabledExtensions",
    // Git settings
    "git.autofetch": true,
    "git.confirmSync": false,
    "git.enableSmartCommit": true,
    "git.showActionButton": {
        "commit": false,
        "publish": false,
        "sync": false
    },
    "github.copilot.enable": {
        "*": true,
        "plaintext": false,
        "scminput": false,
        "yaml": true
    },
    // Explorer settings
    "explorer.excludeGitIgnore": true,
    "explorer.autoReveal": true,
    "explorer.confirmDelete": false,
    "explorer.confirmDragAndDrop": false,
    // Workbench settings
    "workbench.colorTheme": "Default Dark+",
    "workbench.iconTheme": "ayu",
    "workbench.editor.enablePreview": false,
    "workbench.editor.tabSizing": "shrink",
    "workbench.settings.editor": "json",
    // Editor settings
    "ruff.importStrategy": "useBundled",
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnPaste": true,
    "editor.formatOnSave": true,
    "editor.formatOnSaveMode": "file",
    "editor.codeActionsOnSave": {
        "source.organizeImports": "always",
        "source.fixAll": "always"
    },
    // "pylint.args": [
    //     "--max-line-length=150"
    // ],
    "files.autoSave": "onFocusChange",
    "[json]": {
        "editor.defaultFormatter": "vscode.json-language-features"
    },
    "[jsonc]": {
        "editor.defaultFormatter": "vscode.json-language-features"
    },
    // Debug settings
    "debug.toolBarLocation": "docked",
    // Terminal settings
    "terminal.integrated.tabs.enabled": true,
    "terminal.integrated.tabs.hideCondition": "never",
    "terminal.integrated.tabs.location": "right",
    // Markdown settings
    "markdown.preview.scrollEditorWithPreview": true,
    "markdown.preview.scrollPreviewWithEditor": true
}
```
