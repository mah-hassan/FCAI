from tkinter import *
from tkinter import filedialog
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageTk, ImageFilter
root = Tk()
root.title("image processing project")
root.geometry("1500x750")
fr = Frame(root, width="8", padx=50, pady=10)
fr.grid(row=0, column=0)
fr1 = Frame(root, width="8", padx=50, pady=10)
fr1.grid(row=0, column=1)
labels = Frame(root)
labels.grid(row=0, column=2)
Transformations = LabelFrame(
    fr1, text='Transformations', width='10', padx=50, pady=10)
Transformations.grid(row=0, column=0)
fillters = LabelFrame(fr1, text='Fillters', width='10', padx=50, pady=10)
fillters.grid(row=1, column=0)
Threshold = LabelFrame(fr1, text='Threshold', width='10', padx=50, pady=10)
Threshold.grid(row=2, column=0)
ArthLog = LabelFrame(fr, text='ArithmeticAndLogicOperations',
                     width='10', padx=50, pady=10)
ArthLog.pack(side=BOTTOM)


img_paths = [
    "C:\\Users\\MahmoudHassan\\Desktop\\imageProcessing_Project\\images\\noImage.jpg", ""]

  
def browse_image():
    global img
    img_paths[0] = filedialog.askopenfilename()
    img = Image.open(img_paths[0])
    img = ImageTk.PhotoImage(img)
    lb['image'] = img


Browse_bt = Button(fr, command=browse_image, bg="#333333", fg="white", padx=10, pady=8, width="20",
                   text="browse")
Browse_bt.pack()


# def save_image():
#     saved_image = cv2.imread(img_paths[0])
#     save_at_path = filedialog.asksaveasfilename(initialdir="C:\\Users\\MahmoudHassan\\Desktop\\imageProcessing_Project\\saved_images",
#                                                 title="Save Image",
#                                                 filetypes=[("PNG Image", "*.png"),
#                                                            ("JPEG Image",
#                                                             "*.jpg"), ("GIF Image", "*.gif"),
#                                                            ("TIFF Image", "*.tiff"), ("BMP Image", "*.bmp")])
#     cv2.imwrite(save_at_path, saved_image)


# save_bt = Button(fr, command=save_image, bg="#333333",
#                  fg="white", padx=10, pady=8, width="20", text="Save")
# save_bt.pack()
# convert image to gray scale


def gray_image():
    imageGray = cv2.imread(img_paths[0], 0)
    cv2.imshow("gray scale", imageGray)
    return imageGray


gray_image_bt = Button(fr, command=gray_image, bg="#333333", fg="white", padx=10, pady=8, width="20",
                       text="gray")
gray_image_bt.pack()

# convert image to RGB


def RGB_image():
    orgin_img = cv2.imread(img_paths[0], 1)
    RGB_img = cv2.cvtColor(orgin_img, cv2.COLOR_BGR2RGB)
    cv2.imshow('RGB Image', RGB_img)


RGB_bt = Button(fr, command=RGB_image, bg="#333333", fg="white", padx=10, pady=8, width="20",
                text="RGB")
RGB_bt.pack()

# convert image to Binary


def ThresholdBinary():
    orgin_img = cv2.imread(img_paths[0], 0)
    ret, binar_img = cv2.threshold(orgin_img, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow('Binary Image', binar_img)


binary_bt = Button(Threshold, command=ThresholdBinary, bg="#333333", fg="white", padx=10, pady=8, width="20",
                   text="Binary")
binary_bt.pack()


def ThresholdBinaryInv():
    img = cv2.imread(img_paths[0], 0)
    ret, thresh2 = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
    cv2.imshow('THRESH_BINARY_INV', thresh2)


binaryinv_bt = Button(Threshold, command=ThresholdBinaryInv, bg="#333333", fg="white", padx=10, pady=8, width="20",
                      text="BinaryINV")
binaryinv_bt.pack()


def ThresholdTrunc():
    img = cv2.imread(img_paths[0], 0)
    ret, thresh3 = cv2.threshold(img, 120, 255, cv2.THRESH_TRUNC)
    cv2.imshow('THRESH_TRUNC', thresh3)


trunc_bt = Button(Threshold, command=ThresholdTrunc, bg="#333333", fg="white", padx=10, pady=8, width="20",
                  text="Trunc")
trunc_bt.pack()


def ThresholdZeros():
    img = cv2.imread(img_paths[0], 0)
    ret, thresh4 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
    cv2.imshow('THRESH_TOZERO', thresh4)


zeros_bt = Button(Threshold, command=ThresholdZeros, bg="#333333", fg="white", padx=10, pady=8, width="20",
                  text="Zeros")
zeros_bt.pack()


def ThresholdZerosInv():
    img = cv2.imread(img_paths[0], 0)
    ret, thresh5 = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO_INV)
    cv2.imshow('THRESH_TOZERO_INV', thresh5)


zerosinv_bt = Button(Threshold, command=ThresholdZerosInv, bg="#333333", fg="white", padx=10, pady=8, width="20",
                     text="ZerosINV")
