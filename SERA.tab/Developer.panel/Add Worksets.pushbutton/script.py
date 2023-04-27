"""Create SERA Worksets"""
import clr
clr.AddReference("RevitServices")
import RevitServices
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager

clr.AddReference("RevitAPI")
from Autodesk.Revit import DB
clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import TaskDialog

doc = DocumentManager.Instance.CurrentDBDocument

def create_worksets(d, names):
    for name in names:
        ws = DB.Workset.Create(d, name)

workset_names = ["UNITS", "X_A_SITE_RVT", "X_M_MECHANICAL_RVT", "X_S_STRUCTURAL_RVT"]

# enable worksharing
if not doc.IsWorkshared:
    WorksharingUtils.EnableWorksharing("DATUM ELEMENTS", "MAIN MODEL")

if doc.IsWorkshared:
    t = DB.Transaction(doc, "Create Worksets")
    t.Start()
    # make your model changes here
    create_worksets(doc, workset_names)
    t.Commit()
    
message = TaskDialog()
message.Title = "Worksets Added"
message.MainInstruction = "SERA standard worksets have been added to this file. Next Steps:\n\n1. Save file to project folder\n\n2. Select Collaborate > Relinquish All Mine\n\n3. Select File > Close"
message.Show()