
# Tab length compensation a negative number will increase the gap between the tabs
# a fudge factor that increases the gap along the finger joint when
# negative - it should be 1/4 of the gap you want

fudge = -0.2 //0.1 #for (perspex)

thickness = 12

# Internal dimensions of box
box_width = 350
box_height = 120-(2*thickness)
box_depth = 210



cutter='1/8_endmill'
cutterrad=milling.tools[cutter]['diameter']/2



tab_length = 25
material = 'plywood'

centre = V(0,0)
module = camcam.add_plane(Plane('plane', cutter=cutter))

module.add_layer(
    'back',
     material=material,
     thickness=thickness,
     z0=0,
     zoffset=-thickness-box_depth)

module.add_layer(
    'bottom',
     material=material,
     thickness=thickness,
     z0=0,
     zoffset=-thickness-box_depth)

module.add_layer(
    'side',
     material=material,
     thickness=thickness,
     z0=0,
     zoffset=-thickness-box_depth)

bottom_border = FingerJointBoxSide(
    centre,
     box_width,
     box_height,
     'in',
     corners={'left': 'off',
              'top': 'off',
              'right': 'off',
              'bottom': 'off'},
     sidemodes={},
     tab_length=tab_length,
     thickness=thickness,
     cutter=cutter,
     centred=True,
     fudge=fudge)

bottom = module.add_path(
    Part(name='bottom',
         border=bottom_border,
         layer='bottom'))
bottom.number = 1


bottom.add(RoundedRect(centre, centred=True, width=box_width*0.7, height=box_height*0.7, side='in', rad=10), 'bottom')


back_border = FingerJointBoxSide(
    centre,
    box_width,
    box_depth,
    'in',
    corners={'left': 'off', 'top': 'on', 'right': 'off', 'bottom': 'on'}, sidemodes={'top': 'straight'},
    tab_length=tab_length,
    thickness={'left': thickness, 'right': thickness, 'bottom': thickness, 'top': thickness},
    cutter=cutter,
    centred=True,
    fudge=fudge)


back = module.add_path(Part(name='back',
                            border=back_border,
                            layer='back'),
                       layers='back')
back.number = 2

side_border = FingerJointBoxSide(
    centre,
    box_height,
    box_depth,
    'in',
    corners={'left': 'on', 'top': 'on', 'right': 'on', 'bottom': 'on'},
    sidemodes={'top': 'straight'},
    tab_length=tab_length,
    thickness={'left': thickness, 'right': thickness, 'bottom': thickness, 'top': thickness},
    cutter=cutter,
    centred=True,
    fudge=fudge)


side = module.add_path(Part(name='side',
                            border=side_border,
                            layer='side'),
                       layers='side')
side.number = 2
