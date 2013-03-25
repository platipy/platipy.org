#!/bin/bash
cd ..
source ~/venvs/platipy/bin/activate
git checkout ${1}
git pull
cd site
make html
if [ "${1}" == "dev" ]; then
	cp -r _build/html/* /www/dev.platipy.org
fi
if [ "${1}" == "master" ]; then
	cp -r _build/html/* /www/platipy.org
fi
