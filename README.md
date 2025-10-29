In this repo I am learning and documenting how to make a Home Assistant Custom Integration. A few prequisites before you get started:
- You need to have Home Assistant installed. You can find instructions here: https://www.home-assistant.io/installation/
- Secondly, in your Home Assistant instance, you need to install the Home Assistant Community Store (HACS). This is carefully [explained here](https://www.home-assistant.io/blog/2024/08/21/hacs-the-best-way-to-share-community-made-projects/#how-to-install)

Once the above two prequisites are met, you should be able to open the HACS interface through http://IP:8123/hacs (for some http://homeassistant.local:8123/hacs should work).


# Adding the Custom Repository
The most right top button with the three dots is the menu button in the HACS interface. Click it and select "Custom Repositories". In the dialog that opens, you can add this repository (or any other of your liking) as a custom repository by simply pasting the GitHub URL (both the .git and non .git versions should work). For this repo you need to select "Integration" as the category.

The repository that you want to add is required to meet a few criteria before HACS will accept it. You can find the [criteria](https://hacs.xyz/docs/publish/integration):
```filetree
custom_components/INTEGRATION_NAME/__init__.py  // Of course, change INTEGRATION_NAME to your integration name
custom_components/INTEGRATION_NAME/PLATFORM_NAME.py  // Also, change PLATFORM_NAME to the type of integration you are making (e.g. light, sensor) more info: https://developers.home-assistant.io/docs/creating_platform_index/, or: https://www.home-assistant.io/integrations/?brands=featured
custom_components/INTEGRATION_NAME/manifest.json
README.md
hacs.json
```

Note that besides the structure, these files also need content. This repo provides a basic example. Also, you can also find more information in the corresponding files in this repo.

If you are interested in making your own custom integration, from here on you can follow [this video](https://www.youtube.com/watch?app=desktop&v=e3VwPb72Bbg). But of doing all of work directly in VS Code *on* HA, I recommend you make a repo and use the info we went through above.

# Json files explained
Unfortunately comments are not supported in json files. Therefore they are here with comments:
```manifest.json
{
    "domain": "Ewouts_Intergration",  // How it is named within the HA ecosystem
    "name": "Ewouts HACS Integration",  // The human friendly name of the integration
    "requirements": ["numpy"],  // Any Python dependencies required by the integration
    "iot_class": "local_polling",  // The type of integration (e.g., local polling, cloud push) more info: https://developers.home-assistant.io/docs/creating_integration_manifest/#iot-class
    "documentation": "https://github.com/EwoutBergsma/My_HACS_Integration",
    "version": "0.0.1",
    "codeowners": [],
    "dependencies": []  // What's the difference between dependencies and requirements?
}
```

```hacs.json
{
  "name": "Ewouts Awesome Integration"  // More info: https://www.hacs.xyz/docs/publish/start/#hacsjson
}
```

# Installing the Custom Integration
Once you have added the custom repository (to the store), you can install it through HACS by searching for its name (the one you set in `hacs.json`) in the HACS dashboard. Click on it and then click the "Download" button in the bottom right corner. After installation, restart Home Assistant to complete the setup. 

After that it should be available to add through the "Add Integration" button in the Home Assistant settings under "Devices & Services".


# TODO
- [ ] Currently when adding the integration, it will tell you to add it to `configuration.yaml` manually, instead of using the UI. I want this to be different.
- [ ] ChatGPT told me to make the folder without capital letters, not sure if it is right (i.e. `custom_components/ewouts_hacs_integration/
- [ ] ChatGPT told me to make the domain in `manifest.json` without capitals, not sure if it is right (i.e. "domain": "ewouts_hacs_integration")
