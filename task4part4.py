# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 15:20:06 2022

@author: sohum
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist
def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar



cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read() 
    
 

    # Display the resulting frame
    
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    dimensions=img.shape
    print(dimensions)
    roi=cv2.rectangle(img,(220,200),(420,280),(0,255,0),3)
    frame=cv2.cvtColor(cv2.rectangle(img,(220,200),(420,280),(0,255,0),3),cv2.COLOR_RGB2BGR)
    cv2.imshow("image",img)
    roi=img[203:277,223:417,:]
    cv2.imshow("roi",roi)
    roi = roi.reshape((roi.shape[0] * roi.shape[1],3)) #represent as row*column,channel number
    clt = KMeans(n_clusters=3) #cluster number
    clt.fit(roi)
    
    hist = find_histogram(clt)
    bar = plot_colors2(hist, clt.cluster_centers_)
    
    bar=cv2.cvtColor(bar,cv2.COLOR_RGB2BGR)
    plt.axis("off")
    cv2.imshow("histogram",bar)
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
