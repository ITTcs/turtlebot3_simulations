from xml.dom import minidom
import xml.etree.ElementTree as ET

dAperture = .99
yWallSize = 0.01
zWallSize = 0.4
envMaxSize = 5.01
sectioSize = 2.99
num_walls = 12

envMaterial = 'Wood'
sdf = ET.Element('sdf',attrib={'version':'1.6'})
model = ET.SubElement(sdf, 'model', attrib={'name':'circuit_left_right_turns'})
ET.SubElement(model, 'pose', attrib={'frame':''}).text = '0 0 0 0 -0 0'

yWallHalfSize = yWallSize/2
zWallHalfSize = zWallSize/2
inEnvSize = envMaxSize - (2 * yWallSize)

class Wall:
    xWallSize = None
    xWallPose = None
    yWallPose = None
    yawWallPose = None

walls = [Wall() for _ in range(num_walls)]

walls[0].xWallSize = envMaxSize - yWallSize
walls[0].xWallPose = yWallHalfSize
walls[0].yWallPose = walls[0].xWallSize/2
walls[0].yawWallPose = 1.5708

walls[1].xWallSize = sectioSize + yWallSize
walls[1].xWallPose = walls[1].xWallSize/2
walls[1].yWallPose = walls[0].xWallSize + yWallHalfSize
walls[1].yawWallPose = 0

walls[2].xWallSize = inEnvSize - walls[1].xWallSize + yWallSize
walls[2].xWallPose = walls[0].xWallPose + walls[1].xWallSize
walls[2].yWallPose = walls[1].yWallPose - (walls[2].xWallSize/2) + yWallHalfSize
walls[2].yawWallPose = 1.5708

walls[3].xWallSize = walls[2].xWallSize
walls[3].xWallPose = walls[2].yWallPose - yWallSize
walls[3].yWallPose = walls[2].xWallPose 
walls[3].yawWallPose = 0

walls[4].xWallSize = walls[1].xWallSize
walls[4].xWallPose = walls[1].yWallPose
walls[4].yWallPose = walls[1].xWallPose + yWallSize
walls[4].yawWallPose = 1.5708

walls[5].xWallSize = walls[0].xWallSize
walls[5].xWallPose = walls[0].yWallPose + yWallSize
walls[5].yWallPose = walls[0].xWallPose
walls[5].yawWallPose = 0

walls[6].xWallSize = inEnvSize - (2*dAperture + yWallSize)
walls[6].xWallPose = yWallSize + dAperture + yWallHalfSize
walls[6].yWallPose = walls[0].yWallPose
walls[6].yawWallPose = 1.5708

walls[7].xWallSize = walls[1].xWallSize - (2*yWallSize) - (2*dAperture)
walls[7].xWallPose = walls[1].xWallPose
walls[7].yWallPose = walls[6].yWallPose + (walls[6].xWallSize/2) + yWallHalfSize
walls[7].yawWallPose = 0

walls[8].xWallSize = walls[2].xWallSize
walls[8].xWallPose = walls[6].xWallPose + walls[7].xWallSize
walls[8].yWallPose = walls[7].yWallPose - (walls[8].xWallSize/2) + yWallHalfSize
walls[8].yawWallPose = 1.5708

walls[9].xWallSize = walls[8].xWallSize
walls[9].xWallPose = walls[8].yWallPose - yWallSize
walls[9].yWallPose = walls[8].xWallPose 
walls[9].yawWallPose = 0

walls[10].xWallSize = walls[7].xWallSize
walls[10].xWallPose = walls[7].yWallPose
walls[10].yWallPose = walls[4].yWallPose
walls[10].yawWallPose = 1.5708

walls[11].xWallSize = walls[6].xWallSize
walls[11].xWallPose = walls[5].xWallPose
walls[11].yWallPose = walls[6].xWallPose
walls[11].yawWallPose = 0

for i in range(num_walls):

    link = ET.SubElement(model, 'link', attrib={'name':'Wall_' + str(i)})

    collision = ET.SubElement(link, 'collision', attrib={'name':'Wall_' + str(i) + '_Collision'})

    ET.SubElement(ET.SubElement(ET.SubElement(collision, 'geometry'), 'box'), 'size').text = \
        str(walls[i].xWallSize) + ' ' + str(yWallSize) + ' ' + str(zWallSize)

    ET.SubElement(collision, 'pose', attrib={'frame':''}).text = \
        '0 0 ' + str(zWallHalfSize) + ' 0 -0 0'

    visual = ET.SubElement(link, 'visual', attrib={'name':'Wall_' + str(i) + '_Visual'})

    ET.SubElement(visual, 'pose', attrib={'frame':''}).text = \
        '0 0 ' + str(zWallHalfSize) + ' 0 -0 0'

    ET.SubElement(ET.SubElement(ET.SubElement(visual, 'geometry'), 'box'), 'size').text = \
        str(walls[i].xWallSize) + ' ' + str(yWallSize) + ' ' + str(zWallSize)

    material = ET.SubElement(visual, 'material')

    script = ET.SubElement(material, 'script')

    ET.SubElement(script, 'uri').text = 'file://media/materials/scripts/gazebo.material'
    ET.SubElement(script, 'name').text = 'Gazebo/' + envMaterial

    ET.SubElement(material, 'ambient').text = '1 1 1 1'

    ET.SubElement(link, 'pose', attrib={'frame':''}).text = \
        str(walls[i].xWallPose) + ' ' + str(walls[i].yWallPose) + ' 0 0 -0 ' + str(walls[i].yawWallPose)


ET.SubElement(model, 'static').text = '1'

tree = minidom.parseString(ET.tostring(sdf)).toprettyxml(indent="  ")
with open('model.sdf', "w") as fh:
    fh.write(tree)