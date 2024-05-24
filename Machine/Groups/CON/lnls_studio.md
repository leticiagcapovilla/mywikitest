# CON: Lnls-studio

##  Introduction 

The [Control System Studio](https://github.com/ControlSystemStudio/cs-studio/wiki){target=_blank} is a graphical tool based on [http://www.eclipse.org/ Eclipse] which offers many features to monitor and to operate controls systems, being maintained continuously and improved by developers from many laboratories and teaching institutes. Between the projects contained in the [CSS repository](https://github.com/ControlSystemStudio){target=_blank}, one of the them allows the generation of local and customised distributions according to the needs of the respective laboratory. This project, called [org.csstudio.product](https://github.com/ControlSystemStudio/org.csstudio.product) {target=_blank}, was, therefore, extended and modified to meet only our group's needs.

##  Project description 

|![](/img/groups/con/lnls_studio/Splash.png)|
|-|
|**Figure 1**: Lnls-studio's splash screen.|

The [lnls-studio project](https://github.com/lnls-sirius/lnls-studio){target=_blank} the version generated with the modifications for internal use in our group and future operations in the Sirius. There are three directories within this repository:

* `features/`: directory where the ''features'' which will be present in the new version can be added or removed. `org.csstudio.product.configuration.feature` contains the initial parameter definitions which LNLS-Studio will use as soon as it starts. To change them, edit the files contained in `org.csstudio.product.configuration.feature/rootfiles/configuration`, according to:

    * `plugin_customization.ini` - Allows the parameters configuration of each plugin which composes the distribution. Each property should be specified in the format `<plugin>/<propriedade>`. For example, `org.csstudio.alarm.beast/rdb_url=jdbc:postgresql://10.0.4.57:5432/lnls_alarms` defines the property `rdb_url` of the plugin `org.csstudio.alarm.beast`.
    * `jaas.conf` - Configuration of the login method of distribution. Essential for the alarm plugin.
    * `diirt/` - Contains the hosts addresses where the PVs are being provided.

`org.csstudio.product.feature`, in turn, defines which feature will be present in the distribution. Among the main features included so far this edition stand out the alarm client, the archiver's data viewer and the [https://github.com/kasemir/org.csstudio.display.builder display builder]. To add or remove features, edit the file [https://github.com/lnls-sirius/lnls-studio/blob/master/features/org.csstudio.product.feature/feature.xml `org.csstudio.product.feature/feature.xml`].

* `plugins/`: graphical definitions of the product, such as titles, icons, ''splash screen'' etc. All these definition can be found in `org.csstudio.product/`, notably in the file `plugin.xml`

* `repository/`: unification of the settings defined in the two folders above.

##  Distribution generation  

Three versions are available in [lnls-studio](https://github.com/lnls-sirius/lnls-studio){target=_blank}: `4.5.x` (''branch'' `master`), `4.4.x` e `4.3.x`. The compilation process uses [maven](https://maven.apache.org/){target=_blank} to create the binaries. Execute the following commands in the folder where the project was cloned:

```
$ git checkout <version>
$ mvn clean install
```

In the first execution, the process will take a long time to complete, since that many plugins used by maven itself will be downloaded. By default, these files are stored into `~/.m2`. From the second compilation on, the process is faster.

The generated distributions can be retrieved in the directory `repository/target/products` either compressed (`*.zip` or `*.tar.gz`) or uncompressed.

##  Download 

The pre-compiled distributions can be downloaded from this [link](http://10.0.4.57/lnls-studio/){target=_blank}.
