# CON: LDAP server

##  Introduction

The LDAP server provides authorization and authentication support for the services running in our infrastructure. The following services describe the hierarchical levels set in the server.

##  Users 

All users belong to the **organizationalUnit** `ou=users,dc=lnls,dc=br`. A user belongs to the class **organizationalPerson** and has the attributes **cn** (should be used to log into the services), **sn** (person's name) and a **userPassword**.

##  Groups 

`ou=groups,dc=lnls,dc=br` is the top level of all groups in the server. Each group belongs to the class `groupOfNames` and its users are referenced by the attribute `member`.

**Obs.:** if the application is having troubles to read the group's members, it might be an authorization issue. In this case, try to append read permissions with the instructions in this [file](https://github.com/lnls-sirius/docker-openldap/blob/master/model.ldif){target=_blank}.

##  Configuring the applications to use the LDAP server 

In order to use the server with the options above, set your applications settings to reflect the following values:

|Attribute| Value |
|-|-|
|URL| ldap://10.0.6.57:389 |
|User Filter| (cn={0}) |
|User Base| ou=users,dc=lnls,dc=br |
|Bind Name| cn=admin,dc=lnls,dc=br |
|Bind Password| The one used in all Controls Group hosts. |
|Role Base| ou=<application>,ou=groups,dc=lnls,dc=br |
|Role Name| cn |
|Role Search| (member={0})  |

A role should be created for each application.
