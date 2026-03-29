#!/bin/bash
export PATH="/root/.openfang/bin:${PATH}"

# Start OpenFang daemon in foreground
exec openfang start
