"""Create worksets from a list and set default visibility"""
import clr
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
from Autodesk.Revit import DB

doc =  DocumentManager.Instance.CurrentDBDocument

def create_worksets(d, names):
    for name in names:
        ws = DB.Workset.Create(d, name)

workset_names = ["DATUM ELEMENTS", "MAIN MODEL", "UNITS", "X_A_SITE_RVT", "X_M_MECHANICAL_RVT", "X_S_STRUCTURAL_RVT"]
        
if doc.IsWorkshared:
    t = DB.Transaction(doc, "Create Worksets")
    t.Start()
    
    # make your model changes here
    create_worksets(doc, workset_names)
    t.Commit()
    
    
    
    
# #chatGPT

# # check if the document is already workshared
# if not doc.IsWorkshared:
#     # make the document workshared
#     WorksharingUtils.EnableWorksharing(doc)

# # get the worksharing options
# options = WorksharingSaveAsOptions()
# options.SaveAsCentral = True

# # save the file as a central file
# doc.SaveAs(doc.PathName, options)

# # add a list of worksets
# workset_names = ["Workset1", "Workset2", "Workset3"]
# for name in workset_names:
#     Workset.Create(doc, name)

# # save the changes to the file
# doc.Save()