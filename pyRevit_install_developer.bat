:: clone latest version of pyRevit on GitHub to local repository
:: 'base' is the deployment type, see list of types in the pyRevitFile
:: 'base' installs pyRevit dependencies as well as the pyRevit Revit addin, same as exe
pyrevit clone pyRevit_base base --dest="%ProgramData%\Autodesk\pyRevit"

:: attach pyRevit to specified installed versions of Revit (adds manifest file to ProgramData)
:: BIM is currently not supporting Revit 2020 or earlier versions
pyrevit attach pyRevit_base default 2021 --allusers
pyrevit attach pyRevit_base default 2022 --allusers
pyrevit attach pyRevit_base default 2023 --allusers
pyrevit attach pyRevit_base default 2024 --allusers

pyrevit extend ui SERA_user https://github.com/SERABIMTeam/pyRevit_SERA_user.git --dest="%ProgramData%\Autodesk\pyRevit\extensions"
pyrevit extend ui SERA_developer https://github.com/SERABIMTeam/pyRevit_SERA_developer.git --dest="%ProgramData%\Autodesk\pyRevit\extensions"