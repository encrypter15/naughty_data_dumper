#!/usr/bin/env python3
import os, sys, logging
from argparse import ArgumentParser

# Author: Rick Hayes, Version: 1.0, License: MIT

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def dump_files(directory, output_file):
    """Dump file contents from a directory with NSFW flair."""
    try:
        if not os.path.isdir(directory):
            logger.error("Directory %s does not exist", directory)
            sys.exit(1)
        
        with open(output_file, 'w') as out:
            for root, _, files in os.walk(directory):
                for file in files:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', errors='ignore') as f:
                            content = f.read(1024)  # Limit to 1KB per file
                            out.write(f"File: {file_path}\nContent: {content}\n{'-'*50}\n")
                            logger.info("Dumped %s", file_path)
                    except Exception as e:
                        logger.warning("Failed to read %s: %s", file_path, e)
    except Exception as e:
        logger.error("Dump failed: %s", e)

if __name__ == "__main__":
    parser = ArgumentParser(description="NSFW File Dumper")
    parser.add_argument("--dir", required=True, help="Directory to scan")
    parser.add_argument("--out", default="naughty_dump.txt", help="Output file")
    args = parser.parse_args()
    dump_files(args.dir, args.out)
