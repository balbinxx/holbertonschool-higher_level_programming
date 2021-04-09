#!/bin/bash
# Methods that server accepts
curl -sI $1 | grep "Allow" | cut -d " " -f2-
