# -*- coding: utf-8 -*-
# See LICENSE.txt for licensing terms
#$URL$
#$Date$
#$Revision$

# Import all node handler modules here.
# The act of importing them wires them in.

import genelements
import genpdftext

#sphinxnodes needs these
from genpdftext import NodeHandler, FontHandler, HandleEmphasis

# createpdf needs this
nodehandlers = NodeHandler()
