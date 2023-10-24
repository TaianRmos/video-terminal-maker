def create_vbs_writer(project_name, vbs_title, vbs_content, want_loop):
    # Creates the content of the file depending on if the user wants a loop or not
    if want_loop:
        content = f'''# Creates the content of the file depending on if the user wants a loop or not
content = """Do
result = MsgBox("{vbs_content}", vbOKCancel, "{vbs_title}")

If result = vbOK Then
' User clicked OK
Set objShell = CreateObject("WScript.Shell")
objShell.Run "{project_name}.exe", 1, False

Set objShell = CreateObject("WScript.Shell")
objShell.Run "wscript.exe {project_name}.vbs", 1, False

Else
' User clicked Cancel or closed the message box
Set objShell = CreateObject("WScript.Shell")
objShell.Run "{project_name}.exe", 1, False

Set objShell = CreateObject("WScript.Shell")
objShell.Run "wscript.exe {project_name}.vbs", 1, False

End If

loop"""


with open("{project_name}.vbs", 'w') as vbs_file:
    vbs_file.write(content)'''
    
    else:
        content = f'''# Creates the content of the file depending on if the user wants a loop or not
content = """result = MsgBox("{vbs_content}", vbOKCancel, "{vbs_title}")

If result = vbOK Then
' User clicked OK
Set objShell = CreateObject("WScript.Shell")
objShell.Run "{project_name}.exe", 1, True

Else
' User clicked Cancel or closed the message box
Set objShell = CreateObject("WScript.Shell")
objShell.Run "{project_name}.exe", 1, True

End If"""


with open("{project_name}.vbs", 'w') as vbs_file:
    vbs_file.write(content)'''

    
    with open(f"set_vbs.py", 'w') as py_file:
        py_file.write(content)