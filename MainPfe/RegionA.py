import cv2
from matplotlib.pyplot import imshow, rc
import numpy as np
import math
import glob
from numpy.core.fromnumeric import shape
import pandas as pd
import re
from pyds import MassFunction
import Membership
from sys import argv


def mask_area(mask):
    image = mask
    # if(image.shape[0] > 500 or image.shape[1] > 500 ):
    #     image = cv2.resize(image, None, fx = 0.3, fy=0.22)
    # cv2.imshow('Original mask', image)
    # cv2.moveWindow('Original mask', 0,0);
    ret, img = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, contours,  -1, (255,255,255), 1)
    # cv2.imshow('One contour', img)
    # cv2.moveWindow('One contour', 500,0);
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(img, [Largest_contour(contours)],  0, (255,255,255), thickness=cv2.FILLED)
    
    # x,y,w,h = cv2.boundingRect(Largest_contour(contours))
    # cv2.rectangle(img, (x, y), (w+x, h+y), (255,0,0), thickness=cv2.FILLED)

    #cv2.imshow('full contour', small_image(img))
    #cv2.moveWindow('full contour', 900,0)
    #cv2.waitKey()
    

    return img

def interrest(image):
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)[1]

    # Find contour and sort by contour area
    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    # Find bounding box and extract ROI
    for c in cnts:
        x,y,w,h = cv2.boundingRect(c)
        ROI = image[y:y+h, x:x+w]
        break
    return ROI
    
def Largest_contour(contours):
    largest_areas = sorted(contours, key=cv2.contourArea)
    big_contour = largest_areas[-1]
    return big_contour

def small_image(ROI):
    if(ROI.shape[0] > 500 or ROI.shape[1] > 500 ):
        ROI = cv2.resize(ROI, None, fx = 0.3, fy=0.22)
    return ROI
    ##Area with perimetreaa

def Edge_detection(contour, imageSize):
    x,y,w,h = cv2.boundingRect(contour)
    xMin = 0
    yMin = 0
    xMax = imageSize.shape[1] - 1
    yMax = imageSize.shape[0] - 1
    retval = False
    # or h >= yMax
    if( x < xMin or y == yMin or w >= xMax ):
        # print("Border X of contour :", x)
        # print("Border X of image :" , xMin)
        # print(x < xMin)

        # print("Border X of contour :", y)
        # print("Border X of image :" , yMin)
        # print(y == yMin)

        # print("Border X of contour :", w)
        # print("Border X of image :" , xMax)
        # print(w >= xMax)

        # print("----------------------------------------")
        retval = True
    return retval

def keep_object(contour, img):
    mask = np.zeros(img.shape, np.uint8)
    cv2.drawContours(mask, [contour], 0, (255,255,255,255), -1)
    image_result = cv2.bitwise_and(img,img,mask = mask)
    return image_result

