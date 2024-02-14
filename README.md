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

# Vscode setting.json
```
{
    "workbench.colorTheme": "Predawn",
    "workbench.iconTheme": "ayu",
    "python.defaultInterpreterPath": "/usr/bin/python3",
    "python.formatting.provider": "black",
    "workbench.editor.highlightModifiedTabs": true,
    "editor.formatOnSave": true,
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "code-runner.executorMap": {
        "python": "$pythonPath -u $fullFileName"
    },
    "code-runner.clearPreviousOutput": true,
    "code-runner.showExecutionMessage": false,
    "code-runner.ignoreSelection": true,
    "code-runner.saveFileBeforeRun": true,
    "editor.quickSuggestionsDelay": 100,
    "zenMode.centerLayout": false,
    "zenMode.fullScreen": false,
    "zenMode.hideLineNumbers": false,
    "zenMode.hideTabs": false,
    "editor.minimap.enabled": false,
    "workbench.settings.openDefaultSettings": true,
    "workbench.settings.editor": "json",
    "workbench.settings.useSplitJSON": true,
    "workbench.statusBar.feedback.visible": false,
    "workbench.startupEditor": "newUntitledFile",
    "[python]": {
        "editor.formatOnType": true
    }
}
```
