#!/bin/bash
export PATH="/root/.openfang/bin:${PATH}"

# Start OpenFang daemon in background
openfang start &
DAEMON_PID=$!

# Wait for API to be ready
sleep 5

# Get agent ID and set Atlas system prompt from SKILL.md
AGENT_ID=$(curl -s http://localhost:4200/api/agents | python3 -c "import sys,json; print(json.load(sys.stdin)[0]['id'])" 2>/dev/null)
if [ -n "$AGENT_ID" ]; then
  SKILL=$(python3 -c "import json; print(json.dumps(open('/root/.openfang/hands/atlas/SKILL.md').read()))")
  curl -s -X PATCH "http://localhost:4200/api/agents/$AGENT_ID" \
    -H 'Content-Type: application/json' \
    -d "{\"name\":\"atlas\",\"system_prompt\":$SKILL}" > /dev/null 2>&1
  echo "Atlas system prompt loaded for agent $AGENT_ID"
fi

# Wait for daemon
wait $DAEMON_PID