zerosinv_bt.pack()


# Transformations

# (1)Negative Transformation


def NegativeTransformation():
    NegativeImg = cv2.imread(img_paths[0], 0)
    h, w = np.shape(NegativeImg)
    for row in range(h):
        for col in range(w):
            NegativeImg[row][col] = 255 - NegativeImg[row][col]
    cv2.imshow("NegativeImage", NegativeImg)
    return NegativeImg


Negative_bt = Button(Transformations, command=NegativeTransformation, bg="#333333", fg="white", padx=10, pady=8, width="20",
                     text="Negative")
Negative_bt.pack()

# (2)Log Transformation


def LogTransformation():
    LogImg = cv2.imread(img_paths[0], 0)
    h, w = np.shape(LogImg)
    for row in range(h): 
        for col in range(w):
            LogImg[row][col] = int(30*(np.log2(1+LogImg[row][col])))
    cv2.imshow("LogTransform", LogImg)
    return LogImg


Log_bt = Button(Transformations, command=LogTransformation, bg="#333333", fg="white", padx=10, pady=8, width="20",
                text="Log")
Log_bt.pack()

# (3)Power_Law Transformation


def PowerLawTransformation():
    PowLawImg = cv2.imread(img_paths[0], 0)
    h, w = np.shape(PowLawImg)
    for row in range(h):
        for col in range(w):
            PowLawImg[row][col] = 255*(PowLawImg[row][col]/255)**8
    cv2.imshow("PowLawTransform", PowLawImg)
    return PowLawImg


PowLaw_bt = Button(Transformations, command=PowerLawTransformation, bg="#333333", fg="white", padx=10, pady=8, width="20",
                   text="Power Law")
PowLaw_bt.pack()

# Contrast Stretching


def ContrastStretching():
    ConStrImg = cv2.imread(img_paths[0], 0)
    a = np.min(ConStrImg)
    b = np.max(ConStrImg)
    R = b-a
    h, w = np.shape(ConStrImg)
    for row in range(h):
        for col in range(w):
            ConStrImg[row][col] = 255*(ConStrImg[row][col]-a)/R
            ConStrImg[row][col] = np.rint(ConStrImg[row][col])
    cv2.imshow("Contrast Stretching", ConStrImg)
    return ConStrImg


ConStr_bt = Button(fr, command=ContrastStretching, bg="#333333", fg="white", padx=10, pady=8, width="20",
                   text="Contrast Stretching")
ConStr_bt.pack()

# Intensity Slicing


def IntensitySlicing():
    img1 = cv2.imread(img_paths[0], 0)
    h, w = np.shape(img1)
    sliceImg = np.zeros((h, w), dtype='uint8')
    min_range = 10
    max_range = 60
    for row in range(h):
        for col in range(w):
            if img1[row][col] > min_range and img1[row][col] < max_range:
                sliceImg[row][col] = 255
            else:
                sliceImg[row][col] = 0  
    sliceImg = sliceImg/255
    cv2.imshow("Intensity Slicing", sliceImg)
    return sliceImg


IntensitySlicing_bt = Button(
    fr, command=IntensitySlicing, text="Intensity Slicing", bg="#333333", fg="white", padx=10, pady=8, width="20")
IntensitySlicing_bt.pack()

# Histogram


def HistogramCalc():
    histimg = cv2.imread(img_paths[0], 0)
    histogram, bin_edges = np.histogram(histimg, bins=256, range=(0, 255))
    plt.plot(histogram)
    plt.show()


histogram_bt = Button(fr, text="Histogram Calculation", command=HistogramCalc,
                      bg="#333333", fg="white", padx=10, pady=8, width="20")
histogram_bt.pack()


def HistogramEqual():
    histEqImg = cv2.imread(img_paths[0], 0)
    histEqImg = cv2.equalizeHist(histEqImg)
    cv2.imshow('image after histogram equalization', histEqImg)
    histogram, bin_edges = np.histogram(histEqImg, bins=256, range=(0, 255))
    plt.plot(histogram)
    plt.show()


histogramEq_bt = Button(fr, text="Histogram Equalization", bg="#333333",
                        fg="white", padx=10, pady=8, width="20", command=HistogramEqual)
histogramEq_bt.pack()

# Spatial Filtaring
# (1)Mean fillter(average)
# [1,1,1]
# [1,1,1]
# [1,1,1]


def meanFillter():
    before_img = cv2.imread(img_paths[0])
    blurImg = cv2.blur(before_img, (5, 5))
    cv2.imshow('mean fillter (average) ', blurImg)


meanFillter_bt = Button(fillters, command=meanFillter, text="MeanFillter",
                        bg="#333333", fg="white", padx=10, pady=8, width="20")
meanFillter_bt.pack()

# (2)Gaussian fillter
# [1,2,1]
# [2,4,2]
# [1,2,1]
def GaussianFillter():
    before_img = cv2.imread(img_paths[0])
    gaussianImg = cv2.GaussianBlur(before_img, (5, 5), 20)
    cv2.imshow('Gaussian fillter', gaussianImg)


