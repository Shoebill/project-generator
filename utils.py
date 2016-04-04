import os

def ApiDependency(version):
    string = '\t\t<dependency>\n'
    string += '\t\t\t<groupId>net.gtaun</groupId>\n'
    string += '\t\t\t<artifactId>shoebill-api</artifactId>\n'
    string += '\t\t\t<version>' + version + '</version>\n'
    string += "\t\t</dependency>\n"
    return string

def CommonDependency(version):
    string = '\t\t<dependency>\n'
    string += '\t\t\t<groupId>net.gtaun</groupId>\n'
    string += '\t\t\t<artifactId>shoebill-common</artifactId>\n'
    string += '\t\t\t<version>' + version + '</version>\n'
    string += '\t\t</dependency>\n'
    return string

def GtaunRepository():
    string = '\t\t<repository>\n'
    string += '\t\t\t<id>gtaun-public-repo</id>\n'
    string += '\t\t\t<name>GTAUN Public Repository</name>\n'
    string += '\t\t\t<url>http://repo.gtaun.net/content/groups/public</url>\n'
    string += '\t\t</repository>\n'
    return string

def MavenCompilerPlugin():
    string = '\t\t\t<plugin>\n'
    string += '\t\t\t\t<groupId>org.apache.maven.plugins</groupId>\n'
    string += '\t\t\t\t<artifactId>maven-compiler-plugin</artifactId>\n'
    string += '\t\t\t\t<version>3.5.1</version>\n'
    string += '\t\t\t\t<configuration>\n'
    string += '\t\t\t\t\t<compilerArgument>-parameters</compilerArgument>\n'
    string += '\t\t\t\t\t<source>1.8</source>\n'
    string += '\t\t\t\t\t<target>1.8</target>\n'
    string += '\t\t\t\t</configuration>\n'
    string += '\t\t\t</plugin>\n'
    return string

def MavenJarPlugin():
    string = '\t\t\t<plugin>\n'
    string += '\t\t\t\t<groupId>org.apache.maven.plugins</groupId>\n'
    string += '\t\t\t\t<artifactId>maven-jar-plugin</artifactId>\n'
    string += '\t\t\t\t<version>2.6</version>\n'
    string += '\t\t\t</plugin>\n'
    return string

def writePomXml(location, artifactId, groupId, version, author):
    with open(os.path.join(location, "pom.xml"), "a+") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write('<project xmlns="http://maven.apache.org/POM/4.0.0"\n' +
                    '\t\txmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n' +
                    '\t\txsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">\n\n')
        f.write('\t<modelVersion>4.0.0</modelVersion>\n\n')
        f.write('\t<groupId>' + groupId + '</groupId>\n')
        f.write('\t<artifactId>' + artifactId + '</artifactId>\n')
        f.write('\t<version>' + version + '</version>\n\n')
        f.write('\t<repositories>\n')
        f.write(GtaunRepository())
        f.write('\t</repositories>\n\n')
        f.write('\t<dependencies>\n')
        f.write(ApiDependency("1.2-SNAPSHOT") + '\n')
        f.write(CommonDependency("1.3-SNAPSHOT"))
        f.write('\t</dependencies>\n\n')
        f.write('\t<properties>\n')
        f.write('\t\t<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>\n')
        f.write('\t</properties>\n\n')
        f.write('\t<build>\n')
        f.write('\t\t<defaultGoal>clean install</defaultGoal>\n')
        f.write('\t\t<plugins>\n')
        f.write(MavenCompilerPlugin() + '\n')
        f.write(MavenJarPlugin())
        f.write('\t\t</plugins>\n')
        f.write('\t</build>\n\n')
        f.write('</project>')

def writeResourceFile(location, classPath, name, version, author, description):
    with open(os.path.join(location, 'src', 'main', 'resources', 'gamemode.yml'), 'a+') as f:
        f.write('class: ' + classPath + '\n')
        f.write('name: ' + name + '\n')
        f.write('version: ' + version + '\n')
        f.write('buildNumber: 0\n')
        f.write('buildDate: Unknown\n')
        f.write('authors: ' + author + '\n')
        f.write('description: ' + description + '\n')
    return

def writeMainClass(location, name, groupId):
    with open(os.path.join(location, name + '.java'), 'a+') as f:
        f.write('package ' + groupId + ';\n\n')
        f.write('import net.gtaun.shoebill.resource.Gamemode;\n')
        f.write('import org.slf4j.Logger;\n\n')
        f.write('public class ' + name + ' extends Gamemode {\n\n')
        f.write('\tprivate Logger logger;\n\n')
        f.write('\t@Override\n')
        f.write('\tprotected void onEnable() throws Throwable {\n')
        f.write('\t\tlogger = getLogger();\n')
        f.write('\t\t//Put initialization code here\n')
        f.write('\t}\n\n')
        f.write('\t@Override\n')
        f.write('\tprotected void onDisable() throws Throwable {\n')
        f.write('\t\t//Put dispose code here\n')
        f.write('\t}\n')
        f.write('}')
    return