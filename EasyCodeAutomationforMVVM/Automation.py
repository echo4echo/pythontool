# /////////////////////////////////////////////////////////////////////////////////////
# ///        Name space: PropertyAutomation
# ///        File name : Automation
# ///        Description: Automatic generate the code of property change function
# ///        Version Nr:
# ///        Created data : 11/12/2018 1:13:09 PM
# ///        
# ///        Author: Han Liu
# ///        Copyright (c) 2018 All Rights Reserved  
# ///        
# /// Version History:
# ///*********************************************************************************
# ///        Date       Version        Author          Description
# ///*********************************************************************************
# ///   | 20.11.2018 |    1.0    |     Han Liu   |  Initial Version:
# ///  
# /// //////////////////////////////////////////////////////////////////////////////////
import os
import shutil

def main():

    InputDir = r'E:\LCPL\Git\NiMO_LiuHan\NiMO\NiMO\Model\Iparameters.cs'
    OutputDir = r'E:\LCPL\Git\NiMO_LiuHan\NiMO\NiMO\ViewModel\MainViewModel3.cs'
    
    parameterList = []
    
    #read out the parameters
    with open(InputDir,"r") as f:
        lines = f.readlines()
    f.close
    
    #creat the target file
    Newfile = open(OutputDir, 'w')
    Newfile.write("""   
////////////////////////////////////////////////////////////////////////////////////
///        Name space: NiMO.ViewModel
///        File name : MainViewModel2
///        Description: This code is automatic generate by tool
///        Created data : 11/12/2018 1:13:09 PM  
///        Author: Han Liu
///        Copyright (c) 2018 All Rights Reserved  
/// Version History:
///*********************************************************************************
///        Date       Version        Author          Description
///*********************************************************************************
///   | 20.11.2018 |    1.0    |     Han Liu   |  Initial Version:
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using GalaSoft.MvvmLight;
using GalaSoft.MvvmLight.Command;
using GalaSoft.MvvmLight.Messaging;

using NiMO.Model;

namespace NiMO.ViewModel
{
    public partial class MainViewModel : ViewModelBase
    {\n
    """
                  )
    
    for line in lines:
        if "public static Parameters" in line:
            #find the parameters name
            beginPosition = line.find("public static Parameters")
            endPosition = line.find(" = new")
            tempLength = len(" public static Parameters")
            beginPosition = beginPosition + tempLength
            paramter = line[beginPosition:endPosition]
            NewString = propertygenerator("Parameters", paramter)
            
            Newfile.write(NewString)
        elif "public static SettingControl" in line:
            #find the parameters name
            beginPosition = line.find("public static SettingControl")
            endPosition = line.find(" = new")
            tempLength = len(" public static SettingControl")
            beginPosition = beginPosition + tempLength
            paramter = line[beginPosition:endPosition]
            NewString = propertygenerator("SettingControl", paramter)
        
            Newfile.write(NewString)
            
        elif "public static DynamicCtrlData" in line:
            #find the parameters name
            beginPosition = line.find("public static DynamicCtrlData")
            endPosition = line.find("= new")
            tempLength = len(" public static DynamicCtrlData")
            beginPosition = beginPosition + tempLength
            paramter = line[beginPosition:endPosition]
            NewString = propertygenerator("DynamicCtrlData", paramter)
        
            Newfile.write(NewString)
            
        elif "public static string" in line:
            #find the parameters name
            beginPosition = line.find("public static string")
            endPosition = line.find(";")
            tempLength = len(" public static string")
            beginPosition = beginPosition + tempLength
            paramter = line[beginPosition:endPosition]
            NewString = propertygenerator("string", paramter)
        
            Newfile.write(NewString)
        
        
    Newfile.write("\t}\n}")
    
            
            #function to automatic generate the code
            
    f.close()
    
def propertygenerator(parameter_type, parameter):
    strprivate = " _" + parameter[0].lower() + parameter[1:]
    strbegin = "\n\t\t" + "private " + parameter_type + strprivate + ";"
    strfunctionline1 ="\n\t\t" + "public " + parameter_type +" " + parameter
    strfunctionline2 ="\n\t\t" + "{\tget { return " + strprivate +"; }"
    strfunctionline3 = "\n\t\t" + "\tset{ Set(ref" + strprivate + ", value);}"
    strfunctionline4 = "\n\t\t}\n"
    
    return strbegin + strfunctionline1 + strfunctionline2 + strfunctionline3 + strfunctionline4

if __name__ == "__main__":
    main()