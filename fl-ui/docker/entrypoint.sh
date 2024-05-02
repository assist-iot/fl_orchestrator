#!/bin/sh
set -eu

echo "Generating default.conf nginx file"
envsubst '${FL_GUI_UI_HOST_PORT}' < /etc/nginx/templates/default.conf.template > /etc/nginx/conf.d/default.conf

# Replace env vars in JavaScript files
echo "Replacing env constants in JS"
ROOT_DIR=/usr/share/nginx/html
for file in $ROOT_DIR/config.js;
do
  echo "Processing $file ...";

  sed -i 's|FL_GUI_API_HOST_NAME_VALUE|'${FL_GUI_API_HOST_NAME}'|g' $file 
  sed -i 's|FL_GUI_API_PORT_VALUE|'${FL_GUI_API_PORT}'|g' $file
  sed -i 's|FL_GUI_API_WS_PORT_VALUE|'${FL_GUI_API_WS_PORT}'|g' $file

done

echo "Starting Nginx"
nginx -g 'daemon off;'