def training(images, df, Cancer):
    for (file,image) in images :
        mask = glob.glob(file[:-4] + "_Mask*")
        if  mask == [] or file.find("Mask")>-1:
             continue 

        mask = mask_area(cv2.imread(mask[0], 0))

        type = re.search("(LEFT_MLO|LEFT_CC|RIGHT_MLO|RIGHT_CC)",file).group(1)
        Image = image.copy()
        #cv2.imshow('hi ' + imdir[-5 :-1],small_image(image)); 
        #cv2.waitKey()
        
        #keeping only mask zone
        if(Cancer == True):
            contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
            mask_contour = Largest_contour(contours)
            tumor_zone = keep_object(mask_contour, image)
            cv2.destroyAllWindows()
            # cv2.imshow("tumor_zone",small_image(tumor_zone))
            # cv2.moveWindow('tumor_zone', 0,0)
            #cropping tumor zone 
            crop = interrest(tumor_zone)
            # cv2.imshow("cropped",crop)
            # cv2.moveWindow('cropped', 900,0)
            # cv2.waitKey()
            # cv2.destroyAllWindows()
            ROI = crop

        if(Cancer == False):
            crop = image
            ROI = crop

        image = cv2.GaussianBlur(crop,(7,7),0)

        ## Histogram contrast
        image = cv2.equalizeHist(image)
        # cv2.imshow('Histogram amplification',image)
        

        ret, img = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
        #cv2.imshow('Threshhold ' + imdir[-5 :-1], img)
        #cv2.moveWindow('Threshhold '+ imdir[-5 :-1], 50,0)
        


        contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        # cv2.imshow('Kept contours',ROI)
        # cv2.moveWindow('Kept contours', 500,0)
        # cv2.waitKey()
        # cv2.destroyWindow('Kept contours')
        try:
            #if contour is too small eliminate it
            contour = Largest_contour(contours)
        except:
            cv2.destroyAllWindows()
            continue
        out = keep_object(contour,img)
        #cv2.imshow('Largest contour',out)
        #cv2.moveWindow('Largest contour', 500,0)
        
        cnt = Largest_contour(contours)
        cv2.drawContours(ROI, cnt, -1, (0, 0, 255), 3)


        ##Area with perimetre
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt,True)
        Cmp2 = 1 - (math.pi * 4 * area)/(peri * peri)
        Cr = 4*(math.pi * area)/(peri * peri)


        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        ROI = cv2.cvtColor(ROI, cv2.COLOR_GRAY2BGR)
        (x, y), (width, height), angle = rect 
        ArRM = (width) * (height)
        RC = area / ArRM
        cv2.drawContours(ROI,[box],0,(0,0,255),2)

        ellipse = cv2.fitEllipse(cnt)
        ArEMC = ellipse[1][0]/2 * ellipse[1][1]/2 * math.pi
        Exf = area / ArEMC
        cv2.ellipse(ROI,ellipse,(0,255,0),2)

        (x,y),radius = cv2.minEnclosingCircle(cnt)
        center = (int(x),int(y))
        ArCMC = radius * radius * math.pi
        CMC = area / ArCMC
        cv2.circle(ROI,center,int(radius),(255,0,0),2)
        #cv2.imshow('Result ' + imdir[-4 :-1],ROI)
        #cv2.moveWindow('Result '+ imdir[-4 :-1], 950,0)

        cv2.waitKey()
        cv2.destroyAllWindows()
        
        # Tables part
    return df

def Normal_trainning(images, df):
    for (file,image) in images :
        print("image")
        type = re.search("(LEFT_MLO|LEFT_CC|RIGHT_MLO|RIGHT_CC)",file).group(1)     
        Image = image.copy()
        # cv2.imshow('hi ' + imdir[-5 :-1],image); 
        # cv2.waitKey()
        image = cv2.GaussianBlur(image,(7,7),0)

        #Binarization
        ret, img = cv2.threshold(image, 11, 255, cv2.THRESH_BINARY)
        ## keeping only breast zone on full image
        contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        removed = keep_object(Largest_contour(contours),image)

        ## Cropping the breast area##
        ROI = interrest(removed)
        # cv2.imshow('ROI ' + imdir[-5 :-1],small_image(ROI))


        ## Histogram contrast
        image = cv2.equalizeHist(ROI)
        image = cv2.equalizeHist(image)
        # cv2.imshow('Histogram amplification',small_image(image))
        # cv2.waitKey()
        # cv2.destroyWindow('Histogram amplification')

        ret, img = cv2.threshold(image, 233, 255, cv2.THRESH_BINARY)
        # cv2.imshow('Threshhold ' + imdir[-5 :-1], small_image(img))
        # cv2.moveWindow('Threshhold '+ imdir[-5 :-1], 50,0)


        contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        contour = Largest_contour(contours)
        out = keep_object(contour,img)
        # cv2.imshow('Largest contour',small_image(out))
        # cv2.moveWindow('Largest contour', 500,0)
        cv2.drawContours(ROI, contour, -1, (0, 0, 255), 3)
        cnt = contour

        ##Area with perimetre
        area = cv2.contourArea(cnt)
        peri = cv2.arcLength(cnt,True)
        Cmp2 = 1 - (math.pi * 4 * area)/(peri * peri)
        Cr = 4*(math.pi * area)/(peri * peri)


        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        ROI = cv2.cvtColor(ROI, cv2.COLOR_GRAY2BGR)
        (x, y), (width, height), angle = rect 
        ArRM = (width) * (height)
        RC = area / ArRM
        cv2.drawContours(ROI,[box],0,(0,0,255),2)

        ellipse = cv2.fitEllipse(cnt)
        ArEMC = ellipse[1][0]/2 * ellipse[1][1]/2 * math.pi
        Exf = area / ArEMC
        cv2.ellipse(ROI,ellipse,(0,255,0),2)

        (x,y),radius = cv2.minEnclosingCircle(cnt)
        center = (int(x),int(y))
        ArCMC = radius * radius * math.pi
        CMC = area / ArCMC
        cv2.circle(ROI,center,int(radius),(255,0,0),2)
        # cv2.imshow('Result ' + imdir[-4 :-1],small_image(ROI))
        # cv2.moveWindow('Result '+ imdir[-4 :-1], 950,0)

        cv2.waitKey()
        cv2.destroyAllWindows()
        
        # Tables part

    return df


