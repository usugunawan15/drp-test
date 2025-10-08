cat > testt.sh <<'EOF'
#!/usr/bin/env bash
set -euo pipefail

# File akan dibuat di direktori saat ini (tempat kamu menjalankan script)
FILE_NAME="test_output.txt"

echo "testing" > "$FILE_NAME"

echo "✅ File created at: $(pwd)/$FILE_NAME"
echo "   Content:"
cat "$FILE_NAME"
EOF
