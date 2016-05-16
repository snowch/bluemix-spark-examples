#!/bin/bash

tar cf secrets.tar connection.properties vcap.json examples/DashDB/lib/*
travis encrypt-file secrets.tar
