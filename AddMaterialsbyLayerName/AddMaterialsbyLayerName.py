import rhinoscriptsyntax as rs
import random

#author Mesut Sallah
#date February 2021

def randomColor():
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    return R, G, B
    
def MaterialNameByLayer():
    
    layerNames = rs.LayerNames()
    options = ('All Layers', 'Selected Layers')
    
    if options:
        results = rs.ListBox(options, "Pick an option: Mesut")
        
        if results is None: return
        
        elif results == "All Layers":
            for i in layerNames:
                if i:
                    index = rs.LayerMaterialIndex(i)
                    if index == -1:
                        index = rs.AddMaterialToLayer(i)
                        rs.MaterialName(index, i)
                        materialColor = rs.MaterialColor(index, randomColor())
                
        
        else:
            selectedLayers = rs.GetLayers("Select the layers you want to add materials:", False)
            for i in selectedLayers:
                if i:
                    index = rs.LayerMaterialIndex(i)
                    if index >= -1:
                        index = rs.AddMaterialToLayer(i)
                        rs.MaterialName(index, i)
                        materialColor = rs.MaterialColor(index, randomColor())
                    
                    
                    
if __name__=="__main__":
    MaterialNameByLayer()
