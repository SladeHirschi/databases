#!/bin/bash
rm test.db
sqlite3 test.db < schema.sql
sqlite3 test.db < dummyData.sql

python3 queries.py