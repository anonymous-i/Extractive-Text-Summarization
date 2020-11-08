import math
'''Cluster moduel that clusterizes the scored sentences using the K-Means Clustering approach'''

class MakeClusters:
    def __init__(self):
        self.cluster1=list()
        self.cluster2=list()

    def formClusters(self,scr):
            centroid1 = max(scr.values())
            centroid2 = min(scr.values())
            
            sserror=0
            psserror=0
            scl1=0
            scl2=0
            dist=0
            dist2=0

            while(sserror<=psserror):
                psserror = sserror
                for dat in scr:
                    if(abs(scr[dat]-centroid1)<abs(scr[dat]-centroid2)):
                        self.cluster1.append(scr[dat])
                    else:
                        self.cluster2.append(scr[dat])
                for dat in self.cluster1:
                    sserror = sserror + abs(dat-pow(dat,2))
                for dat in self.cluster2:
                    sserror = sserror + abs(dat-pow(dat,2))
                    
                for cl1 in self.cluster1:
                    scl1 = scl1+cl1
                for cl2 in self.cluster2:
                    scl2 = scl2+cl2

                centroid1 = int(scl1/len(self.cluster1))
                centroid2 = int(scl2/len(self.cluster2))
            for dat in self.cluster1:
                dist = dist+ abs(dat-centroid1)
            for dat in self.cluster2:
                dist2 = dist2+abs(dat-centroid2)
            cs1 = dist/len(self.cluster1)
            cs2 = dist2/len(self.cluster2)
            print((100-(cs1+cs2)/2))
                

    def chooseSentences(self,scr):
        '''A method that selects the sentences for the summary'''
        summary =""
        self.cluster1.sort()
        self.cluster1.reverse()
        traversed = []
        for d in self.cluster1[:3]:
            for dat in scr:
                if d == scr[dat] and d not in traversed:
                    traversed.append(d)
                    summary = summary + dat +"\n"
        return summary
    

               
               
               
            

                
                
            
        
        
