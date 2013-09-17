#!/bin/bash

cd `dirname "$0"`;
source venv/bin/activate;

if [ $# -eq 0 ]  || [[ $# -gt 0  &&  -z "$1" ]]
then
	# Launch the app in background
	{{launch}} &
else
	echo $1;
	$1 &
fi

# After launch
{% if after_launch %}
{{after_launch}}
{% endif %}
