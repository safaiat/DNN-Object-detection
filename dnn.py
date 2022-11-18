import cv2
import glob

i=1 
path = glob.glob("test_images/*.jpg")
for file in path:
    i=i+1
    img = cv2.imread(file)
    # cv2.imshow("image",img)
    # cv2.waitKey(1000)
    filename =( 'outpot_images/savedImage' + str(i) + '.jpg')
    cv2.imwrite(filename, img)
    
cv2.destroyAllWindows()


