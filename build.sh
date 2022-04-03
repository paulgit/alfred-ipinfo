#!/bin/bash

WORKFLOW_NAME="ipinfo"
SCRIPT_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BUILD_FOLDER="$SCRIPT_FOLDER/build"
SOURCE_FOLDER="$SCRIPT_FOLDER/source"
WORKFLOW_FILE="$BUILD_FOLDER/${WORKFLOW_NAME}.alfredworkflow"

# Start building the alfred workflow
echo "Building $WORKFLOW_NAME"

# Empty build folder
rm -rf "$BUILD_FOLDER/"
mkdir -p "$BUILD_FOLDER" > /dev/null
cd "$SOURCE_FOLDER"
zip -rq "$WORKFLOW_FILE" *

# Done!
echo "Complete!"
