# Obtain shared config values
import sys
from pathlib import Path
from os.path import abspath, join, dirname
ROOT = Path(__file__).resolve().parents[2]
sys.path.append(abspath(join(dirname(__file__), "..")))
sys.path.append(abspath(join(dirname(__file__), "..", "..")))
from shared_conf import *

# Enable & configure autodoc
extensions.append("sphinx.ext.autodoc")
autodoc_default_flags = ["members", "special-members"]

# Default is 'local' building, but reference the public WWW site when building
# under RTD.
target = join(dirname(__file__), "..", "www", "_build")
if on_rtd:
    target = "https://www.fabfile.org/"
www = (target, None)
# Intersphinx connection to www site
intersphinx_mapping.update({"www": www})

# Sister-site links to WWW
html_theme_options["extra_nav_links"] = {
    "Main website": "https://daobook.github.io/fabric/www/"
}

language = 'zh_CN'
locale_dirs = [str(ROOT/'sites/docs/locales/')]  # path is example but recommended.
print('ROOT', ROOT)
gettext_compact = False  # optional.