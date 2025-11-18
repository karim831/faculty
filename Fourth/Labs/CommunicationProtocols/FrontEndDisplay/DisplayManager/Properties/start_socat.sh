#!/bin/bash

#tunnel between /tmp/vterm0 and /tmp/vterm1
socat -d -d -d PTY,link=/tmp/vterm0,raw,echo=0 PTY,link=/tmp/vterm1,raw,echo=0
