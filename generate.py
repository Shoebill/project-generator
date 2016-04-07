import getpass
import os
import sys
import shutil

import utils

DEFAULT_PROJECT_NAME = "Example"
DEFAULT_GROUP_ID = "com.example"
DEFAULT_AUTHOR = getpass.getuser()
DEFAULT_DESCRIPTION = "This is an empty gamemode."
DEFAULT_VERSION = "1.0-SNAPSHOT"
DEFAULT_DIRECTORY_PATH = ""

def query_yes_no(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

def generateProject(name, artifactId, groupId, author, description, version, location):
    if os.path.exists(location):
        if query_yes_no(location + " already exists. Do you want to override it?"):
            retry = True
            while(shutil.rmtree(location) == False and retry == True):
                retry = query_yes_no("Could not remove " + location + ". Retry?")
            if retry == False:
                exit()
        else:
            exit()

    className = raw_input("Main Class Name (no blank spaces): ")

    sourcePath = os.path.join(location, 'src')
    testPath = os.path.join(sourcePath, 'test', 'java')
    sourceMainPath = os.path.join(sourcePath, 'main')
    sourceMainJavaPath = os.path.join(sourceMainPath, 'java')
    sourceMainResourcesPath = os.path.join(sourceMainPath, 'resources')

    packagePath = sourceMainJavaPath
    for dir in groupId.split('.'):
        packagePath = os.path.join(packagePath, dir)

    os.makedirs(packagePath)
    os.makedirs(testPath)
    os.makedirs(sourceMainResourcesPath)
    utils.writePomXml(location, artifactId, groupId, version, author)
    utils.writeResourceFile(location, groupId + "." + className, name, version, author, description)
    utils.writeMainClass(packagePath, className, groupId)

    print("\nThe project '" + name + "' has been generated successfully. You can now import it into your IDE.")
    print("For instructions on how to import a maven project into your IDE you can take a look here:")
    print("IDEA: https://www.jetbrains.com/help/idea/2016.1/importing-project-from-maven-model.html")
    print("Eclipse: https://books.sonatype.com/m2eclipse-book/reference/creating-sect-importing-projects.html")
    print("NetBeans: http://www.tutorialspoint.com/maven/maven_netbeans.htm")

    return

def main():

    print("******************************")
    print("* Shoebill Project Generator *")
    print("* Version: 1.0               *")
    print("* Author: 123marvin123       *")
    print("******************************")

    print("\nThis tool will create a maven project for you.\n")
    projectName = raw_input("Project Name [" + DEFAULT_PROJECT_NAME + "]: ").strip()
    if len(projectName) <= 0:
        projectName = DEFAULT_PROJECT_NAME
    artifactId = projectName.lower()

    groupId = raw_input("Group ID [" + DEFAULT_GROUP_ID + "]: ").strip()
    if len(groupId) <= 0:
        groupId = DEFAULT_GROUP_ID

    author = raw_input("Author [" + DEFAULT_AUTHOR + "]: ").strip()
    if len(author) <= 0:
        author = DEFAULT_AUTHOR

    description = raw_input("Description [" + DEFAULT_DESCRIPTION + "]: ").strip()
    if len(description) <= 0:
        description = DEFAULT_DESCRIPTION

    version = raw_input("Version [" + DEFAULT_VERSION + "]: ").strip()
    if len(version) <= 0:
        version = DEFAULT_VERSION

    DEFAULT_DIRECTORY_PATH = os.path.join(os.getcwd(), projectName)
    location = raw_input("Project Location [" + DEFAULT_DIRECTORY_PATH + "]: ").strip()
    if len(location) <= 0:
        location = DEFAULT_DIRECTORY_PATH

    generateProject(projectName, artifactId, groupId, author, description, version, location)

    return

if __name__ == "__main__":
    main()