# FAC: Cookbook

Straightforward recipes for Accelerator Physics group projects and activities tasks. Command-line instructions are given for bash.

### Conventions
* `<arg>`: argument to be substituted by user

* `arg1|arg2`: alternative arguments to be selected from

* `[arg]`: optional argument

## CS-Studio

### Import lnls-sirius OPIs
To test and run lnls-sirius OPIs in CS-Studio, clone the `hla` repository if it is not already available, with

```
git clone https://github.com/lnls-sirius/hla
```

Import the projects containing the OPIs into CS-Studio, clicking on *File->Import...->Existing Projects into Workspace*. Then select the root directory and click *Finish*. Colour and font definitions used are retrieved from the Sirius web server.

### Set preferences
As we are currently using the SNS version of CS-Studio for tests, some default configurations are not adequate and need to be changed. For this, click on *Edit->Preferences* and set the following values (in other operating systems, *Preferences* may be located under another menu):

* *CSS Applications->Display->BOY*

    * *Color File*: click on *Browse...* and select the color.def file from the `common` project, imported according to the instructions above.

    * *Font File*: click on *Browse...* and select the font.def file from the `common` project, imported according to the instructions above.

    * *OPI Search Path*: `<path_to_hla_repository>/sirius/opi`.

    * *Top OPIs*: `launcher/main.opi`, where `launcher` was imported according to the instructions above.

* *CSS Applications->Display->BOY->OPI Editor*

    * *Schema OPI*: *(blank)*

* *CSS Applications->Trends->Data Browser*

    * *Archive Data Server URLs*: remove the `jdbc` entries

    * *Default Archiver Data Sources*: remove the `Inst` and `Accl` entries

* *CSS Core->E-Mail*

    * *SMTP Host*: *(blank)*

* *CSS Core->EPICS*

    * *addr_list*: `<epics_gateway_ip_address>`

## EPICS

### Create empty IOC from template
To create an empty IOC structure using the EPICS Base-provided `makeBaseApp.pl`, create a directory and, inside it, issue (assuming makeBaseApp.pl is in PATH)

```
makeBaseApp.pl -t ioc <ioc_name>
makeBaseApp.pl -t ioc -i -a <architecture> <ioc_name>
```
where `<architecture>` must be substituted by the host architecture (e.g., `linux-x86_64`.)

