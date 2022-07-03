import numpy as np
import cv2

img = cv2.imread('this_is_a_cell.jpg')
# This is a confocal microscopy image of a Chinese hamster ovary cell. The pixel intensity values are integrated throughout the z-stack axis.
# The cell nucleus is stained in blue and the cytoplasm is in red.

cv2.imshow('image', img)
cv2.waitKey(2000)

img_1,img_2,img_3,img_4,img_5,img_6,img_7,img_8,img_9,img_10,img_11,img_12,\
    img_13,img_14,img_15,img_16,img_17,img_18,img_19,img_20,img_21,img_22,img_23,img_24,\
    img_25,img_26,img_27,img_28,img_29,img_30,img_31,img_32,img_33,img_34,img_35,img_36,\
    img_37,img_38,img_39,img_40,img_41,img_42,img_43,img_44,img_45,img_46,img_47,img_48\
    = np.hsplit(img, 48)


image_1_1 = cv2.hconcat(
    [img_1,img_3,img_5,img_7,img_9,img_11,img_13,img_15,img_17,img_19,img_21,img_23,
     img_25,img_27,img_29,img_31,img_33,img_35,img_37,img_39,img_41,img_43,img_45,img_47])

#print(image_1.shape)


image_1_2 = cv2.hconcat(
    [img_2,img_4,img_6,img_8,img_10,img_12,img_14,img_16,img_18,img_20,img_22,img_24,
     img_26,img_28,img_30,img_32,img_34,img_36,img_38,img_40,img_42,img_44,img_46,img_48])


image_tmp = cv2.hconcat([image_1_1, image_1_2])

cv2.imshow('image', image_tmp)
cv2.waitKey(2000)


img_1,img_2,img_3,img_4,img_5,img_6,img_7,img_8,img_9,img_10,img_11,img_12,\
    img_13,img_14,img_15,img_16,img_17,img_18,img_19,img_20,img_21,img_22,img_23,img_24,\
    img_25,img_26,img_27,img_28,img_29,img_30,img_31,img_32,img_33,img_34,img_35,img_36,\
    img_37,img_38,img_39,img_40,img_41,img_42,img_43,img_44,img_45,img_46,img_47,img_48\
    = np.vsplit(image_tmp, 48)

# the next lines 42-187 are for the temporal visualisation of the split steps.
# it's fine for a follow-up, but it is not necessary to include.

cv2.imshow('image', img_1)
cv2.waitKey(300)

cv2.imshow('image', img_2)
cv2.waitKey(300)

cv2.imshow('image', img_3)
cv2.waitKey(300)

cv2.imshow('image', img_4)
cv2.waitKey(300)

cv2.imshow('image', img_5)
cv2.waitKey(300)

cv2.imshow('image', img_6)
cv2.waitKey(300)

cv2.imshow('image', img_7)
cv2.waitKey(300)

cv2.imshow('image', img_8)
cv2.waitKey(300)

cv2.imshow('image', img_9)
cv2.waitKey(300)

cv2.imshow('image', img_10)
cv2.waitKey(300)

cv2.imshow('image', img_11)
cv2.waitKey(300)

cv2.imshow('image', img_12)
cv2.waitKey(300)

cv2.imshow('image', img_13)
cv2.waitKey(300)

cv2.imshow('image', img_14)
cv2.waitKey(300)

cv2.imshow('image', img_15)
cv2.waitKey(300)

cv2.imshow('image', img_16)
cv2.waitKey(300)

cv2.imshow('image', img_17)
cv2.waitKey(300)

cv2.imshow('image', img_18)
cv2.waitKey(300)

cv2.imshow('image', img_19)
cv2.waitKey(300)

cv2.imshow('image', img_20)
cv2.waitKey(300)

cv2.imshow('image', img_21)
cv2.waitKey(300)

cv2.imshow('image', img_22)
cv2.waitKey(300)

cv2.imshow('image', img_23)
cv2.waitKey(300)

cv2.imshow('image', img_24)
cv2.waitKey(300)

cv2.imshow('image', img_25)
cv2.waitKey(300)

cv2.imshow('image', img_26)
cv2.waitKey(300)

cv2.imshow('image', img_27)
cv2.waitKey(300)

cv2.imshow('image', img_28)
cv2.waitKey(300)

cv2.imshow('image', img_29)
cv2.waitKey(300)

cv2.imshow('image', img_30)
cv2.waitKey(300)

cv2.imshow('image', img_31)
cv2.waitKey(300)

cv2.imshow('image', img_32)
cv2.waitKey(300)

cv2.imshow('image', img_33)
cv2.waitKey(300)

cv2.imshow('image', img_34)
cv2.waitKey(300)

cv2.imshow('image', img_35)
cv2.waitKey(300)

cv2.imshow('image', img_36)
cv2.waitKey(300)

cv2.imshow('image', img_37)
cv2.waitKey(300)

cv2.imshow('image', img_38)
cv2.waitKey(300)

cv2.imshow('image', img_39)
cv2.waitKey(300)

cv2.imshow('image', img_40)
cv2.waitKey(300)

cv2.imshow('image', img_41)
cv2.waitKey(300)

cv2.imshow('image', img_42)
cv2.waitKey(300)

cv2.imshow('image', img_43)
cv2.waitKey(300)

cv2.imshow('image', img_44)
cv2.waitKey(300)

cv2.imshow('image', img_45)
cv2.waitKey(300)

cv2.imshow('image', img_46)
cv2.waitKey(300)

cv2.imshow('image', img_47)
cv2.waitKey(300)

cv2.imshow('image', img_48)
cv2.waitKey(300)

image_2_1 = cv2.vconcat(
    [img_1,img_3,img_5,img_7,img_9,img_11,img_13,img_15,img_17,img_19,img_21,img_23,
     img_25,img_27,img_29,img_31,img_33,img_35,img_37,img_39,img_41,img_43,img_45,img_47])

image_2_2 = cv2.vconcat(
    [img_2,img_4,img_6,img_8,img_10,img_12,img_14,img_16,img_18,img_20,img_22,img_24,
     img_26,img_28,img_30,img_32,img_34,img_36,img_38,img_40,img_42,img_44,img_46,img_48])

image_final = cv2.vconcat([image_2_1, image_2_2])

#print(image_final.shape)
cv2.imshow('image', image_final)
cv2.imwrite('image_final.jpg', image_final)

cv2.imshow('this_is_a_cell.jpg', img)

cv2.waitKey(0)

