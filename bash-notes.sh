# !/bin/bash

# git
git config --list --show-origin
git log --pretty=format:"%h-(%an, %cn): %s" -p --graph

# git-lfs
git lfs install
git lfs track "*.pdf"
git lfs track "*.jpg"
git lfs track "*.jpeg"
git lfs track "*.png"
git lfs track "*.otf"
git lfs track "*.ttf"