def execution(image, type, regle, decision ):
    """
    regle : 0 conjonctive, 1 disjonctive, 2 hybride, 3 pcr, 4 yager.
    decision : 0 bel , 1 pl, 2 pig
    """
    b = 0
    tumeur = None

    ROI = image.copy()

    image = cv2.equalizeHist(image)


    ret, img = cv2.threshold(image, 227, 255, cv2.THRESH_BINARY )
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

       
    mask = np.ones(image.shape[:2], dtype="uint8") * 255

    #Exception is thrown when no contour is found
    try:
        contour = Largest_contour(contours)
    except:
        return 0
        

    ROI = cv2.cvtColor(ROI, cv2.COLOR_GRAY2BGR) 
    maxcombined=0
    combined = 0 
    decisionMax= 0
    contours = sorted(contours , key= cv2.contourArea, reverse=True)
    for cnt in contours:
        ##Area with perimetre
        if(cv2.contourArea(cnt) > 10000 ):
            area = cv2.contourArea(cnt)
            peri = cv2.arcLength(cnt,True)
            Cmp2 = 1 - (math.pi * 4 * area)/(peri * peri)
            Cr = 4*(math.pi * area)/(peri * peri)

            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            (x, y), (width, height), angle = rect 
            ArRM = (width) * (height)
            RC = area / ArRM
                

            ellipse = cv2.fitEllipse(cnt)
            ArEMC = ellipse[1][0]/2 * ellipse[1][1]/2 * math.pi + 0.1
            Exf = area / ArEMC
                

            (x,y),radius = cv2.minEnclosingCircle(cnt)
            center = (int(x),int(y))
            ArCMC = radius * radius * math.pi
            CMC = area / ArCMC 
                
                
            m1 = MassFunction({'M' : Membership.getCr(Cr) , 'B' : 1 - Membership.getCr(Cr)})
            m2 = MassFunction({'M' : Membership.getEx(Exf) , 'B' : 1 - Membership.getEx(Exf)})
            m3= MassFunction({'M' : Membership.getCo(Cmp2) , 'B' : 1 - Membership.getCo(Cmp2)})
            m4 = MassFunction({'M' : Membership.getRc(RC) , 'B' : 1 - Membership.getRc(RC)})
            Fcom = [m1.combine_conjunctive, m1.combine_disjunctive, m1.combine_Hybride, m1.combine_Pcr, m1.combine_Yager]
                
            combined = Fcom[regle]([m2,m3,m4])
            Fdec = [(combined.max_bel, combined.bel), (combined.max_pl, combined.pl), (combined.max_pig, combined.pignistic)]

            if(maxcombined != 0):
                if (combined['M'] > maxcombined['M'] )and Fdec[decision][0]() == {'B'}:
                    maxcombined = combined
                    tumeur = cnt
            else:
                if Fdec[decision][0]() == {'B'}:
                    maxcombined = combined
                    tumeur = cnt


            if Fdec[decision][0]() == {'M'} and ((decision==2 and Fdec[decision][1]()[{'M'}] > decisionMax) or (decision!=2 and Fdec[decision][1]({'M'}) > decisionMax)):
                decisionMax = Fdec[decision][1]({'M'}) if decision!=2 else Fdec[decision][1]()[{'M'}]
                tumeur = cnt
                maxcombined = combined
                # cv2.drawContours(ROI,[box],0,(0,0,255),2)
                cv2.drawContours(ROI, cnt , -1 , (0,0,0), 2)
                # cv2.ellipse(ROI,ellipse,(0,255,0),2)
                # cv2.circle(ROI,center,int(radius),(255,0,0),2)
                    

                #mass = [[Cr,Exf,Cmp2,RC,imdir[-5: -1],type,area]]
                #DF = pd.DataFrame(mass, columns =["Cercularité", "Excentricité", "Compacité", "Rectangularité", "Patient", "Type","Area"])
                #df = df.append(DF, ignore_index=True)
    cv2.imwrite("Temp/"+type + ".jpg", ROI)
           

    return (tumeur, maxcombined)


