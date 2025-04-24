#!/bin/bash

if [ -z "$1" ]; then
  echo "Usage: $0 <room-name>"
  exit 1
fi

ROOM_NAME="$1"
FILE_NAME="${ROOM_NAME}.md"

cat << EOF > "$FILE_NAME"
# ${ROOM_NAME//-/ }

## Overview
*Write a brief summary of what this room is about.*

## Key Concepts
- 

## Commands Used
\`\`\`bash
# Example
\`\`\`

## What I Learned
*Write what you personally understood or struggled with here.*

## Room Link
[TryHackMe Room](https://tryhackme.com/room/{$ROOM_NAME})
EOF

