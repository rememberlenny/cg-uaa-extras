#!/usr/bin/env python
"""Run the webapp in debug mode"""

from uaaextras.webapp import create_app

if __name__ == "__main__":
    app = create_app()

    app.run(debug=True)
