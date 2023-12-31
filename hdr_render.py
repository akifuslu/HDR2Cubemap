import bpy
import math
import sys
import os

args = sys.argv[sys.argv.index("--") + 1:]

in_path = args[0]
out_path = bpy.path.abspath(args[1])
res = 512
z_shift = 0
x_shift = 0
y_shift = 0
if len(args) > 2:
    res = int(args[2])
if len(args) > 3:
    z_shift = int(args[3])
if len(args) > 4:
    x_shift = int(args[4])
if len(args) > 5:
    y_shift = int(args[5])

rots = [
(0 + x_shift, y_shift, 0 + z_shift),
(90 + x_shift, y_shift, 0 + z_shift),
(90 + x_shift, y_shift, 90 + z_shift),
(90 + x_shift, y_shift, 180 + z_shift),
(90 + x_shift, y_shift, 270 + z_shift),
(180 + x_shift, y_shift, 0 + z_shift),
]

# clear scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete()

# scene setup
world = bpy.data.worlds[0]
env_map_node = world.node_tree.nodes.new(type='ShaderNodeTexEnvironment')
bpy.ops.image.open(filepath=in_path)
im_name = os.path.basename(in_path)
env_map_node.image = bpy.data.images[im_name]
l1 = env_map_node.outputs[0]
l2 = world.node_tree.nodes['Background'].inputs[0]
world.node_tree.links.new(l1, l2)

# render setup
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.samples = 1
bpy.context.scene.render.image_settings.file_format = 'HDR'
bpy.context.scene.render.resolution_x = res
bpy.context.scene.render.resolution_y = res

# camera setup
bpy.ops.object.camera_add(scale=(1, 1, 1))
cam_obj = bpy.context.active_object
cam = cam_obj.data
bpy.context.scene.camera = cam_obj
cam.type = 'PANO'
cam.cycles.panorama_type = 'EQUIANGULAR_CUBEMAP_FACE'

# render loop
k = 0
for rot in rots:
    cam_obj.rotation_euler = tuple(math.radians(r) for r in rot)
    bpy.context.scene.render.filepath = os.path.join(out_path, str(k) + '.hdr')
    bpy.ops.render.render(write_still=True)
    k += 1