def Pretreatement(image, type):
    image = cv2.GaussianBlur(image,(21,21),0)
    image = image[125 : image.shape[0] - 150 ,  : ]
    #Binarization
    ret, img = cv2.threshold(image, 11, 255, cv2.THRESH_BINARY)
    
    ## keeping only breast zone on full image
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    removed = keep_object(Largest_contour(contours),image)

    ## Cropping the breast area##
    ROI = interrest(removed)
    ## Histogram contrast
    #ROI = ROI[125: ROI.shape[0] - 150, : ]
    image = cv2.equalizeHist(ROI)
    #cv2.imshow('Histogram amplification',small_image(image))
    #cv2.waitKey()
    # cv2.destroyWindow('Histogram amplification')
    i = 0

    if('MLO' in type):
        i = 15
        ret, img = cv2.threshold(image, 190, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # cv2.imshow('muscle',small_image(img))
        # cv2.waitKey()
        # cv2.destroyWindow('muscle')
        mask = np.ones(image.shape[:2], dtype="uint8") * 255

        for contour in contours:
            if(Edge_detection(contour, img)):
                cv2.drawContours(mask, [contour], -1, 0, -1)

        ROI = cv2.bitwise_and(ROI, ROI, mask=mask)
        image = cv2.equalizeHist(ROI)
        # cv2.imshow('muscle removal' , small_image(image))
        # cv2.moveWindow('muscle removal', 1,0)
        # cv2.waitKey()
        # cv2.destroyWindow('muscle removal')
    cv2.imwrite("Temp/" + type + ".jpg", image)
    return ROI

def combineMLOCC(mlo, cc, age, regle, decision):
    """
    regle : 0 conjonctive, 1 disjonctive, 2 hybride, 3 pcr, 4 yager.
    decision : 0 bel , 1 pl, 2 pig
    """


    Fcom = [mlo.combine_conjunctive, mlo.combine_disjunctive, mlo.combine_Hybride, mlo.combine_Pcr, mlo.combine_Yager]
    Age = MassFunction({'M' : Membership.getAge(age), 'B' : 1 - Membership.getAge(age)})
    combined = Fcom[regle]([cc, Age])
    Fdec = [(combined.max_bel, combined.bel), (combined.max_pl, combined.pl), (combined.max_pig, combined.pignistic)]

    return (Fdec[decision][0]())