GaussianFillter_bt = Button(fillters, command=GaussianFillter,
                            text="GaussianFillter", bg="#333333", fg="white", padx=10, pady=8, width="20")
GaussianFillter_bt.pack()

# Median Fillter

    
def MedianFillter():
    noisyImg = cv2.imread(img_paths[0])
    mediamFillterImg = cv2.medianBlur(noisyImg, 5)
    cv2.imshow('After Median Fillter', mediamFillterImg)


MedianFillter_bt = Button(fillters, command=MedianFillter,
                          text="MedianFillter", bg="#333333", fg="white", padx=10, pady=8, width="20")
MedianFillter_bt.pack()

# Min Fillter


def MinFillter():
    noisyImg = Image.open(img_paths[0])
    Min_ = noisyImg.filter(ImageFilter.MinFilter(size=3))
    Min_.show()
    # remove solt dots


MinFillter_bt = Button(fillters, command=MinFillter, text="MinFillter",
                       bg="#333333", fg="white", padx=10, pady=8, width="20")
MinFillter_bt.pack()

# Max Fillter


def MaxFillter():
    noisyImg = Image.open(img_paths[0])
    Max_ = noisyImg.filter(ImageFilter.MaxFilter(size=3))
    Max_.show()
    # remove peper dots


MaxFillter_bt = Button(fillters, command=MaxFillter, text="MaxFillter",
                       bg="#333333", fg="white", padx=10, pady=8, width="20")
MaxFillter_bt.pack()

# Addition of Image


def Addition():
    firstImg = cv2.imread(img_paths[0])
    img_paths[1] = filedialog.askopenfilename()
    secondImg = cv2.imread(img_paths[1])
    firstImg = cv2.resize(firstImg, (500, 400))
    secondImg = cv2.resize(secondImg, (500, 400))
    weightedSum = cv2.addWeighted(firstImg, 0.5, secondImg, 0.4, 0)
    cv2.imshow('Addition', weightedSum)


Addition_bt = Button(ArthLog, command=Addition, text="Addition",
                     bg="#333333", fg="white", padx=10, pady=8, width="20")
Addition_bt.pack()
# Subtraction of Image


def Subtraction():
    firstImg = cv2.imread(img_paths[0])
    img_paths[1] = filedialog.askopenfilename()
    secondImg = cv2.imread(img_paths[1])
    firstImg = cv2.resize(firstImg, (500, 400))
    secondImg = cv2.resize(secondImg, (500, 400))
    weightedSum = cv2.subtract(firstImg, secondImg)
    cv2.imshow('Addition', weightedSum)


Subtraction_bt = Button(ArthLog, command=Subtraction, text="Subtraction",
                        bg="#333333", fg="white", padx=10, pady=8, width="20")
Subtraction_bt.pack()

# Logic Operation

# AND


def And():
    firstImg = cv2.imread(img_paths[0])
    img_paths[1] = filedialog.askopenfilename()
    secondImg = cv2.imread(img_paths[1])
    cv2.imshow('second image', secondImg)
    dest_and = cv2.bitwise_and(firstImg, secondImg, mask=None)
    cv2.imshow('img1 AND img2', dest_and)


and_bt = Button(ArthLog, command=And, text="AND",
                bg="#333333", fg="white", padx=10, pady=8, width="20")
and_bt.pack()
# OR


def OR():
    firstImg = cv2.imread(img_paths[0])
    img_paths[1] = filedialog.askopenfilename()
    secondImg = cv2.imread(img_paths[1])
    cv2.imshow('second image', secondImg)
    dest_or = cv2.bitwise_or(firstImg, secondImg, mask=None)
    cv2.imshow('img1 OR img2', dest_or)


or_bt = Button(ArthLog, command=OR, text="OR",
               bg="#333333", fg="white", padx=10, pady=8, width="20")
or_bt.pack()

# XOR


def XOR():
    firstImg = cv2.imread(img_paths[0])
    img_paths[1] = filedialog.askopenfilename()
    secondImg = cv2.imread(img_paths[1])
    cv2.imshow('second image', secondImg)
    dest_xor = cv2.bitwise_or(firstImg, secondImg, mask=None)
    cv2.imshow('img1 OR img2', dest_xor)


xor_bt = Button(ArthLog, command=XOR, text="XOR",
                bg="#333333", fg="white", padx=10, pady=8, width="20")
xor_bt.pack()
# Not


def NOT():
    orign = cv2.imread(img_paths[0])
    dest_not = cv2.bitwise_not(orign, mask=None)
    cv2.imshow('NOT', dest_not)


not_bt = Button(ArthLog, command=NOT, text="NOT",
                bg="#333333", fg="white", padx=10, pady=8, width="20")
not_bt.pack()
no_image = Image.open(img_paths[0])
no_image = no_image.resize((600, 400))
no_image = ImageTk.PhotoImage(no_image)
lb = Label(labels, bg="white", image=no_image)
lb.grid(row=0, column=0)
root.mainloop()
