#!/bin/bash
elixirc --ignore-module-conflict *.ex && elixir "$@"
