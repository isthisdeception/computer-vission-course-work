"""Reusable, secret-safe Kaggle -> GitHub auto-sync helper for GROUP 08."""

from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path
from typing import Dict, Iterable, Optional

REPO_URL = "https://github.com/isthisdeception/computer-vission-course-work.git"
DEFAULT_BRANCH = "main"
SECRET_CANDIDATES = (
    "GITHUB_TOKEN",
    "GH_TOKEN",
    "GITHUB_PAT",
    "GIT_TOKEN",
    "GITHUB_ACCESS_TOKEN",
    "github_token",
)


def get_github_token(secret_names: Iterable[str] = SECRET_CANDIDATES) -> tuple[str, str]:
    """Retrieve a GitHub personal access token from Kaggle Secrets or environment."""
    # 1. Try Kaggle Secrets first
    try:
        from kaggle_secrets import UserSecretsClient

        client = UserSecretsClient()
        for name in secret_names:
            try:
                val = client.get_secret(name)
                if val and val.strip():
                    return val.strip(), f"kaggle_secret:{name}"
            except Exception:
                continue
    except ImportError:
        pass

    # 2. Fallback to environment variables
    for name in secret_names:
        val = os.environ.get(name, "").strip()
        if val:
            return val, f"env:{name}"

    raise RuntimeError(
        "GitHub token not found! In Kaggle Notebook, open Add-ons -> Secrets, "
        "enable 'GITHUB_TOKEN', and re-run."
    )


def _run_masked(cmd: list[str], cwd: Optional[Path] = None, secret: Optional[str] = None) -> str:
    """Run subprocess while guaranteeing the secret never appears in stdout/stderr/errors."""
    res = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, check=False)
    mask = (lambda text: text.replace(secret, "***")) if secret else (lambda text: text)
    stdout = mask(res.stdout.strip())
    stderr = mask(res.stderr.strip())
    if stdout:
        print(stdout)
    if res.returncode != 0:
        if stderr:
            print(stderr)
        raise RuntimeError(f"Command failed (rc={res.returncode}): {mask(' '.join(cmd))}")
    return stdout


def push_outputs_to_github(
    file_map: Dict[Path | str, str],
    commit_message: str,
    *,
    repo_url: str = REPO_URL,
    branch: str = DEFAULT_BRANCH,
    git_user_name: str = "Assaduzzaman",
    git_user_email: str = "md.assaduzzaman99@gmail.com",
    work_dir: Path = Path("/kaggle/working/_repo_sync"),
    post_copy_hook=None,
) -> str:
    """Clone latest repo, copy outputs, commit, and push back to GitHub with masked credentials."""
    token, source = get_github_token()
    print(f"[sync] Loaded GitHub token from {source} (masked).")

    if work_dir.exists():
        shutil.rmtree(work_dir)

    auth_url = repo_url.replace("https://", f"https://x-access-token:{token}@", 1)

    _run_masked(
        ["git", "clone", "--depth", "1", "--branch", branch, auth_url, str(work_dir)],
        secret=token,
    )
    # Strip token from local .git/config immediately
    _run_masked(["git", "remote", "set-url", "origin", repo_url], cwd=work_dir, secret=token)
    _run_masked(["git", "config", "user.name", git_user_name], cwd=work_dir, secret=token)
    _run_masked(["git", "config", "user.email", git_user_email], cwd=work_dir, secret=token)

    for src_item, rel_dst in file_map.items():
        src_path = Path(src_item)
        if not src_path.is_file():
            raise FileNotFoundError(f"Expected output file missing: {src_path}")
        dst_path = work_dir / rel_dst
        dst_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src_path, dst_path)
        print(f"[sync] Staged {src_path.name} -> {rel_dst}")

    if callable(post_copy_hook):
        post_copy_hook(work_dir)

    _run_masked(["git", "add", "-A"], cwd=work_dir, secret=token)
    status = _run_masked(["git", "status", "--porcelain"], cwd=work_dir, secret=token)
    if not status.strip():
        print("[sync] No changes detected; repository is already up to date.")
        return _run_masked(["git", "rev-parse", "--short", "HEAD"], cwd=work_dir, secret=token)

    _run_masked(["git", "commit", "-m", commit_message], cwd=work_dir, secret=token)
    _run_masked(["git", "push", auth_url, f"HEAD:refs/heads/{branch}"], cwd=work_dir, secret=token)
    commit_sha = _run_masked(["git", "rev-parse", "--short", "HEAD"], cwd=work_dir, secret=token)
    print(f"[sync] SUCCESS! Pushed commit {commit_sha} to {repo_url} ({branch})")
    return commit_sha
