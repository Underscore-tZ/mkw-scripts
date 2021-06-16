__author__ = "_tZ"
__version__ = "0.1"

from BrawlCrate.API import *
from BrawlCrate.NodeWrappers import MDL0EntryWrapper
from System.Windows.Forms import ToolStripMenuItem
from BrawlLib.SSBB.ResourceNodes import ResourceType
from BrawlLib.Internal import Vector3

qprint = lambda x: BrawlAPI.ShowMessage( str(x) , "Q")

def EnableCheck(sender, event_args):
    # only enable for normals
    sender.Enabled = (BrawlAPI.SelectedNode.ResourceFileType == ResourceType.MDL0Normal)


def on_normalize(sender, event_args):
    normal_node = BrawlAPI.SelectedNode
    # qprint( dir(normal_node) )
    for i in range(0, normal_node.NumEntries):
        normal_node.Normals[i] = normal_node.Normals[i].Normalize()

    # have to do this to get it to rebuild lol
    normal_node.ForceRebuild = True
    normal_node.Rebuild()

# add to right click menu
BrawlAPI.AddContextMenuItem(MDL0EntryWrapper, "", "Normalize", EnableCheck, ToolStripMenuItem("Normalize", None, on_normalize))
