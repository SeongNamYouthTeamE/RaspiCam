# heatmap test using openCV
import numpy as np
import cv2

videoname = 'vtest.avi'

cap = cv2.VideoCapture(videoname)

_, f = cap.read()
cv2.imwrite('frame1.jpg', f)
f = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
f = cv2.GaussianBlur(f, (11, 11), 2, 2)
res = 0.05 * f
res = res.astype(np.float64)
fgbg = cv2.createBackgroundSubtractorMOG2(history=1, varThreshold=100,
                                          detectShadows=True)
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (13, 13))
while True:
    ret, image_np = cap.read()
    # heatmap
    fgmask = fgbg.apply(image_np, None, 0.01)
    gray = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (11, 11), 2, 2)
    gray = gray.astype(np.float64)
    fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    fgmask = fgmask.astype(np.float64)
    res += (40 * fgmask + gray) * 0.01
    res_show = res / res.max()
    res_show = np.floor(res_show * 255)
    res_show = res_show.astype(np.uint8)
    res_show = cv2.applyColorMap(res_show, cv2.COLORMAP_JET)
    cv2.imwrite('frame2.jpg', res_show)
    cv2.imshow('hitmap', res_show)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        # conn.commit()
        # conn.close()
        break
