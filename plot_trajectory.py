from matplotlib import pyplot as plt
import json
from XMLParser import XMLParser
import parseTrackletXML as xmlParser
import numpy as np

xxx = xmlParser.parseXML('H:\\trajectoryprediction\\Dataset\\trka5_kitti_data_set\\2011_09_26_drive_0005_tracklets'
                         '\\2011_09_26\\2011_09_26_drive_0005_sync\\tracklet_labels.xml')



K = np.array([(721.5377, 0, 609.5593),
              (0, 721.5377, 172.8540),
              (0, 0, 1.0000)])

veloToCam = np.array([(0.0002, -0.9999, -0.0106, 0.0594),
                      (0.0104, 0.0106, -0.9999, -0.0751),
                      (0.9999, 0.0001, 0.0105, -0.2721),
                      (0, 0, 0, 1.0000)])

# % project in image
loxations = parsed[0]['Van0']

dt = np.dtype('float')
pts_3D = np.array(loxations, dtype=dt)
numberframes = len(pts_3D)
one1 = np.ones((numberframes, 1))
pts_3D = np.append(pts_3D, one1, 1)
pts_3D = np.transpose(pts_3D)
pts_3 = veloToCam.dot(pts_3D)

pts_2D = K.dot(pts_3[0:3, :])

# scale projected points
pts_2D[0, :] = pts_2D[0, :] / pts_2D[2, :]
pts_2D[1, :] = pts_2D[1, :] / pts_2D[2, :]
# pts_2D[2, :] = []

plt.imshow(img)
plt.plot(pts_2D[0, 60], pts_2D[1, 60], c='blue', marker='o', markersize=2)
# plt.plot(pts_2D[0, 19:59],  pts_2D[1, 19:59], c='green', marker='o', markersize=3)
# plt.plot(pred_index[:, 0], pred_index[:, 1], c='red', linewidth=1, marker='o', markersize=3)
# # plt.plot(past[:, 0] * 2 + 180, past[:, 1] * 2 + 180, c='blue')
# # plt.plot(future[:, 0] * 2 + 180, future[:, 1] * 2 + 180, c='green')
plt.show()
plt.close()
