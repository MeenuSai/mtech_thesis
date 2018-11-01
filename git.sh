#!/bin/bash
echo "Initiating Git update"
git add .
sleep 1
echo "40% complete"
git commit -m "auto update"
sleep 2
echo "80% complete"
git push

echo "update completed"
