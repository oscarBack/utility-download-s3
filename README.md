# download_s3_files.py — README

Overview
- Small utility to bulk-download objects from an S3 bucket into a local folder.
- `download_s3_files.py` automatically loads configuration from a `.env` file (via python-dotenv).

Prerequisites
- Python 3.8+ (or your project's required Python)
- A virtual environment for isolation (recommended)
- AWS credentials with permission to list and get objects from the target bucket

Quick setup
1. Create and activate a virtualenv (optional but recommended):

```bash
python -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

Configuration
- Create a `.env` file in the project root (the script already includes an example `.env`).
- Required keys (example, do NOT commit real secrets):

```
BUCKET_NAME="your-bucket-name"
S3_PREFIX="optional/prefix/"
LOCAL_DIRECTORY="/path/to/downloaded_files"
AWS_REGION="us-east-1"
AWS_ACCESS_KEY_ID="<your-access-key>"
AWS_SECRET_ACCESS_KEY="<your-secret-key>"
```

Notes:
- The script will call `load_dotenv()` at startup, so environment variables from `.env` are used automatically.
- Alternatively, you can provide credentials via `~/.aws/credentials` or environment variables set in the shell.

Run
- With the virtualenv activated and a `.env` file present:

```bash
python download_s3_files.py
```

- Or run with inline environment variables (example):

```bash
AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=... BUCKET_NAME=... python download_s3_files.py
```

Security
- Do NOT commit `.env` with secrets. Add `.env` to `.gitignore`.
- Consider using IAM roles or the AWS CLI credential store for safer credential management.

Troubleshooting
- "Unable to locate credentials": verify `AWS_ACCESS_KEY_ID`/`AWS_SECRET_ACCESS_KEY` are set or that `~/.aws/credentials` exists.
- Permission errors: ensure the IAM user/role has `s3:ListBucket` and `s3:GetObject` for the target bucket/prefix.

If you'd like, I can also add a `.gitignore` entry or a small safety check in the script to avoid overwriting files.
