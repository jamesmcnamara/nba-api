from __future__ import (print_function, absolute_import, division,
	                    unicode_literals)

import os

from nba.app import app
from nba import routes


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)