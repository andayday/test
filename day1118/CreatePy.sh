#!/bin/bash

Filename=$1
if [ -f ${Filename} ];then
	echo "The File is exist"
	exit 1;
fi

CreateFilename=${Filename}".py"
touch ${CreateFilename}
echo "Create ${CreateFilename} Success"

chmod u+x ${CreateFilename}
echo '#!/usr/bin/env python3' > ${CreateFilename}
