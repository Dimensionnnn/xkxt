from flask import Flask, jsonify, request, make_response, url_for, redirect, render_template, session
from flask_httpauth import HTTPBasicAuth
import datetime
import json, urllib
from urllib import parse
from urllib.request import urlopen

from nameko.standalone.rpc import ClusterRpcProxy

app = Flask(__name__, static_url_path = "")
app.config['SECRET_KEY'] = '123456'
