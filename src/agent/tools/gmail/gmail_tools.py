"""
Gmail tools implementation module. 
This module formats the Gmail API functions into LangChain tools.
"""

import os
import sys
import base64
import email.utils
import json
import logging
from datetime import datetime
from typing import List, Optional, Dict, Any, Iterator
from pathlib import Path
from pydantic import Field, BaseModel
from langchain_core.tools import tool

