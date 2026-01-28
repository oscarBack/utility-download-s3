# 📥 download_s3_files.py

> A lightweight utility to bulk-download objects from an AWS S3 bucket into a local folder

---

## ✨ Overview

- **Automated S3 Downloads** — Efficiently bulk-download objects from an S3 bucket
- **Environment Configuration** — Loads settings from a `.env` file using python-dotenv
- **Simple & Secure** — Minimal setup with clear credential management

## 📋 Prerequisites

- **Python 3.8+** (or your project's required version)
- **Virtual environment** (recommended for isolation)
- **AWS credentials** with `s3:ListBucket` and `s3:GetObject` permissions for your target bucket

## 🚀 Quick Start

### 1️⃣ Setup Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment

Create a `.env` file in the project root with your AWS credentials:

```env
BUCKET_NAME="your-bucket-name"
S3_PREFIX="optional/prefix/"
LOCAL_DIRECTORY="/path/to/downloaded_files"
AWS_REGION="us-east-1"
AWS_ACCESS_KEY_ID="<your-access-key>"
AWS_SECRET_ACCESS_KEY="<your-secret-key>"
```

> **Note:** The script automatically loads environment variables from `.env` at startup.

### 4️⃣ Run the Script

```bash
python download_s3_files.py
```

**Alternative:** Provide credentials inline:
```bash
AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=... BUCKET_NAME=... python download_s3_files.py
```

## 🔐 Security Best Practices

⚠️ **Important:**
- **Never commit** `.env` with real secrets — add it to `.gitignore`
- Use **AWS IAM roles** or the **AWS CLI credential store** for production
- Ensure your IAM user/role has appropriate S3 permissions

```gitignore
# Add to .gitignore
.env
.env.local
__pycache__/
.venv/
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| ❌ "Unable to locate credentials" | Verify `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are set, or check `~/.aws/credentials` |
| ❌ Permission errors | Ensure IAM user/role has `s3:ListBucket` and `s3:GetObject` permissions |
| ❌ Files not found | Check `S3_PREFIX` and `BUCKET_NAME` configuration |

## 💡 Additional Notes

- Supports **alternative credential sources**: `~/.aws/credentials` or shell environment variables
- **Automatic directory creation**: Creates `LOCAL_DIRECTORY` if it doesn't exist
- Consider adding a safety check to avoid overwriting existing files if needed

---

**Happy downloading!** 🎉
