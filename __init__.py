import ranger.api
from ranger.core.linemode import LinemodeBase
from ranger.ext.human_readable import human_readable, human_readable_time
from datetime import datetime
from .devicons import *

@ranger.api.register_linemode
class DevIconsLinemode(LinemodeBase):
  name = "devicons"

  uses_metadata = False

  def filetitle(self, file, metadata):
    return devicon(file) + ' ' + file.relative_path

@ranger.api.register_linemode
class DevIconsLinemodeFile(LinemodeBase):
  name = "filename"

  def filetitle(self, file, metadata):
    return devicon(file) + ' ' + file.relative_path

@ranger.api.register_linemode
class DevIconsLinemode(LinemodeBase):
  name = "sizemtime"

  uses_metadata = False

  def filetitle(self, file, metadata):
    return devicon(file) + ' ' + file.relative_path

  def infostring(self, fobj, metadata):
    if fobj.stat is None:
      return '?'
    return "%s %s" % (human_readable(fobj.size),
                      datetime.fromtimestamp(fobj.stat.st_mtime).strftime("%Y-%m-%d %H:%M"))
