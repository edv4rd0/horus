from flask import Flask

app = Flask(__name__)

import horus.models
import horus.views