### Create empty PCASPy Channel Access Server
To create a PCASPy CAS simple structure, the script `instantiate_template.py` available in the [hla](https://github.com/lnls-fac/hla) repository at `sirius/iocs/pcaspy_template` can be used with

```
<path_to_hla>/sirius/iocs/pcaspy_template/instantiate_template.py <name> [-d <dest_dir>]
```

### Install ChannelFinder
Follow the [instructions in the ChannelFinder page](http://channelfinder.sourceforge.net/ChannelFinderService/installation.html) to install version 1.1.1. Some workarounds were needed and are described below with some additional recommendations for setting up a test installation; they are not recommended for a production installation, so the issues must be investigated.

* The JDK can be installed with `apt-get install default-jdk`.
* MySQL can be installed using `apt-get install mysql-server`. You can execute the SQL in the file provided with ChannelFinder by issuing `mysql -u <user> -p < <filename>`. MySQL will prompt you for the password.
* When creating the database connection in Glassfish, the names of the additional properties that must be defined are `serverName`, `databaseName`, `user`, and `password`.
* OpenLDAP can be installed using `apt-get install slapd`; run `dpkg-reconfigure slapd` and set the DNS domain name, organisation name, and administrator password, leaving other options as default. Then, configure phpldapadmin by setting the following variables in `/etc/phpldapadmin/config.php` to the values shown:

```
$servers->setValue('server','host','localhost');
// If the domain name is example.com, <DNS domain name>='dc=example,dc=com'
$servers->setValue('server','base',array(<DNS domain name>));
$servers->setValue('server','bind_id',array('cn=admin,'<DNS domain name>));
$config->custom->appearance['hide_template_warning'] = true;
```

Open `<nowiki>http://localhost/phpldapadmin</nowiki>` and log in using the administrator password you set for slapd. Then add the following items:
* Organisational units: `groups`, `users`.
* Groups (Posix Groups): `cf_admins`, `cf_channels`, `cf_properties`, `cf_tags`.
* Users (User Account): `<user name>`; add the user to the groups according to permissions.
If you get an error when adding user accounts, edit `/usr/share/phpldapadmin/lib/TemplateRender.php` and change `password_hash` to `password_hash_custom` in line 2469. 

For testing ChannelFinder with the Python API, it may be necessary to disable SSL certificate validation. You can do it editing the file restfullib.py before installation. Change the line `self.h = httplib2.Http()` to `self.h = httplib2.Http(disable_ssl_certificate_validation=True)`.

### Set Channel Access environment variables
To set the EPICS environment variables that define the IP addresses Channel Access will use to look for PVs, issue

```
export EPICS_CA_ADDR_LIST=<server_ip>
export EPICS_CA_AUTO_ADDR_LIST=no
```

where `<server_ip>` must be substituted by the broadcast, server or Gateway address to be used.

## Git

### Change working directory contents to specific release
To change the working directory contents to that of a release, inside the local repository issue

```
git checkout <version_tag>
```

where `<version_tag>` must be substituted by a valid release tag (e.g., vX.Y.Z for the procedure described [below][link].) To return to the master working directory, use

```
git checkout master
```

## GitHub

### Create a repository release

You need to be signed in to your GitHub account to be able to create a release; moreover, you need to have the appropriate permissions in the [lnls-fac](https://github.com/lnls-fac) organisation. With these requirements fulfilled, follow the instructions below:

* Go to the repository page on GitHub.

* Click on the *releases* link (below the repository description, preceded by number of releases).

* On the releases page, click on *Draft a new release*.

* On the new release page, fill in the fields with

    * Tag version: vX.Y.Z (e.g., v0.1.2), using the current version.

    * Release title: Version X.Y.Z, using the same version number (e.g., Version 0.1.2).

* Optionally, add a description.

* Click on *Publish release*.

The next pull from the remote repository will bring the tag corresponding to the release.

## Sirius Wiki

This section contains recipes for performing maintenance tasks on the Sirius Wiki.

### Access MySQL parameter tables

In the machine where Sirius Wiki is running, open the MySQL client with

```
mysql -u root -p
```

Then, select the `parameters` database:

```
USE parameters;
```

Some useful examples of commands to issue are


```
SHOW TABLES;
SELECT * FROM parameter;
SELECT * FROM parameter WHERE NAME LIKE "SI optics radiation%";
```

### Install the Parameters MediaWiki extension

In this recipe, we assume that MediaWiki and MySQL are already installed in the machine. First install a required package with (when prompted, choose to keep current local version of php.ini)

```
apt-get install php5-mysqlnd
```

Then download and copy the `Parameters` directory to the MediaWiki extensions directory using

```
cp -r Parameters /var/www/mediawiki-1.23.1/extensions
```

The extension's MySQL user and tables are created by the commands in the file `Parameters.sql` available in the `Parameters` directory. The user password is defined in that file and, if changed, must also be updated in the class `FacConnection` in the file `FacTable.php`. To create the user and tables, run (you will be prompted for the MySQL root user password)

```
mysql -u root -p < Parameters.sql
```

Finally, to install the extension, add the following line to the `/var/www/mediawiki-1.23.1/extensions/LocalSettings.php` file:

```
require_once "$IP/extensions/Parameters/Parameters.php";
```

 ### Reset user password

Inside the fac-wiki virtual machine, open the MySQL client with (you will be prompted for the MySQL root user password)

```
mysql -u root -p
```

Then issue the commands below, substituting `<user_name>` and `<new_password>`:

```
USE fac_wiki
UPDATE `user` SET user_password = CONCAT(':B:somesalt:', MD5(CONCAT('somesalt-', MD5('<new password>')))) WHERE user_name = '<user_name>';
```

## VirtualBox

### Manage virtual machines from the command-line

To obtain a list of available or running virtual machines (VMs), run

```
vboxmanage list vms|runningvms
```

You can start a VM on headless mode (without opening a window with its GUI) with

```
vboxmanage startvm <vm_name> --type headless
```

where `vm_name` is the VM name, that can be obtained with the `list vms` command given above.

To save the machine state or power it off, issue

```
vboxmanage controlvm <vm_name> savestate|poweroff
```

## Virtual Accelerator

### Start the virtual accelerator

To start the virtual accelerator (VA), IOCs, and Gateway in the va virtual machine created with [hla-vagrant](https://github.com/lnls-fac/hla-vagrant), issue

```
sirius-vaca.py 2>&1 > sirius-vaca.log & # then wait for server initialisation
sirius-va start viocs
gateway -sip <ip_address> -access ./GATEWAY.access -prefix FAC-VA-GATEWAY -server
```

`GATEWAY.access` is the file at the `fac` user's home directory. To run the VA in other machines, copy the file from `hla/salt/files` in the lnls-fac [hla-vagrant](https://github.com/lnls-fac/hla-vagrant) repository

### Stop the virtual accelerator

To stop the Gateway and IOCs in the va virtual machine created with [hla-vagrant](https://github.com/lnls-fac/hla-vagrant) and started as described [above][link], issue in the fac user's home directory

```
./gateway.killer
sirius-va stop viocs
```

To stop the virtual accelerator (VA), use ps to find the main process PID:

```
ps -elf | grep sirius-vaca.py
```

The output should look like the following lines if the VA is running:

```
Sample output:
 
0 S fac        336 31580  0  80   0 -  2615 pipe_w 16:03 pts/1    00:00:00 grep --color=auto (...)
0 S fac      31870 31580  7  80   0 - 182938 poll_s 15:56 pts/1   00:00:31 /usr/bin/python3  (...)
1 S fac      31874 31870  0  80   0 - 89354 poll_s 15:56 pts/1    00:00:00 /usr/bin/python3  (...)
1 S fac      31876 31870  0  80   0 - 89546 poll_s 15:56 pts/1    00:00:01 /usr/bin/python3  (...)
1 S fac      31878 31870 31  80   0 - 91611 poll_s 15:56 pts/1    00:02:08 /usr/bin/python3  (...)
1 S fac      31881 31870  0  80   0 - 89542 poll_s 15:56 pts/1    00:00:01 /usr/bin/python3  (...)
1 S fac      31883 31870 49  80   0 - 95086 poll_s 15:56 pts/1    00:03:22 /usr/bin/python3  (...)
```

The main process is that with the PID repeated five times on the the fifth column (one for each child process), 31870 in this example. To send the `SIGINT` signal to it, issue

```
kill -2 <main_process_pid>
```