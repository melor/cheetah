#!/usr/bin/env python
# $Id: Servlet.py,v 1.1 2001/06/13 03:50:39 tavis_rudd Exp $
"""An abstract base class for Cheetah Servlets that can be used with Webware

Meta-Data
================================================================================
Author: Tavis Rudd <tavis@calrudd.com>,
Version: $Revision: 1.1 $
Start Date: 2001/04/05
Last Revision Date: $Date: 2001/06/13 03:50:39 $
"""
__author__ = "Tavis Rudd <tavis@calrudd.com>"
__version__ = "$Revision: 1.1 $"[11:-2]

##################################################
## DEPENDENCIES ##

import types

# intra-package imports ...
from Template import Template
from Utilities import mergeNestedDictionaries
import CodeGenerator as CodeGen

try: 
    from WebKit.HTTPServlet import HTTPServlet
except:
    class HTTPServlet:
        pass

##################################################
## GLOBALS AND CONSTANTS ##

True = (1==1)
False = (0==1)

##################################################
## CLASSES ##

class TemplateServlet(Template, HTTPServlet):
    """An abstract base class for Cheetah servlets that can be used with
    Webware"""

    def __init__(self, template='', *searchList, **kw):
        """ """
        if not kw.has_key('settings'):
            kw['settings']={}
        kw['settings']['delayedStart'] = True
        Template.__init__(self, template, *searchList, **kw)
        self.initializeTemplate()
        self.startServer()

    def initializeTemplate(self):
        """a hook that can be used by subclasses to do things after the
        Template has been initialized, but before it has been started
        (i.e. before the codeGeneration process starts) """
        pass




