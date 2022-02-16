import numpy as np
import time
class ME461Group:
    '''
    This is the random player used in the colab example.
    Edit this file properly to turn it into your submission or generate a similar file that has the same minimal class structure.
    You have to replace the name of the class (ME461Group) with one of the following (exactly as given below) to match your group name
        atlas
        backspacex
        ducati
        hepsi1
        mechrix
        meturoam
        nebula
        ohmygroup
        tulumba
    After you edit this class, save it as groupname.py where groupname again is exactly one of the above
    '''
    def __init__(self, userName, clrDictionary, maxStepSize, maxTime):
        self.name = userName # your object will be given a user name, i.e. your group name
        self.maxStep = maxStepSize # maximum length of the returned path from run()
        self.maxTime = maxTime # run() is supposed to return before maxTime
        self.colorzzz = clrDictionary
        self.colorzzz['ak'] = ((255,255,255),0,0)
        
    def compress(self,imgg):
        reducedd = np.empty((15, 15, 3))
        for i in range(15):
            for j in range(15):
                reduced[i][j] = img[i * 50][j * 50]
        return reducedd

    def konumPuani(self,konum):
        a = self.reduced[tuple(konum)]
        for i in self.colorzzz.values():
            if (a == i[0]).all():
                return i[1]

    def findCenter(self,point): # point p (y,x)
        # send a point in 15x15 grid, and return center point in 750x750
        center = point * 50 + 25
        return center


    def findTargetPoint(self,pos,target): # position in 750x750, target point in 15x15 grid
        target_center = self.findCenter(target)
        posx = pos[1]
        posy = pos[0]
        centerx = target_center[1]
        centery = target_center[0]
    
        if(posx <= centerx + 25 and posx >= centerx - 25 and posy <= centery + 25 and posy >= centery - 25):
            return [pos,]

        if(posx <= centerx + 25 and posx >= centerx-25):
            if(posy <= centery - 25):
                target_pix = np.array([[centery - 25,posx]])
            else:
                target_pix = np.array([[centery + 25,posx]])
        
        elif(posy <= centery + 25 and posy >= centery - 25):
            if(posx <= centerx - 25):
                target_pix = np.array([[posy,centerx - 25]])
            else:
                target_pix = np.array([[posy,centerx + 25]])

        else:
            if(posx > centerx and posy > centery):
                target_pix = np.array([[centery + 25,posx],[centery + 25,centerx + 25]])
            
            elif(posx < centerx and posy > centery):
                target_pix = np.array([[centery + 25,posx],[centery + 25,centerx - 25]])
            
            elif(posx > centerx and posy < centery):
                target_pix = np.array([[centery - 25,posx],[centery - 25,centerx + 25]])
            
            else:
                target_pix = np.array([[centery - 25,posx],[centery - 25,centerx - 25]])    
        
        return target_pix

    def travelLength1(self,pos, target): # both points in 750x750
        return abs(pos[0]-target[0]) + abs(pos[1] - target[1])




    def run(self, img, info):
        myinfo = info[self.name]
        imS = img.shape[0] # assume square image and get size
        # get current location 
        loc, game_point = info[self.name]
        y1,x1 = loc # get current y,x coordinates
        # a very simple randomizer
        maxL = self.maxStep # total travel
        
        self.reduced = self.compress(img)[:,:,0:3]

        pos_dict = {}

        y,x = np.where(np.all(self.reduced==self.colorzzz['clr20'][0],axis=2))
        pos_dict[20] = np.column_stack((y,x))
        y,x = np.where(np.all(self.reduced==self.colorzzz['clr30'][0],axis=2))
        pos_dict[30] = np.column_stack((y,x))
        y,x = np.where(np.all(self.reduced==self.colorzzz['clr50'][0],axis=2))
        pos_dict[50] = np.column_stack((y,x))
        y,x = np.where(np.all(self.reduced==self.colorzzz['clr100'][0],axis=2))
        pos_dict[100] = np.column_stack((y,x))

#         biz = [int(y1/50),int(x1/50)]

#         yenimesafe = float('inf')
#         for i in pos_dict.keys():
#             for j in pos_dict[i]:
#                 mesafe = abs(biz[0]-j[0])+abs(biz[1]-j[1])
#                 if mesafe <= yenimesafe:
#                     hedef = j
#                     yenimesafe = mesafe

#         print('bizim yer',biz,'- hedef',hedef)

#         tumiht = []
#         yollar = []
#         tumiht.append([biz])
#         while tumiht:
#             guzerg = tumiht.pop(0)
#             sonDurak = guzerg[-1]
#             y,x = sonDurak
#             if (sonDurak == hedef).all():
#                 yollar.append(guzerg.copy())
#             if y < hedef[0]:    # hedef altta
#                 guzerg.append([y+1,x])
#                 tumiht.append(guzerg.copy())
#                 guzerg.pop()
#             if y > hedef[0]:    # hedef ustte
#                 guzerg.append([y-1,x])
#                 tumiht.append(guzerg.copy())
#                 guzerg.pop()
#             if x < hedef[1]:    # hedef sagda
#                 guzerg.append([y,x+1])
#                 tumiht.append(guzerg.copy())
#                 guzerg.pop()
#             if x > hedef[1]:    # hedef solda
#                 guzerg.append([y,x-1])
#                 tumiht.append(guzerg.copy())
#                 guzerg.pop()

#         print('tüm yollar',yollar)

#         eskiTop = 0
#         for i in range(len(yollar)):
#             top = 0
#             for j in yollar[i]:
#                 top += self.konumPuani(j)
#             if top > eskiTop:
#                 guzelYol = yollar[i]
#                 guzelYol.pop(0)
#                 eskiTop = top
#         print('en güzel yol', guzelYol)

#         pos = self.findCenter(loc)
#         yolnp = np.array(guzelYol)
#         pos2 = np.copy(pos)
#         way = [np.copy(pos),]

#         total_walk = 0

#         for target in yolnp:
#             pix = self.findTargetPoint(pos2,target)
#             way = np.append(way,pix,axis=0)
#             pos2 = np.copy(pix[-1])


#         for i in range(len(way) - 1):
#             total_walk += self.travelLength1(way[i],way[i+1])
#             print(total_walk)
#             if total_walk > 100:
#                 diff = total_walk - 100
#                 dir = np.not_equal(way[i+1] - way[i],0)
#                 road = np.copy(way[0:i+1])
                
#                 if(dir[0]):
#                     road = np.append(road,[[way[i+1][0]-diff,way[i+1][1]]],axis=0)
#                 if(dir[1]):
#                     road = np.append(road,[[way[i+1][0],way[i+1][1] + diff]],axis=0)
#                 break



        return [[y1+100,x1]]


   
