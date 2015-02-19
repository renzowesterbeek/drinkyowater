#!/bin/bash

echo "Updating application..."
cd ..
rm -rf drinkyowater
git clone https://github.com/renzowesterbeek/drinkyowater.git
mv drinkyowater drinkyowaterlatest