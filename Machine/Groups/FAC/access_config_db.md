---
title: Accessing configuration database
description: 
published: 1
date: 2024-03-19T20:03:00.621Z
tags: 
editor: markdown
dateCreated: 2024-03-19T20:03:00.621Z
---

# FAC:Accessing configuration database

## Mongo

[Introduction to Mongo](https://docs.mongodb.com/manual/introduction/)

* Document database
* Each document is a record, which is composed of field and value pair (JSON)

### Acessing the database

#### Log into Docker container running the mongo server

* List of active containers: <code>docker container ls</code>
* Get container name
* Run bash in existing container: <code>docker container exec -it {CONTAINER_NAME} bash</code>
* Inside the container issue <code>mongo</code> to access the mongo shell.

#### Mongo Shell

* Issue <code>show dbs</code> to show existing dbs and their names.
* In order to use a secific db issue: <code>use {DB_NAME}</code>.
* Issuing <code>show collections</code> will show a list of the collections available for the db currently being used.

### Managing Documents

#### Finding documents
  
<code>db.configs.find()</code>: This command will return all documents in the ''configs'' collection.
  
Optionally you may supply a constraint document in order to filter the selected documents.
  
E.g.: 
* <code>db.configs.find( {discarded: true} )</code> will return all documents in which the field ''discarded'' is ''true''.
* <code>db.configs.find( {name: /.*beam.*/} )</code> will return all documents in which the field ''name'' has the '''beam''' substring.

Another useful parameter the ''find'' method accepts is a projection document of fields.
  
E.g.: <code>db.configs.find( {discarded: true}, {name: true} )</code> will return all documents in which the field ''discarded'' is ''true''. However, the documents returned will contain only '''_id''' and '''name''' fields. Note that the '''_id''' field will always be present, unless you explicitly remove it in the projection document (e.g.: <code>{_id: false, name: true}</code>).

#### Deleting documents

There are two methods available:
* deleteOne
* deleteMany

<code>db.configs.deleteMany({})</code> will delete all documents from the ''configs'' collection. BE CAREFUL!!

Just like the ''find'' method you can supply a constraint document.

<code>db.configs.deleteMany( {discarded: True} )</code> will delete all documents in which the field ''discarded'' is ''true''.

Be careful! Always check your constraint list issuing a ''find'' first.
    
E.g.: If you want to delete all documents that have the ''discarded'' field set to ''true'' first run a ''find'':
* <code>db.configs.find( {discarded: True} )</code> or
* <code>db.configs.find( {discarded: True} ).pretty()</code> or yet
* <code>db.configs.find( {discarded: True} ).count()</code> which returns the number of documents matched. 

After you are certain that these are the documents you wish to remove from the database you may proceed to delete.

For more check mongo documentation: 
* [https://docs.mongodb.com/manual/tutorial/query-documents/ Query Documents]
* [https://docs.mongodb.com/manual/tutorial/remove-documents/ Delete Documents]

### Restoring the database

Mongo makes two tools available for dealing with backup: ''mongodump'' and ''mongorestore''.

A backup is made every day and is currently being saved in NFS folder in PC lnls452-linux.

In order to restore the database, the ''sirius-configdb-restore.sh'' script should be ran. This script is available at the ''lnls-sirius/docker-config-db'' repository. When the ''mongorestore'' is ran the target database will lose all of its data, so be careful.

Three parameters must be supplied:
* The path for one of the backup files.
* The container name that is running the Mongo server database (usually config-db, <code>docker container ls</code> can be issued to check it).
* The docker network in which the container is running. (the name being used is config-service, you can check issuing <code>docker network ls</code>).

Note that the container that runs the Mongo server should be running.
