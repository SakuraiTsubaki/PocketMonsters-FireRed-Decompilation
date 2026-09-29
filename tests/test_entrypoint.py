from __future__ import annotations
import hashlib,json,re,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class EntrypointTests(unittest.TestCase):
 def test_entry_evidence_and_source_agree(self):
  r=json.loads((ROOT/"analysis"/"firered-jp-entrypoint.json").read_text(encoding="utf-8"));s=(ROOT/"src"/"rom_entry.s").read_text(encoding="utf-8");self.assertEqual(r["source_sha256"],"1e4af44b0c75cc8649bfb8649dc4ae5850bf5358bd6b9cd0bf779c99f9db1486");self.assertEqual((r["instruction_word"],r["target_address"]),(0xEA00007F,0x08000204));self.assertEqual(int(re.search(r"\.word 0x([0-9a-f]+)",s).group(1),16),r["instruction_word"])
 def test_manifest_hashes_outputs(self):
  m=json.loads((ROOT/"manifests"/"entrypoint.json").read_text(encoding="utf-8"));
  for o in m["outputs"]:self.assertEqual(hashlib.sha256((ROOT/o["path"]).read_bytes()).hexdigest(),o["sha256"])
if __name__=="__main__":unittest.main()
