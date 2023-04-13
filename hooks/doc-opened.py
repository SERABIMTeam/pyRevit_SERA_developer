from pyrevit import forms
# forms.alert(message, title, body1, body2, footer)
from pyrevit import EXEC_PARAMS
from Autodesk.Revit.DB import ModelPathUtils

title = "Warning!"
message = "You've opened the central model. OMG!"
body = "No worries, all will be fine. Simply click OK, do not save, and close out of the file. Try creating a local from this file instead."

if EXEC_PARAMS.event_args.Document.IsWorkshared:

    modelPath = EXEC_PARAMS.event_args.Document.GetWorksharingCentralModelPath()
    centralPath = ModelPathUtils.ConvertModelPathToUserVisiblePath(modelPath)
    currentDocPath = EXEC_PARAMS.event_args.Document.PathName

    modifiedCentralPath = centralPath.replace("\\\\local.serapdx.com\\library\\Projects\\","P:\\")

    if  currentDocPath == modifiedCentralPath:
        forms.alert(message,title,body)
    else:
        pass
        #forms.alert("Nothing is wrong at all. Carry on.","Central Model Check", "Central File Path: \n" + modifiedCentralPath,"Current File Path: \n" + currentDocPath)

else:
    pass