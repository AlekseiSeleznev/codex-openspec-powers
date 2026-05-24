import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
OPSX = ROOT / "bin" / "opsx"
SHIM = ROOT / "bin" / "openspec-shim"


class OpsxCliTests(unittest.TestCase):
    def run_opsx(self, *args, cwd=None, env=None):
        return subprocess.run(
            [sys.executable, str(OPSX), *args],
            cwd=cwd or ROOT,
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def test_repair_restores_overwritten_prompt_from_source_bundle(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "target"
            target.mkdir()
            prompt = target / ".codex/prompts/opsx-apply.md"
            prompt.parent.mkdir(parents=True)
            prompt.write_text("upstream generated prompt without overlay markers\n", encoding="utf-8")

            result = self.run_opsx("repair", "--root", str(target), "--source-root", str(ROOT), "--yes")

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            repaired = prompt.read_text(encoding="utf-8")
            self.assertIn("Recommendation selection rule:", repaired)
            self.assertIn("**== УРОКИ ==**", repaired)
            self.assertTrue(
                (target / ".codex/codex-openspec-powers/template/.codex/prompts/opsx-apply.md").exists()
            )

    def test_repair_dry_run_reports_without_writing(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "target"
            target.mkdir()

            result = self.run_opsx("repair", "--root", str(target), "--source-root", str(ROOT), "--dry-run")

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("repair action", result.stdout)
            self.assertFalse((target / ".codex/prompts/opsx-apply.md").exists())

    def test_repair_uses_target_bundled_source_when_present(self):
        with tempfile.TemporaryDirectory() as td:
            target = Path(td) / "target"
            target.mkdir()

            first = self.run_opsx("repair", "--root", str(target), "--source-root", str(ROOT), "--yes")
            self.assertEqual(first.returncode, 0, first.stdout + first.stderr)

            prompt = target / ".codex/prompts/opsx-apply.md"
            prompt.write_text("damaged by openspec update\n", encoding="utf-8")

            second = self.run_opsx("repair", "--root", str(target), "--yes")

            self.assertEqual(second.returncode, 0, second.stdout + second.stderr)
            self.assertIn("Recommendation selection rule:", prompt.read_text(encoding="utf-8"))

    def test_shim_runs_real_openspec_then_auto_repairs_codex_init(self):
        with tempfile.TemporaryDirectory() as td:
            work = Path(td)
            fake_bin = work / "fake-bin"
            fake_bin.mkdir()
            real_openspec = fake_bin / "real-openspec"
            real_openspec.write_text(
                "#!/usr/bin/env python3\n"
                "import pathlib, sys\n"
                "target = pathlib.Path(sys.argv[-1]) if sys.argv[-1] != 'codex' else pathlib.Path.cwd()\n"
                "if target.name.startswith('--'):\n"
                "    target = pathlib.Path.cwd()\n"
                "target.mkdir(parents=True, exist_ok=True)\n"
                "(target / '.codex/prompts').mkdir(parents=True, exist_ok=True)\n"
                "(target / '.codex/prompts/opsx-apply.md').write_text('regenerated\\n')\n",
                encoding="utf-8",
            )
            real_openspec.chmod(0o755)

            opsx_link = fake_bin / "opsx"
            shutil.copy2(OPSX, opsx_link)
            opsx_link.chmod(0o755)

            target = work / "project"
            env = os.environ.copy()
            env["OPSX_REAL_OPENSPEC"] = str(real_openspec)
            env["OPSX_SOURCE_ROOT"] = str(ROOT)
            env["PATH"] = f"{fake_bin}{os.pathsep}{env.get('PATH', '')}"

            result = subprocess.run(
                [sys.executable, str(SHIM), "init", "--tools", "codex", str(target)],
                cwd=work,
                env=env,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
            )

            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            repaired = (target / ".codex/prompts/opsx-apply.md").read_text(encoding="utf-8")
            self.assertIn("Recommendation selection rule:", repaired)


if __name__ == "__main__":
    unittest.main()
