from  .core import *
TYPENAMES = []

#----------------------------------------------------------------   
class VTK2Blender(Node, VTKTreeNode):

    bl_idname = 'VTK2BlenderType' # type name
    bl_label  = 'ToBlender'       # label for nice name display 
    m_Name = bpy.props.StringProperty( name="Name", default="mesh")

    def m_properties(self):
        return ['m_Name']

    def m_outputs(self):
        return []

    def init(self, context):
        self.width = 150
        self.inputs.new('VTKPolyDataSocketType', "in")
        node_created( self )

    def draw_buttons(self, context, layout):
        layout.prop(self, "m_Name")
        layout.operator("node.update", text="update").node_id = self.node_id
        #layout.operator("node.print").node_id = self.node_id

    def apply_properties(self, vtkobj):
        pass

CLASSES.append  (  VTK2Blender )        
TYPENAMES.append( 'VTK2BlenderType' )

#----------------------------------------------------------------   
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( VTKNodeCategory("converters", "converters", items=menu_items) )