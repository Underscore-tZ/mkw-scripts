__author__ = "_tZ"
__version__ = "0.1"

from BrawlCrate.API import *
from BrawlCrate.NodeWrappers import MDL0EntryWrapper, MDL0ColorWrapper
from System.Windows.Forms import ToolStripMenuItem
from BrawlLib.SSBB.ResourceNodes import ResourceType
from BrawlLib.Imaging import ARGBPixel

qprint = lambda x: BrawlAPI.ShowMessage( str(x) , "Q")

def EnableCheck(sender, event_args):
    # redundant
    sender.Enabled = (BrawlAPI.SelectedNode.ResourceFileType == ResourceType.MDL0Color)


def on_setalpha(sender, event_args):
    color_node = BrawlAPI.SelectedNode
    qprint( dir(color_node) )

    for i in range(0, color_node.Colors.Length):
        color = color_node.GetColor(i, i)
        if color.R == color.G == color.B:
            pixel = ARGBPixel(color.R, color.R, color.G, color.B)
            color_node.SetColor(i, i, pixel)

    # rebuild
    color_node.Rebuild()

# add to right click menu
BrawlAPI.AddContextMenuItem(MDL0ColorWrapper, "", "Set Alpha Channel", EnableCheck, ToolStripMenuItem("Set Alpha Channel", None, on_setalpha))
