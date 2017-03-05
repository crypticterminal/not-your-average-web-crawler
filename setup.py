# -*- coding: utf-8 -*-

# MIT License
# 
# Copyright (c) 2017 Tijme Gommers
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import find_packages, setup

setup(
    name="crawl-like-a-sir",
    version="0.0.1",
    description="A web crawler that gathers requests instead of URLs.",
    long_description="""A very useful web crawler for vulnerability scanning. Crawl Like A Sir (C.L.A.S) is a Python application that enables you to crawl web applications for requests instead of URLs. It crawls every GET and POST request on the specified domain and keeps track of the request and response data. It's main purpose is to be used in web application vulnerability scanners like Angular CSTI scanner (https://github.com/tijme/angular-csti-scanner).""",
    author="Tijme Gommers",
    author_email="tijme@finnwea.com",
    platforms=["any"],
    license="MIT",
    url="https://github.com/tijme/crawl-like-a-sir",
    packages=find_packages(),
    install_requires=[i.strip() for i in open("requirements.txt").readlines()]
)