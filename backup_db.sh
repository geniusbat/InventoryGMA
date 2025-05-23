#!/bin/bash
cd <directory of backup files>
export PGPASSWORD='<password>'; pg_dump -h 127.0.0.1 -U <user> -d <db> -f igma_backup.sql
tar -czf igma_backup.tar.gz igma_backup.sql --remove-files
#Move file to parent directory. 
mv igma_backup.tar.gz ../igma_backup.tar.gz
