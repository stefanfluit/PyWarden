#!/usr/bin/env bash
# -*- coding: utf-8 -*-

set -e

fetch_version() {
    local version
    version="$(cd pywarden/pywarden && python3 -c 'import version; print(version.pywarden_version())')"
    printf "%s\n" "$version"
}

run_build() {
    # Set version
    local VERSION
    VERSION="$(fetch_version)"

    # Ensure dist directory is empty
    rm -rf dist/*

    # Fetch version from setup.cfg
    VERSION=$(grep -oP '(?<=^version = ).*' setup.cfg)
    printf "Building version %s\n" "${VERSION}"

    VERSION=$(echo "${VERSION}" | awk -F. '{$NF = $NF + 1;} 1' | sed 's/ /./g')
    printf "New version %s\n" "${VERSION}"

    # Update version in setup.cfg
    sed -i "s/^version = .*/version = ${VERSION}/" setup.cfg
    sed -i "s/^version = .*/version = ${VERSION}/" pywarden/pywarden/version.py

    printf "Building wheel..\n"
    python3 -m build && \
    printf "Uploading to PyPI..\n"
    python3 -m twine upload dist/* && \
    printf "Done!\n"

    # Git 
    git add setup.cfg && \
    git commit -m "Bump version to ${VERSION}" && \
    git push
}

run_test() {
    # Ensure dist directory is empty
    rm -rf dist/*
    # Fetch version from setup.cfg
    VERSION=$(grep -oP '(?<=^version = ).*' setup.cfg)
    printf "Building version %s\n" "${VERSION}"
    # Run build
    python3 -m build && \
    # Install using pip
    python3 -m pip install dist/*.whl --force-reinstall
    # Run tests
}

declare param
param="${1:-}"

case "${param}" in
    test)
        run_test
        ;;
    build)
        run_build
        ;;
    *)
        printf "Usage: %s {test|build}\n" "${0}"
        exit 1
esac
