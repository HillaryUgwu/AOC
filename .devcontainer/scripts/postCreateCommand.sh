#!/bin/bash

BASE_PATH="/aoc"

ENVIRONMENT=$BASE_PATH/.env
DEVELOPMENT_ENVIRONMENT=$BASE_PATH/.env.development

sudo groupmod -n dev vscode

# Copy the development environment file to the actual environment file if it doesn't exist
if [ ! -f $ENVIRONMENT ]
then
	cp $DEVELOPMENT_ENVIRONMENT $ENVIRONMENT
fi

# Determine the architecture of the machine
ARCH=$(lscpu | grep Architecture | awk '{print $2}')

if [ "$ARCH" == "aarch64" ]
then
    SLS_ARCH="arm64"
elif [ "$ARCH" == "x86_64" ]
then
    SLS_ARCH="x86_64"
else
    SLS_ARCH="unknown"
fi

# Replace the placeholder "<YOUR MACHINE ARCHITECTURE>" in the .env file with the actual architecture
if [ "$SLS_ARCH" != "unknown" ]
then
	sed -i "s/<YOUR MACHINE ARCHITECTURE>/$SLS_ARCH/" $ENVIRONMENT
fi

# Install dependencies
uv venv --seed $VIRTUAL_ENV
uv pip install -r requirements-dev.txt

# Generate uv & ruff shell autocompletions
uv generate-shell-completion zsh > ~/.zfunc/_uv
ruff generate-shell-completion zsh > ~/.zfunc/_ruff

# Update npm & install dependencies
npm install npm@latest -g
npm clean-install

# If pytest-xdist is installed, add an alias to run tests in parallel
uv pip show pytest-xdist
if [ $? -eq 0 ]
then
	echo "alias pytest-fast='pytest -n auto'" >> ~/.zshrc
fi

# # serverless patches - it's wild out here in the serverless world + the fixes are a bit hacky, but it's the only way to make things work
# PYTHON_VERSION=$(python3 -c "import sys; print(f'python{sys.version_info.major}.{sys.version_info.minor}')")

# # Patch serverless to support python 3.12 (or our current newer version), see https://github.com/serverless/serverless/pull/12300
# SLS_PLUGIN_PATH="$BASE_PATH/node_modules/serverless/lib/plugins/aws"
# sed -i "/'python3.7', 'python3.8', 'python3.9', 'python3.10', 'python3.11'/ s/].includes/, '$PYTHON_VERSION'].includes/" $SLS_PLUGIN_PATH/invoke-local/index.js
# sed -i "/'python3.11',/a \              '$PYTHON_VERSION'," $SLS_PLUGIN_PATH/provider.js

# # Patch serverless-offline to support binary response from AWS λ, since our route decorator encodes them with utf-8
# SLS_OFFLINE_HANDLER="$BASE_PATH/node_modules/serverless-offline/src/lambda/handler-runner/python-runner"
# sed -i '104a\        if data is not None and '\''__offline_payload__'\'' in data and isinstance(data['\''__offline_payload__'\''], dict) and '\''body'\'' in data['\''__offline_payload__'\''] and isinstance(data['\''__offline_payload__'\'']['\''body'\''], bytes):\n            data['\''__offline_payload__'\'']['\''body'\''] = data['\''__offline_payload__'\'']['\''body'\''].decode('\''utf-8'\'')\n' $SLS_OFFLINE_HANDLER/invoke.py

# # Patch serverless-offline to support python 3.12 (or our current newer version), see https://github.com/dherault/serverless-offline/pull/1761
# SLS_OFFLINE_CONFIG_PATH="$BASE_PATH/node_modules/serverless-offline/src/config"
# sed -i "/supportedPython = new Set(\[/ a \  \"$PYTHON_VERSION\"," $SLS_OFFLINE_CONFIG_PATH/supportedRuntimes.js

# # Patch serverless-offline-sqs to create SQS queues with '*-dlq-*' in the name before other ones. If not done, this leads to a dependency problem with dead letter queues since the other queues depend on the DLQ, see https://github.com/CoorpAcademy/serverless-plugins/issues/167
# SLS_OFFLINE_SQS_PATH="$BASE_PATH/node_modules/serverless-offline-sqs/src/"
# replacement="    const sortedEvents = events.sort((a, b) => {\n      const aContainsDlq = a.functionKey.includes('-dlq-');\n      const bContainsDlq = b.functionKey.includes('-dlq-');\n      \n      return bContainsDlq - aContainsDlq;\n    });\n\n    return sortedEvents.reduce((promiseChain, event) => {\n      return promiseChain.then(() => this._create(event.functionKey, event.sqs));\n    }, Promise.resolve());"
# sed -i "/return Promise.all(events.map(({functionKey, sqs}) => this._create(functionKey, sqs)));/c $replacement" $SLS_OFFLINE_SQS_PATH/sqs.js

# # Add uv support to serverless-python-requirements
# patch_file=$BASE_PATH/.devcontainer/scripts/patches/add_uv_support_to_serverless-python-requirements.patch
# target_file=$BASE_PATH/node_modules/serverless-python-requirements/lib/pip.js
# patch "$target_file" < "$patch_file"

# pre-commit hooks
pre-commit install --install-hooks --overwrite --hook-type pre-commit

# Remove marker file
sudo rm /home/dev/.postCreateCommandRunning

source $ENVIRONMENT
