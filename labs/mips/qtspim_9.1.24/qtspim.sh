#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)


export LD_LIBRARY_PATH=${SCRIPT_DIR}/usr/lib/qtspim/lib

export QT_QPA_PLATFORM_PLUGIN_PATH=${SCRIPT_DIR}/usr/lib/qtspim/plugins

exec ${SCRIPT_DIR}/usr/lib/qtspim/bin/qtspim
